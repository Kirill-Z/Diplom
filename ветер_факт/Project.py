import os
import pandas as pd

cwd = os.getcwd()

os.chdir("/home/ubuntu/Desktop/Diplom/ветер_факт")

os.listdir(".")

file = 'USDD_2015_01 (1).xlsx'
x1 = pd.ExcelFile(file)
print(x1.sheet_names)
df1 = x1.parse('USDD_2015_01', usecols=[0, 1, 2, 3, 4, 6, 7, 8])

data = df1.values.tolist()
lengthData = len(data)

for i in range(lengthData):
    del data[i][0]
    del data[i][1]

for i in range(lengthData):
    for j in range(5):
        data[i][j] = int(data[i][j])

for i in range(lengthData):
    if data[i][2] == 30:
        data[i][2] = 3

for i in range(lengthData):
    data[i][0] = str(data[i][0])+str(data[i][1])+str(data[i][2])
    del data[i][2]
    del data[i][1]

for i in range(5):
    print(data[i])