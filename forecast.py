import os
import re
import pandas as pd
from tqdm import tqdm
import write_in_file as write

PATH = "/home/kirill/Downloads/Data/gfs/"  # Path to files with forecast data


def calc_point_number(lat, lon):
    """Calculation of the point number based on the specified coordinates."""
    lat_point = ((lat - 44) / 0.5 + 1)
    lon_point = ((lon - 50) / 0.5 + 1)
    lat_point = int(lat_point + (0.5 if lat_point > 0 else -0.5))
    lon_point = int(lon_point + (0.5 if lon_point > 0 else -0.5))
    point_number_in_gfc = 141 * (lat_point - 1) + lon_point
    return point_number_in_gfc


def calc_five_points(lat, lon):
    """The required point is taken and 4 points around."""
    need_point = calc_point_number(lat, lon)
    first_point = calc_point_number(lat - 0.5, lon - 0.5)
    second_point = calc_point_number(lat - 0.5, lon)
    third_point = calc_point_number(lat + 0.5, lon - 0.5)
    fourth_point = calc_point_number(lat + 0.5, lon + 0.5)
    print(f'First point number in gfs: {first_point}')
    print(f'Second point number in gfs: {second_point}')
    print(f'Third point number in gfs: {third_point}')
    print(f'Fourth point number in gfs: {fourth_point}')
    print(f'Need point number in gfs: {need_point}')

    return first_point, second_point, third_point, fourth_point, need_point


def add_information(data_from_file, get_data, num_item):
    # [0] - parameter number (04 or 05), [1] - height level
    correct_data = [data_from_file[num_item][0], data_from_file[num_item][1]]
    speed_data = get_data
    if type(speed_data) == list and len(speed_data) > 2:  # Executed if multiple points are present
        for i in range(0, len(speed_data)):
            correct_data.append(speed_data[i])  # [i] - wind speed
    else:  # Executed if point is present
        correct_data.append(speed_data)
    return correct_data


def get_need_data_for_point(point_to_calculate, data_from_file, num_item):
    """Obtaining data on the direction of wind speed for point."""
    speed_wind = data_from_file[num_item][point_to_calculate]
    return speed_wind


def get_need_data_for_five_point(data_from_file, first_point, second_point, third_point, fourth_point, need_point,
                                 num_item):
    """Obtaining data on the direction of wind speed for 5 points."""
    speed_wind = [data_from_file[num_item][first_point], data_from_file[num_item][second_point],
                  data_from_file[num_item][third_point], data_from_file[num_item][fourth_point],
                  data_from_file[num_item][need_point]]
    return speed_wind


def add_data_to_the_speed_list(file):
    """Adding 1.file name, 2.year, 3.month, 4.day, 5.time."""
    wind_data = [file, file[slice(0, 4)], file[slice(4, 6)], int(file[slice(6, 8)]), int(file[slice(11, 13)])]
    return wind_data


def calc_wind_speed(correct_data_VGRD, correct_data_UGRD, file):
    """Calculation of wind speed from vertical(VGRD) and horizontal(UGRD) wind components."""
    speed = add_data_to_the_speed_list(file)
    for j in range(2, len(correct_data_VGRD)):
        speed.append(((float(correct_data_UGRD[j]) ** 2) +
                      (float(correct_data_VGRD[j]) ** 2)) ** (1 / 2))
    if len(speed) > 6:
        speed[5] = calc_average_speed_in_the_range(speed)
    return speed


def calc_average_speed_in_the_range(speed):
    num_of_points = 0
    # Starts with 6, since this is preceded by information about the file name, date and time
    for i in range(6, len(speed)):
        speed[5] += speed[i]
        num_of_points += 1
    speed[5] /= (num_of_points + 1)
    for i in range(len(speed) - 1, 5, -1):
        del speed[i]
    return speed[5]


def calc_day_based_on_lead_time(speed_wind, reference_num):
    """Used when the lead time exceeds a day."""
    hours_in_a_day = {1: 24, 2: 48, 3: 72, 4: 96}
    for i in hours_in_a_day:
        if hours_in_a_day[i] <= int(speed_wind[reference_num][4]) < hours_in_a_day[i + 1]:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - hours_in_a_day[i]  # [4] - hour
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + i  # [3] - day

    return speed_wind


def calc_month_based_on_day(speed_wind, reference_num):
    """Used when the number of days in a month exceeds the allowable."""
    day_in_month = {1: 31, 2: (29 if (int(speed_wind[reference_num][1]) % 4 == 0) else 28), 3: 31, 4: 30, 5: 31,
                    6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for num_of_days in day_in_month.keys():
        if (int(speed_wind[reference_num][2]) == num_of_days) and \
                (speed_wind[reference_num][3] > day_in_month[num_of_days]):
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]  # [3] - day
            speed_wind[reference_num][2] = int(speed_wind[reference_num][2]) + 1  # [2] - month
    return speed_wind


def calc_year_based_on_month(speed_wind, reference_num):
    """Used when the month value overflows > 13."""
    if int(speed_wind[reference_num][2]) > 12:
        speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12  # [2] - month
        speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1  # [1] - year
    return speed_wind


def get_wind_speed_for_point(dirs, points_to_calculate, speed_wind, reference_num):
    print(10 * ' ' + f'Directory {dirs} being processed')
    for file, progress_bar in zip(sorted(os.listdir(PATH + dirs)), tqdm(sorted(os.listdir(PATH + dirs)))):
        if re.match('\d{10}_\d{2}', file):
            current_file = PATH + dirs + '/' + file
            file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
            data_from_file = file_reader.values.tolist()
            num_rows = 0
            for i in range(0, 70):
                data_from_file[i] = data_from_file[i][0].split()
                if ((data_from_file[i][0] == "04") or (data_from_file[i][0] == "05")) and data_from_file[i][1] == '21':
                    if data_from_file[i][0] == '04':
                        correct_data_UGRD = add_information(data_from_file,
                                                            get_need_data_for_point(points_to_calculate,
                                                                                    data_from_file,
                                                                                    num_rows),
                                                            num_rows)
                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = add_information(data_from_file,
                                                            get_need_data_for_point(points_to_calculate,
                                                                                    data_from_file,
                                                                                    num_rows),
                                                            num_rows)

                num_rows += 1
            speed_wind.append(calc_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

            speed_wind = calc_day_based_on_lead_time(speed_wind, reference_num)
            speed_wind = calc_month_based_on_day(speed_wind, reference_num)
            speed_wind = calc_year_based_on_month(speed_wind, reference_num)
            reference_num += 1

    return speed_wind, reference_num


def get_wind_speed_for_five_point(dirs, first_point, second_point, third_point, fourth_point, need_point,
                                  speed_wind, reference_num):
    print(10*' ' + f'Directory {dirs} being processed')
    for file, progress_bar in zip(sorted(os.listdir(PATH + dirs)), tqdm(sorted(os.listdir(PATH + dirs)))):
        if re.match('\d{10}_\d{2}', file):

            current_file = PATH + dirs + '/' + file
            file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
            data_from_file = file_reader.values.tolist()
            num_rows = 0
            for i in range(0, 70):
                data_from_file[i] = data_from_file[i][0].split()
                if (data_from_file[i][0] == "04" or "05") and data_from_file[i][1] == '21':
                    if data_from_file[i][0] == '04':
                        correct_data_UGRD = add_information(data_from_file,
                                                            get_need_data_for_five_point(data_from_file, first_point,
                                                                                         second_point, third_point,
                                                                                         fourth_point, need_point,
                                                                                         num_rows),
                                                            num_rows)
                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = add_information(data_from_file,
                                                            get_need_data_for_five_point(data_from_file, first_point,
                                                                                         second_point, third_point,
                                                                                         fourth_point, need_point,
                                                                                         num_rows),
                                                            num_rows)

                num_rows += 1
            speed_wind.append(calc_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

            speed_wind = calc_day_based_on_lead_time(speed_wind, reference_num)
            speed_wind = calc_month_based_on_day(speed_wind, reference_num)
            speed_wind = calc_year_based_on_month(speed_wind, reference_num)
            reference_num += 1
    return speed_wind, reference_num


def main(value):
    reference_num = 0
    speed_wind_training = []
    speed_wind_test = []
    lat = float(input('Input latitude: ') or 55.03)  # 55.03 - lat Tolmachevo
    lon = float(input('Input longitude: ') or 82.6)  # 82.6 - lon Tolmachevo
    if value == '1':
        points_to_calculate = calc_point_number(lat, lon) + 1
        print(f"Point number  in gfs: {points_to_calculate - 1}")
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind_training, reference_num = get_wind_speed_for_point(dirs, points_to_calculate,
                                                                              speed_wind_training,
                                                                              reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_test, reference_num = get_wind_speed_for_point(dirs, points_to_calculate, speed_wind_test,
                                                                          reference_num)

        write.write_in_file(PATH, 'forecast_for_point_data_training', speed_wind_training)
        write.write_in_file(PATH, 'forecast_for_point_data_test', speed_wind_test)

    elif value == '2':
        first_point, second_point, third_point, fourth_point, need_point = calc_five_points(lat, lon)
        first_point += 1
        second_point += 1
        third_point += 1
        fourth_point += 1
        need_point += 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind_training, reference_num = get_wind_speed_for_five_point(dirs, first_point, second_point,
                                                                                   third_point,
                                                                                   fourth_point, need_point,
                                                                                   speed_wind_training,
                                                                                   reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_test, reference_num = get_wind_speed_for_five_point(dirs, first_point, second_point,
                                                                               third_point,
                                                                               fourth_point, need_point,
                                                                               speed_wind_test,
                                                                               reference_num)
        write.write_in_file(PATH, 'forecast_for_five_point_data_training', speed_wind_training)
        write.write_in_file(PATH, 'forecast_for_five_point_data_test', speed_wind_test)
    return speed_wind_training, speed_wind_test
