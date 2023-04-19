osz2tja
=======

osz2tja is a program that converts osu!'s beatmaps to TJA, a standard format supported by many Taiko Simulators.

**English** | [简体中文](README.zh-cn.md)

## Usage

Simply enter the following command in the terminal:
```
python main.py <source .osz filename> <output path>
```

osz2tja will read .osz version files and display all versions along with their overall difficulties, like:
```
====== Difficulty Selection ======
Index  Difficulty  Version
(0):   8           xxxx(Insane)
(1):   6           ddddd(Hard)
(2):   4           ddsadf(Normal)
(3):   2           xxxxx(Easy)
Oni:
Hard:
Normal:
Easy:
```
Please follow the prompts to match the current beatmap's difficulties with the difficulies of a .tja file.

For example: If you want to match the "Insane" difficulty to the Oni difficulty, enter it's index number (which is 0) after the "Oni:" prompt.
If you don't want to convert a difficulty, enter "-1" in its prompt.

Following a successful match, osz2tja will generate a .tja file and extract the audio file to the output path, creating a new folder named after the title.
