from osu2tja.osu2tja import osu2tja, reset_global_variables
from zipfile import ZipFile, is_zipfile
from typing import Dict, List
from os import path
import os
import optparse
from io import TextIOWrapper


def extract_osu_file_info(file) -> Dict[str, object]:
    line: str = file.readline()
    result: Dict[str, object] = dict()
    print(type(line))
    while line != None:
        if line.startswith("Version:"):
            result["version"] = line.split(":")[1].strip()
        elif line.startswith("OverallDifficulty:"):
            result["difficulty"] = float(line.split(":")[1])
        elif line.startswith("TitleUnicode:"):
            result["title"] = line.split(":")[1].strip()
        elif line.startswith("AudioFilename:"):
            result["audio"] = line.split(":")[1].strip()

        if len(result.keys()) == 4:
            return result
        line = file.readline()
    return result


def convert(source_path: str, target_path: str) -> None:
    if not is_zipfile(source_path):
        print(f"{source_path} is not a zip file")
        return

    osu_zip: ZipFile = ZipFile(source_path, "r")
    osu_files = [filename for filename in osu_zip.namelist()
                 if filename.endswith(".osu")]
    osu_infos = list()
    for filename in osu_files:
        fp = TextIOWrapper(osu_zip.open(filename, "r"), encoding="utf-8")
        osu_info = extract_osu_file_info(fp)
        fp.close()
        osu_info["filename"] = filename
        osu_infos.append(osu_info)
    original_audio_name = osu_infos[0]["audio"]
    title = osu_infos[0]["title"]
    new_audio_name = title + \
        path.splitext(original_audio_name)[-1]

    # interactive mode, show all difficulties to user
    print("====== Difficulties Selection ======")
    print("Index\tDifficulty\tVersion")
    osu_infos.sort(key=lambda x: x["difficulty"], reverse=True)
    for i, osu_info in enumerate(osu_infos):
        print(f"({i}):\t{osu_info['difficulty']}\t{osu_info['version']}")

    print()
    print("Please select difficulties(-1 if not available):")
    oni_index = int(input("Oni:"))
    hard_index = int(input("Hard:"))
    normal_index = int(input("Normal:"))
    easy_index = int(input("Easy:"))

    head = []
    oni_contents = []
    hard_contents = []
    normal_contents = []
    easy_contents = []
    if oni_index != -1:
        reset_global_variables()
        oni_fp = TextIOWrapper(osu_zip.open(
            osu_infos[oni_index]["filename"]), encoding="utf-8")
        level = int(osu_infos[oni_index]["difficulty"])
        head, oni_contents = osu2tja(oni_fp, "Oni", level, new_audio_name)
        oni_fp.close()
    if hard_index != -1:
        reset_global_variables()
        hard_fp = TextIOWrapper(osu_zip.open(
            osu_infos[hard_index]["filename"]), encoding="utf-8")
        level = int(osu_infos[hard_index]["difficulty"])
        head, hard_contents = osu2tja(hard_fp, "Hard", level, new_audio_name)
        hard_fp.close()
    if normal_index != -1:
        reset_global_variables()
        normal_fp = TextIOWrapper(osu_zip.open(
            osu_infos[normal_index]["filename"]), encoding="utf-8")
        level = int(osu_infos[normal_index]["difficulty"])
        head, normal_contents = osu2tja(
            normal_fp, "Normal", level, new_audio_name)
        normal_fp.close()
    if easy_index != -1:
        reset_global_variables()
        easy_fp = TextIOWrapper(osu_zip.open(
            osu_infos[easy_index]["filename"]), encoding="utf-8")
        level = int(osu_infos[easy_index]["difficulty"])
        head, easy_contents = osu2tja(easy_fp, "Easy", level, new_audio_name)
        easy_fp.close()

    # extract audio
    storage_path = path.join(target_path, title)
    os.mkdir(storage_path)
    osu_zip.extract(original_audio_name, storage_path)
    os.rename(path.join(storage_path, original_audio_name),
              path.join(storage_path, new_audio_name))
    print("Extract Audio Done!")
    # saving tja
    with open(path.join(storage_path, title+".tja"), "w+") as f:
        f.write("\n".join(head))
        f.write("\n")
        f.write("\n".join(oni_contents))
        f.write("\n")
        f.write("\n".join(hard_contents))
        f.write("\n")
        f.write("\n".join(normal_contents))
        f.write("\n")
        f.write("\n".join(easy_contents))
    print("Tja converted!")
    osu_zip.close()


if __name__ == "__main__":
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()
    convert(args[0], args[1])
