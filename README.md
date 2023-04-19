osz2tja
=======

osz2tja is a program that converts osu!'s beatmaps to TJA, a standard format supported by many Taiko Simulators.

**English** | [简体中文](README.zh-cn.md)

## Usage

Simply enter the following command::
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

For example, if you want to match the "xxxx(Insane)" version to the Oni difficulty, enter "0" after the "Oni:" prompt.
If you want to disable a difficulty, enter "-1.".

Following a successful match, osz2tja will generate a .tja file and extract the audio file to the output path, creating a new folder named after the title.
