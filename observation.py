import os
import re
import pandas as pd
import forecast

PATH = "/home/kirill/Downloads/Data/АВ6/"  # Path to files with observation data


def add_data_to_the_speed_list(file, data, i):
    """Adding file name, year, month, day, time."""
    speed_wind = [file[2:], file[2:6], file[6:8], file[8:10], data[i][0], data[i][2]]
    return speed_wind


def get_data_hour_by_hour(file, data_from_file, speed_wind):
    for i in range(0, len(data_from_file)):
        hour1 = data_from_file[i][0][0]
        hour2 = data_from_file[i][0][1]
        hour = hour1 + hour2
        minute1 = data_from_file[i][0][3]
        minute2 = data_from_file[i][0][4]
        minute = minute1 + minute2
        if int(hour) % 3 == 0 and int(minute) == 0:
            speed_wind.append(add_data_to_the_speed_list(file, data_from_file, i))
    return speed_wind


def get_data_in_time_range(file, data_from_file, speed_wind, num_record):
    hour_time = 0
    data_for_next_time = 0
    speed_for_next_time = 0
    for i in range(0, len(data_from_file)):
        hour = data_from_file[i][0][0] + data_from_file[i][0][1]
        minute = data_from_file[i][0][3] + data_from_file[i][0][4]
        if int(minute) % 30 == 0 and int(hour) <= 21:
            if int(hour) % 3 == 0 and int(minute) == 0:
                num_record += 1
                speed_wind.append(add_data_to_the_speed_list(file, data_from_file, i))
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
    return speed_wind


def get_data_for_a_range_with_every_minute(file, data_from_file, speed_wind, num_record):
    hour_time = 0
    data_for_next_time = 0
    speed_for_next_time = 0
    data_area = []
    speed_area = []
    for i in range(0, len(data_from_file)):

        hour = data_from_file[i][0][0] + data_from_file[i][0][1]
        minute = data_from_file[i][0][3] + data_from_file[i][0][4]
        if int(hour) <= 21:
            if (int(hour) % 3 == 0) and (int(minute) == 0):
                num_record += 1
                speed_wind.append(add_data_to_the_speed_list(file, data_from_file, i))
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
                for k in range(5, len(speed_wind[num_record - 1])):
                    speed_wind[num_record - 1][5] += speed_wind[num_record - 1][k]
                speed_wind[num_record - 1][5] = speed_wind[num_record - 1][5] / (
                        len(speed_wind[num_record - 1]) - 4)
                for k in range((len(speed_wind[num_record - 1]) - 1), 5, -1):
                    del speed_wind[num_record - 1][k]
    return speed_wind


def main(value: str):
    speed_wind_training = []
    speed_wind_test = []
    num_record = 0
    if value == '1':
        for dirs1 in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_training = get_data_hour_by_hour(file, data_from_file, speed_wind_training)

            if re.match('2018', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_test = get_data_hour_by_hour(file, data_from_file, speed_wind_test)
        print(speed_wind_training)
        forecast.write_in_file(PATH, 'observation_data_training_hour_by_hour', speed_wind_training)
        forecast.write_in_file(PATH, 'observation_data_test_hour_by_hour', speed_wind_test)

    if value == '2':
        for dirs1 in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_training = get_data_in_time_range(file, data_from_file, speed_wind_training,
                                                                         num_record)

            if re.match('2018', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_test = get_data_in_time_range(file, data_from_file, speed_wind_test, num_record)

        forecast.write_in_file(PATH, 'observation_data_training_time_range', speed_wind_training)
        forecast.write_in_file(PATH, 'observation_data_test_time_range', speed_wind_test)

    if value == '3':
        for dirs1 in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_training = get_data_for_a_range_with_every_minute(file, data_from_file,
                                                                                         speed_wind_training,
                                                                                         num_record)

            if re.match('2018', dirs1):
                for dirs2 in sorted(os.listdir(PATH + dirs1)):
                    for file in sorted(os.listdir(PATH + dirs1 + '/' + dirs2)):
                        if re.match('av*', file):
                            current_file = PATH + dirs1 + '/' + dirs2 + '/' + file
                            file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
                            data_from_file = file_reader.values.tolist()
                            speed_wind_test = get_data_for_a_range_with_every_minute(file, data_from_file,
                                                                                      speed_wind_test, num_record)
        forecast.write_in_file(PATH, 'observation_data_training_time_range_with_every_minute', speed_wind_training)
        forecast.write_in_file(PATH, 'observation_data_test_time_range_with_every_minute', speed_wind_test)

    return speed_wind_training, speed_wind_test
