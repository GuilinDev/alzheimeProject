import os
from Bio.Affy import CelFile

current_dir = os.path.dirname(__file__)
print(current_dir)
unzip_dir = os.path.join(current_dir, "GSE84422")
print(unzip_dir)

with open(unzip_dir + "/GSM2233971_51294hg133a11.CEL", "r") as handle:
    c = CelFile.read_v3(handle)

print(c.stdevs)
