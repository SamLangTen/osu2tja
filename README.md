osz2tja
=======

osz2tja is a converter to convert OSU! beatmap to TJA, which is a common format supported by a series of Taiko Simulator.

**English**|[简体中文](README.zh-cn.md)

## Usage

Just simply input the following command:
```
python main.py <source .osz filename> <output path>
```

osz2tja will read version files in .osz and exhibit all versions with their overall difficulties, like:
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

Please follow the prompts to match the difficulty versions of OSU and difficulies of Taiko no Tatsujin.

For example, input "0" after the "Oni:" prompt if you want to match "xxxx(Insane)" version to Oni difficulty.
Please input "-1" if you want to disable a difficulty.

After matching, osz2tja will generate .tja file and extract audio file to the output path, with a new-created folder named after title.
