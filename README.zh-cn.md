osz2tja
=======

osz2tja能将OSU!游戏的谱面转换成太鼓模拟器能读取的TJA文件。

[English](README.md)|**简体中文**

## 用法

只需简单地输入以下命令：
```
python main.py <源.osz文件名> <输出路径>
```

osz2tja会读取.osz内的所有.osu子谱面，并输出：
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

根据提示匹配OSU的难度版本和太鼓达人的难度。

例如，如果要将“xxxx(Insane)”版本与太鼓的魔王难度匹配，则在“Oni:”提示后输入“0”。
如果您想禁用难度，请输入“-1”。

匹配后osz2tja会生成.tja文件，并将音频文件解压到输出路径下以title命名的文件夹中。
