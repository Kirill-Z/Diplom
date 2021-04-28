import pandas as pd
import os
import re
import plotting

PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/АВ6_Толмачево/2016/"


def add_data_to_the_speed_list(data, i):
    speed_wind = []
    speed_wind.append(file[2:])
    speed_wind.append(file[2:6])
    speed_wind.append(file[6:8])
    speed_wind.append(file[8:10])
    speed_wind.append(data[i][0])
    speed_wind.append(data[i][2])
    return speed_wind


def write_data_to_a_file(speed_wind, my_file):
    for i in range(0, len(speed_wind)):
        for j in range(0, len(speed_wind[i])):
            if len(str(speed_wind[i][j])) == 1:
                my_file.write(str(speed_wind[i][j]) + '  |  ')
            elif len(str(speed_wind[i][j])) == 3:
                my_file.write(str(speed_wind[i][j]) + '|   ')
            else:
                my_file.write(str(speed_wind[i][j]) + ' |  ')
        my_file.write('\n')

    my_file.close()
    return print('The end write in file')


def main():
    #my_file = open(PATH + 'data_practical_wind_01_2016.csv', 'w')
    #my_file.write('File name    |  Year |Month| Day |  Time  |Speed|\n')
    speed_wind = []

    for dirs in sorted(os.listdir(PATH)):
        for file in sorted(os.listdir(PATH + dirs)):
            if re.match('av*', file):
                currentFile = PATH + dirs + '/' + file
                file_reader = pd.read_csv(currentFile, sep=';', header=None, engine='python')
                data_from_file = file_reader.values.tolist()

                for i in range(0, len(data_from_file)):
                    hour1 = data_from_file[i][0][0]
                    hour2 = data_from_file[i][0][1]
                    hour = hour1 + hour2

                    minute1 = data_from_file[i][0][3]
                    minute2 = data_from_file[i][0][4]
                    minute = minute1 + minute2

                    if int(hour) % 3 == 0 and int(minute) == 0:
                        speed_wind.append(add_data_to_the_speed_list(data_from_file, i))

    # write_data_to_a_file(speed_wind, my_file)

    return speed_wind


def main_area():
    #my_file = open(PATH + 'data_practical_wind_01_2016_area.csv', 'w')
    #y_file.write('File name    |  Year |Month| Day |  Time  |Speed|\n')
    speed_wind = []
    num_record = 0

    for dirs in sorted(os.listdir(PATH)):
        for file in sorted(os.listdir(PATH + dirs)):
            if re.match('av*', file):
                data_for_next_time = 0
                speed_for_next_time = 0
                currentFile = PATH + dirs + '/' + file
                file_reader = pd.read_csv(currentFile, sep=';', header=None, engine='python')
                data_from_file = file_reader.values.tolist()
                hour_time = 0
                for i in range(0, len(data_from_file)):

                    hour = data_from_file[i][0][0] + data_from_file[i][0][1]
                    minute = data_from_file[i][0][3] + data_from_file[i][0][4]
                    if int(minute) % 30 == 0 and int(hour) <= 21:
                        if int(hour) % 3 == 0 and int(minute) == 0:
                            num_record += 1
                            speed_wind.append(add_data_to_the_speed_list(data_from_file, i))
                            if data_for_next_time != 0:
                                speed_wind[num_record - 1].append(speed_for_next_time)
                            hour_time = hour
                        elif int(hour) % 3 == 0 and int(minute) == 30:
                            speed_wind[num_record - 1].append(data_from_file[i][2])
                            if len(speed_wind[num_record - 1]) > 7:
                                speed_wind[num_record - 1][5] = ((speed_wind[num_record - 1][5] +
                                                                  speed_wind[num_record - 1][6] +
                                                                  speed_wind[num_record - 1][7]) / 3)
                                del speed_wind[num_record - 1][7]
                                del speed_wind[num_record - 1][6]
                            else:
                                speed_wind[num_record - 1][5] = (
                                        (speed_wind[num_record - 1][5] + speed_wind[num_record - 1][6]) / 2)
                                del speed_wind[num_record - 1][6]
                        elif int(hour) == (int(hour_time) + 2) and int(minute) == 30:
                            data_for_next_time = data_from_file[i][0]
                            speed_for_next_time = data_from_file[i][2]

    # write_data_to_a_file(speed_wind, my_file)

    return speed_wind


def main_area_with_every_minute():
    #my_file = open(PATH + 'data_practical_wind_01_2016_every_minute_area.csv', 'w')
    #my_file.write('File name    |  Year |Month| Day |  Time  |Speed|\n')
    speed_wind = []
    num_record = 0

    for dirs in sorted(os.listdir(PATH)):
        for file in sorted(os.listdir(PATH + dirs)):
            if re.match('av*', file):
                data_for_next_time = 0
                speed_for_next_time = 0
                data_area = []
                speed_area = []
                currentFile = PATH + dirs + '/' + file
                file_reader = pd.read_csv(currentFile, sep=';', header=None, engine='python')
                data_from_file = file_reader.values.tolist()
                hour_time = 0

                for i in range(0, len(data_from_file)):

                    hour = data_from_file[i][0][0] + data_from_file[i][0][1]
                    minute = data_from_file[i][0][3] + data_from_file[i][0][4]

                    if int(hour) <= 21:
                        if (int(hour) % 3 == 0) and (int(minute) == 0):
                            num_record += 1
                            speed_wind.append(add_data_to_the_speed_list(data_from_file, i))
                            hour_time = hour

                            if data_for_next_time != 0:
                                speed_wind[num_record - 1].append(speed_for_next_time)

                            if len(data_area) != 0:
                                for j in range(0, len(data_area)):
                                    speed_wind[num_record - 1].append(speed_area[j])
                                data_area = []
                                speed_area = []

                        elif (int(hour) % 3 == 0) and (0 < int(minute) < 30):
                            speed_wind[num_record - 1].append(data_from_file[i][2])



                        elif int(hour) == (int(hour_time) + 2) and int(minute) == 30:
                            speed_for_next_time = data_from_file[i][2]

                        elif int(hour) == (int(hour_time) + 2) and (30 <= int(minute) <= 59):
                            speed_area.append(data_from_file[i][2])


                        elif int(hour) % 3 == 0 and int(minute) == 30:
                            speed_wind[num_record - 1].append(data_from_file[i][2])

                            if len(speed_wind[num_record - 1]) > len(speed_wind[0]):
                                for k in range(5, len(speed_wind[num_record - 1])):
                                    speed_wind[num_record - 1][5] += speed_wind[num_record - 1][k]
                                speed_wind[num_record - 1][5] = speed_wind[num_record - 1][5] / (
                                        len(speed_wind[num_record - 1]) - 4)
                                for k in range((len(speed_wind[num_record - 1]) - 1), 5, -1):
                                    del speed_wind[num_record - 1][k]
                            else:
                                for k in range(5, len(speed_wind[num_record - 1])):
                                    speed_wind[num_record - 1][5] += speed_wind[num_record - 1][k]
                                speed_wind[num_record - 1][5] = speed_wind[num_record - 1][5] / (
                                        len(speed_wind[num_record - 1]) - 4)
                                for k in range((len(speed_wind[num_record - 1]) - 1), 5, -1):
                                    del speed_wind[num_record - 1][k]

    return speed_wind
