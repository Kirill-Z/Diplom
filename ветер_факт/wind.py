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
    #print(file_list[0][1])
    print(len(file_list[1]))
    correctData = []

    for i in range(len(file_list)):
        correctData.append([])

    numRows = 0
    for i in range(len(file_list)):
        if file_list[i][0] == '04':
            correctData[numRows].append(file_list[i][0])
            correctData[numRows].append(file_list[i][1])
            numRows += 1
            for j in range(0, len(file_list[i])):
                if 1442 < j < 1532:
                    print(numRows)
                    correctData[numRows-1].append(file_list[i][j])

    print(correctData[0])
