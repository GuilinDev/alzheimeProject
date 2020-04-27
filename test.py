# 任务1： 拷贝阿尔兹海默病人的源文件到这个文件下

# 任务2： 使用numpy或者pandas读取病人源文件


# step1：读入table1_description.xlsx,这是一个描述性的table，表示我找到的数据集及他的相关信息
import pandas as pd
from pandas import DataFrame
import os

# Get the current dir
current_dir = os.path.dirname(__file__)
print(current_dir)
# Direct to input Source
inputSourceFilesPath = os.path.join(current_dir, "inputSource")

# table1 = DataFrame(pd.read_excel(os.path.join(inputSourceFilesPath, 'table1_description.xlsx')))
# print(table1)
#
# # step2：读入table2_demography.xlsx,这是对每一个数据集进行的描述
# table2 = DataFrame(pd.read_excel(os.path.join(inputSourceFilesPath, 'table2_demography.xlsx')))
# print(table2)
#
# # step3： 读入table3_21brainRegions.xlsx，这是对每一个脑区的分组，接下来就是根据这个分组对每一个脑区分别进行分析
# # table3中有21个sheet，先得到每个sheet的名称，以及得到每个sheet中的内容
#
# # 方法一：
# x1 = pd.ExcelFile(os.path.join(inputSourceFilesPath, 'table3_21brainRegions.xlsx'))
# sheet_names = x1.sheet_names
# print(sheet_names)
# df = x1.parse(sheet_names)
# print(df)
# # 结果中为啥最后两个sheet的格式和前面不一样？

# 方法二：
# df = pd.read_excel('table3_21brainRegions.xlsx', None)
# df.keys()
# print(df)

# step4：unzip all the cel.gz under the directory
import zipfile

# 试试方法一：将path更改到需要解压的文件夹：
os.chdir('D:\alzheimeProject\GSE84422')
os.getcwd()
retval = os.getcwd()
print("%s" % retval)
# OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: 'D:\x07lzheimeProject\\GSE84422'
# 此处我想把路径变成GSE84422的文件夹，然后下面解压在inputSource文件夹中，为什么此处显示文件名不正确？
extracting = zipfile.ZipFile('.gz')
extracting.extract('D:\alzheimeProject\inputSource')
extracting.close()

# 试试方法二：用open函数直接打开需要解压的文件夹
os.open('D:\alzheimeProject\GSE84422', 'r')
extracting = zipfile.ZipFile('.gz')
extracting.extract('D:\alzheimeProject\inputSource')
extracting.close()
# TypeError: open() missing required argument 'flags' (pos 2)
# 加入参数'r'时，TypeError: an integer is required (got type str)

# 试试方法三：
# gz： 即gzip，通常只能压缩一个文件。与tar结合起来就可以实现先打包，再压缩。这句笔记还不能理解意思，先放在这儿，慢慢体会。
import gzip


def un_gz(file_name):
    "D:\alzheimeProject\GSE84422"
    f_name = file_name.replace(".gz", "")
    g_file = gzip.GzipFile(file_name)
    open(f_name, "wb+").write(g_file.read("D:\alzheimeProject\inputSource"))
    g_file.close()
# 没反应？哪里错了？

# # step 5 parse one .cel file
# from Bio.Affy import CelFile
# with open("GSE84422/GSM2233971_51294hg133a11.CEL", "r") as handle:
#     c = CelFile.read_v3(handle)
#
# c.version = 3
# print("%i by %i array" % c.intensities.shape)
#
# # step 6 install PyAffy
# pip install pyaffy
# # 显示douban.com untrust，装不上
# # 用github中setup的代码还是装不上，我想是不是还得经历一回儿powershell啊？
