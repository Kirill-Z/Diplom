import pandas as pd
import os
import re


def getting_need_data(wind_direction):
    num_rows = 0
    if wind_direction == '04':
        correct_data = 'correctDataUGRD_' + file
        correct_data = []
    elif wind_direction == '05':
        correct_data = 'correctDataVGRD_' + file
        correct_data = []

    for i in range(len(data_from_file)):
        if data_from_file[i][0] == wind_direction and data_from_file[i][1] == '21':
            correct_data.append([])
            correct_data[num_rows].append(data_from_file[i][0])
            correct_data[num_rows].append(data_from_file[i][1])
            num_rows += 1
            for j in range(0, len(data_from_file[i])):
                if 1435 < j < 1614:
                    correct_data[num_rows - 1].append(data_from_file[i][j])
    return correct_data


def wind_speed_calculation(correct_data_VGRD, correct_data_UGRD):

    speed_wind = 'speed_wind_' + file
    speed_wind = []

    for i in range(0, len(correct_data_VGRD)):
        speed_wind.append(file)  #
        speed_wind.append(file[slice(0, 4)])
        speed_wind.append(int(file[slice(4, 6)]))
        speed_wind.append(int(file[slice(6, 8)]))
        speed_wind.append(int(file[slice(11, 13)]))
        speed_wind.append(correct_data_VGRD[i][1])

        print(correct_data_VGRD[i])
        for j in range(2, len(correct_data_VGRD[i])):
            speed_wind.append(((float(correct_data_UGRD[i][j]) ** 2) +
                                                      (float(correct_data_VGRD[i][j]) ** 2)) ** (1 / 2))
    return speed_wind


PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/part_of_directory_2016/"
my_file = open('/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/part_of_directory_2016/data_for_points_around_Tolmachevo_01_2016', 'w')
my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
speed_wind = []
reference_num = 0

for file in sorted(os.listdir(PATH)):
    if re.match('\d{10}_\d{2}', file):
        currentFile = PATH + file
        file_reader = pd.read_csv(currentFile, sep='/s', skiprows=1, header=None, engine='python')
        file_reader.dropna(inplace=True)
        data_from_file = file_reader.values.tolist()  # Getting a list of data from a file

        for i in range(0, 70):  # 70 lines in each gfc file
            data_from_file[i] = data_from_file[i][0].split()

        correct_data_UGRD = getting_need_data('04')
        correct_data_VGRD = getting_need_data('05')

        speed_wind.append(wind_speed_calculation(correct_data_VGRD, correct_data_UGRD))

        # Calculates the day based on the lead time
        if 24 <= int(speed_wind[reference_num][4]) < 48:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - 24
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + 1
        elif 48 <= int(speed_wind[reference_num][4]) < 72:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - 48
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + 2
        elif int(speed_wind[reference_num][4]) >= 72:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - 72
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + 3

        # Calculates a month based on a day
        if int(speed_wind[reference_num][2] == 1) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 2):
            if int(speed_wind[reference_num][1]) % 4 == 0 and int(speed_wind[reference_num][3]) > 29:
                speed_wind[reference_num][3] = speed_wind[reference_num][3] - 29
                speed_wind[reference_num][2] += 1
            elif int(speed_wind[reference_num][1]) % 4 != 0 and int(speed_wind[reference_num][3]) > 28:
                speed_wind[reference_num][3] = speed_wind[reference_num][3] - 28
                speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 3) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 4) and int(speed_wind[reference_num][3]) > 30:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 30
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 5) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 6) and int(speed_wind[reference_num][3]) > 30:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 30
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 7) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 8) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 9) and int(speed_wind[reference_num][3]) > 30:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 30
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 10) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 11) and int(speed_wind[reference_num][3]) > 30:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 30
            speed_wind[reference_num][2] += 1
        if int(speed_wind[reference_num][2] == 12) and int(speed_wind[reference_num][3]) > 31:
            speed_wind[reference_num][3] = speed_wind[reference_num][3] - 31
            speed_wind[reference_num][2] += 1

        # Calculation of the year based on data by months (used when the month value overflows > 13)
        if int(speed_wind[reference_num][2]) > 12:
            speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
            speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1

        reference_num += 1

# print(len(str(speed_wind[reference_num-1])))
# Sorting data in a list by year
#for i in range(0, len(speed_wind)):
#    sorted(str(speed_wind[i][1]))

#print(speed_wind[1])
# Sort date by month
#for i in range(0, len(speed_wind)):
#    if int(speed_wind[i][1]) != 2017:
#        sorted(str(speed_wind[i][2]))

# Sort date by day
#for i in range(0, len(speed_wind)):
#    if int(speed_wind[i][2]) != :
#        sorted(str(speed_wind[i][2]))


# Writing data to a file
for i in range(0, len(speed_wind)):
    for j in range(0, len(speed_wind[i])):
        if len(str(speed_wind[i][j])) == 1:
            my_file.write(str(speed_wind[i][j]) + '  |   ')
        elif len(str(speed_wind[i][j])) == 2:
            my_file.write(str(speed_wind[i][j]) + ' |   ')
        else:
            my_file.write(str(speed_wind[i][j]) + ' |   ')
    my_file.write('\n')


my_file.close()
print('The end of the script')