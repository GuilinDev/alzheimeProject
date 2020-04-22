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

table1 = DataFrame(pd.read_excel(os.path.join(inputSourceFilesPath, 'table1_description.xlsx')))
print(table1)

# step2：读入table2_demography.xlsx,这是对每一个数据集进行的描述
table2 = DataFrame(pd.read_excel(os.path.join(inputSourceFilesPath, 'table2_demography.xlsx')))
print(table2)

# step3： 读入table3_21brainRegions.xlsx，这是对每一个脑区的分组，接下来就是根据这个分组对每一个脑区分别进行分析
# table3中有21个sheet，先得到每个sheet的名称，以及得到每个sheet中的内容

# 方法一：
x1 = pd.ExcelFile(os.path.join(inputSourceFilesPath, 'table3_21brainRegions.xlsx'))
sheet_names = x1.sheet_names
print(sheet_names)
df = x1.parse(sheet_names)
print(df)
# 结果中为啥最后两个sheet的格式和前面不一样？

# 方法二：
# df = pd.read_excel('table3_21brainRegions.xlsx', None)
# df.keys()
# print(df)

# # step4：unzip all the cel.gz under the directory

# step 5 parse one .cel file
from Bio.Affy import CelFile
with open("GSE84422/GSM2233971_51294hg133a11.CEL", "r") as handle:
    c = CelFile.read_v3(handle)

c.version = 3
print("%i by %i array" % c.intensities.shape)











# from Pandas import (series, head_map_filter, row_iter)
# from typing import (NamedTuple, Callable, List, Tuple, Iterable, Dict, Any)
#
# RawPairIter = Iterable[Tuple[float, float]]
#
# class Pair(NamedTuple):
#     x: float
#     y: float
#
# pairs: Callable[[RawPairIter], List[Pair]] \
#     = lambda source: list(Pair(*row) for row in source)
#
# def raw_data() -> Dict[str, List[Pair]]:
#     with open("annotation96.csv") as source:
#         data = tuple(head_map_filter(row_iter(source)))
#         mapping = {
#             id_str: pairs(series(id_num, data))
#             for id_num, id_str in enumerate(
#                  ['I', 'II', 'III', 'IV'])
#         }
#     return mapping
