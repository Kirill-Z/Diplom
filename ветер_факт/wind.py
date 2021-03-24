import pandas as pd

with open('/home/ubuntu/Desktop/Diplom/DATA_GFS/2015010100_00') as r_file:
    file_reader = pd.read_csv(r_file, sep='/s', skiprows=1, header=None, engine='python')
    count = 0
    occurNum = 2
    pattern = '/-?/d{1,}'


    file_reader.dropna(inplace=True)
    file_list = file_reader.values.tolist()

    for i in range(0, 70):
        file_list[i] = file_list[i][0].split()

    correctDataUGRD = []
    correctDataVGRD = []
    numRows = 0
    for i in range(len(file_list)):
        if file_list[i][0] == '04':
            correctDataUGRD.append([])
            correctDataUGRD[numRows].append(file_list[i][0])
            correctDataUGRD[numRows].append(file_list[i][1])
            numRows += 1
            for j in range(0, len(file_list[i])):
                if 1442 < j < 1532:
                    correctDataUGRD[numRows-1].append(file_list[i][j])

    numRows = 0
    for i in range(len(file_list)):
        if file_list[i][0] == '05':
            correctDataVGRD.append([])
            correctDataVGRD[numRows].append(file_list[i][0])
            correctDataVGRD[numRows].append(file_list[i][1])
            numRows += 1
            for j in range(0, len(file_list[i])):
                if 1442 < j < 1532:
                    correctDataVGRD[numRows-1].append(file_list[i][j])

    speedWind = []
    numRows = 0
    for i in range(0, len(correctDataVGRD)):
        speedWind.append([])
        speedWind[numRows].append(correctDataVGRD[i][1])
        numRows += 1
        for j in range(2, len(correctDataVGRD[i])):
            speedWind[numRows-1].append(((float(correctDataUGRD[i][j])**2)+(float(correctDataVGRD[i][j])**2))**(1/2))


    print(len(speedWind))
    #for i in range(0, len(speedWind)):
    print(speedWind[7])


