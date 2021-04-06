import pandas as pd
import os
import re

def gettingNeedData(windDirection):
    numRows = 0
    if windDirection == '04':
        correctData = 'correctDataUGRD_' + file
        correctData = []
    elif windDirection == '05':
        correctData = 'correctDataVGRD_' + file
        correctData = []

    for i in range(len(data_from_file)):
        if data_from_file[i][0] == windDirection:
            correctData.append([])
            correctData[numRows].append(data_from_file[i][0])
            correctData[numRows].append(data_from_file[i][1])
            numRows += 1
            for j in range(0, len(data_from_file[i])):
                if 1442 < j < 1532:
                    correctData[numRows - 1].append(data_from_file[i][j])
    return correctData


PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/EarlyData/Project/DATA_GFS/"

for file in os.listdir(PATH):
    if re.match('\d{10}_\d{2}.csv', file):
        currentFile = PATH + file
        file_reader = pd.read_csv(currentFile, sep='/s', skiprows=1, header=None, engine='python')
        file_reader.dropna(inplace=True)
        data_from_file = file_reader.values.tolist()  # Getting a list of data from a file

        for i in range(0, 70):  # 70 lines in each gfc file
            data_from_file[i] = data_from_file[i][0].split()


        correctDataUGRD = gettingNeedData('04')
        correctDataVGRD = gettingNeedData('05')

        speedWind = []
        numRowsForSpeed = 0
        for i in range(0, len(correctDataVGRD)):
            speedWind.append([])
            speedWind[numRowsForSpeed].append(correctDataVGRD[i][1])
            numRowsForSpeed += 1
            for j in range(2, len(correctDataVGRD[i])):
                speedWind[numRowsForSpeed-1].append(((float(correctDataUGRD[i][j])**2)+(float(correctDataVGRD[i][j])**2))**(1/2))

        print(len(speedWind))


