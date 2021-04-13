import pandas as pd
import os
import re


# Obtaining data on the direction of wind speed
def getting_need_data(wind_direction):
    num_rows = 0
    if wind_direction == '04':  #
        correct_data = 'correctDataUGRD_' + file
    elif wind_direction == '05':
        correct_data = 'correctDataVGRD_' + file

    correct_data = []
    for i in range(len(data_from_file)):
        if data_from_file[i][0] == wind_direction and data_from_file[i][
            1] == '21':  # Level 21 corresponds to 10m above the ground
            correct_data.append([])
            correct_data[num_rows].append(data_from_file[i][0])  # Adding wind direction information
            correct_data[num_rows].append(data_from_file[i][1])  # Adding Level Information
            num_rows += 1

            for j in range(0, len(data_from_file[i])):
                if j == 1528:  # 1528 corresponds to the point Tolmachevo
                    correct_data[num_rows - 1].append(data_from_file[i][j])
    return correct_data


def adding_data_to_the_speed_list(list_correct_data):
    speed_wind = 'speed_wind_' + file
    speed_wind = []

    for i in range(0, len(list_correct_data)):
        speed_wind.append(file)                      # Adding a file name
        speed_wind.append(file[slice(0, 4)])         # Adding the year
        speed_wind.append(int(file[slice(4, 6)]))    # Adding a month
        speed_wind.append(int(file[slice(6, 8)]))    # Adding a day
        speed_wind.append(int(file[slice(11, 13)]))  # Adding lead times
        speed_wind.append(correct_data_VGRD[i][1])   # Adding a level
    return speed_wind


def calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, speed_wind):
    for i in range(0, len(correct_data_VGRD)):
        for j in range(2, len(correct_data_VGRD[i])):
            speed_wind.append(((float(correct_data_UGRD[i][j]) ** 2) +
                               (float(correct_data_VGRD[i][j]) ** 2)) ** (1 / 2))
    return speed_wind


def calculates_the_day_based_on_the_lead_time(hours_in_a_day):
    hours_in_a_day = {1: 24, 2: 48, 3: 72, 4: 96}
    for i in (hours_in_a_day):
        print(i)
        if hours_in_a_day[i] <= int(speed_wind[reference_num][4]) < hours_in_a_day[i + 1]:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - hours_in_a_day[i]
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + i


def calculates_month_based_on_day():
    day_in_month = {1: 31, 2: (29 if (int(speed_wind[reference_num][1]) % 4 == 0) else 28), 3: 31, 4: 30, 5: 31,
                    6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for num_of_days in day_in_month.keys():
        if int(speed_wind[reference_num][2] == num_of_days) and speed_wind[reference_num][3] > day_in_month[
            num_of_days]:
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]
            speed_wind[reference_num][2] += 1


def calculation_of_the_year_based_on_month():  # Used when the month value overflows > 13
    if int(speed_wind[reference_num][2]) > 12:
        speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
        speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1

PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/part_of_directory_2016/"
my_file = open(
    '/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/part_of_directory_2016/data_out_for_Tolmachevo_point_01_2016',
    'w')
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

        correct_data_UGRD = getting_need_data('04')  # Horizontal wind direction
        correct_data_VGRD = getting_need_data('05')  # Vertical wind direction

        speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, adding_data_to_the_speed_list(correct_data_VGRD)))

        calculates_the_day_based_on_the_lead_time()
        calculates_month_based_on_day()
        calculation_of_the_year_based_on_month()

        reference_num += 1

# print(len(str(speed_wind[reference_num-1])))
# Sorting data in a list by year
# for i in range(0, len(speed_wind)):
#    sorted(str(speed_wind[i][1]))

# print(speed_wind[1])
# Sort date by month
# for i in range(0, len(speed_wind)):
#    if int(speed_wind[i][1]) != 2017:
#        sorted(str(speed_wind[i][2]))

# Sort date by day
# for i in range(0, len(speed_wind)):
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
