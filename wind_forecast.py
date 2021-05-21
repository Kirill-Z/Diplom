import pandas as pd
import os
import re

PATH = "/home/kirill/Downloads/Data/gfs/"


# Calculation of the point number based on the specified coordinates
def calculation_of_the_point_number():
    lat = float(input('Input latitude: ') or 55.03)
    lon = float(input('Input longitude: ') or 82.6)
    point_number_in_gfc = ((lat - 43.5) * 2) * ((lon - 49.5) * 2)
    point_number_in_gfc = int(point_number_in_gfc + (0.5 if point_number_in_gfc > 0 else -0.5))
    print(f"Point number  in gfc: {point_number_in_gfc}")
    return point_number_in_gfc

    # Calculation of the area of points by the specified coordinates


def calculation_of_the_area_of_points():
    low_lat = float(input('Enter the lower value latitude: ') or 54.5)
    low_lon = float(input('Enter the lower value longitude: ') or 82.1)
    top_lat = float(input('Enter the top value latitude: ') or 55.5)
    top_lon = float(input('Enter the top value longitude: ') or 83.1)
    low_point_number_in_gfc = ((low_lat - 43.5) * 2) * ((low_lon - 49.5) * 2)
    low_point_number_in_gfc = int(low_point_number_in_gfc + (0.5 if low_point_number_in_gfc > 0 else -0.5))
    top_point_number_in_gfc = ((top_lat - 43.5) * 2) * ((top_lon - 49.5) * 2)
    top_point_number_in_gfc = int(top_point_number_in_gfc + (0.5 if top_point_number_in_gfc > 0 else -0.5))
    print(f"Low point number  in gfc: {low_point_number_in_gfc}")
    print(f"Top point number  in gfc: {top_point_number_in_gfc}")
    return low_point_number_in_gfc, top_point_number_in_gfc


def adding_information(data_from_file, get_data, num_item):
    correct_data = [data_from_file[num_item][0], data_from_file[num_item][1]]
    speed_data = get_data
    if len(speed_data) > 2:
        for i in range(0, len(speed_data)):
            correct_data.append(speed_data[i])
    else:
        correct_data.append(speed_data)
    return correct_data


# Obtaining data on the direction of wind speed
def getting_need_data_for_point(point_to_calculate, data_from_file, num_item):
    correct_data = data_from_file[num_item][point_to_calculate]
    return correct_data


def getting_need_data_for_area(data_from_file, low_points_to_calculate, top_points_to_calculate, num_item):
    correct_data = []
    for j in range(low_points_to_calculate, top_points_to_calculate):
        correct_data.append(data_from_file[num_item][j])
    return correct_data


def adding_data_to_the_speed_list(file):
    # Adding file name, year, month, day, time
    wind_data = [file, file[slice(0, 4)], file[slice(4, 6)], int(file[slice(6, 8)]), int(file[slice(11, 13)])]
    return wind_data


def calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file):
    speed = adding_data_to_the_speed_list(file)
    for j in range(2, len(correct_data_VGRD)):
        speed.append(((float(correct_data_UGRD[j]) ** 2) +
                      (float(correct_data_VGRD[j]) ** 2)) ** (1 / 2))
    if len(speed) > 6:
        speed[5] = calculation_of_the_average_speed_in_the_range(speed)
    return speed


def calculation_of_the_average_speed_in_the_range(speed):
    num_of_points = 0
    for i in range(6, len(speed)):
        speed[5] += speed[i]
        num_of_points += 1
    speed[5] /= (num_of_points + 1)
    for i in range(len(speed) - 1, 5, -1):
        del speed[i]
    return speed[5]


def calculates_the_day_based_on_the_lead_time(speed_wind, reference_num):
    hours_in_a_day = {1: 24, 2: 48, 3: 72, 4: 96}
    for i in hours_in_a_day:
        if hours_in_a_day[i] <= int(speed_wind[reference_num][4]) < hours_in_a_day[i + 1]:
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - hours_in_a_day[i]
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + i


def calculates_month_based_on_day(speed_wind, reference_num):
    day_in_month = {1: 31, 2: (29 if (int(speed_wind[reference_num][1]) % 4 == 0) else 28), 3: 31, 4: 30, 5: 31,
                    6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for num_of_days in day_in_month.keys():
        if int(speed_wind[reference_num][2] == num_of_days) and \
                speed_wind[reference_num][3] > day_in_month[num_of_days]:
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]
            speed_wind[reference_num][2] += 1


def calculation_of_the_year_based_on_month(speed_wind, reference_num):  # Used when the month value overflows > 13
    if int(speed_wind[reference_num][2]) > 12:
        speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
        speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1


def calc_point(data_from_file, get_data, num_item):
    correct_data = adding_information(data_from_file, get_data, num_item)
    return correct_data


def calc_for_area(data_from_file, get_data, num_item):
    correct_data = adding_information(data_from_file, get_data, num_item)
    return correct_data


def write_data_to_a_file(speed, write_file, name_file):  # For convenient output in a file
    my_file = open(PATH + name_file, 'w')
    my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
    for i in range(0, len(speed)):
        for j in range(0, len(speed[i])):
            if len(str(speed[i][j])) == 1:
                write_file.write(str(speed[i][j]) + '  |   ')
            elif len(str(speed[i][j])) == 2:
                write_file.write(str(speed[i][j]) + ' |   ')
            else:
                write_file.write(str(speed[i][j]) + ' |   ')
        write_file.write('\n')

    write_file.close()
    return print('End of writing to file')


def write_in_file(path_to_dir, write_file, list_data):
    my_file = open(path_to_dir + write_file, 'w')
    for i in range(0, len(list_data)):
        for j in range(0, len(list_data[i])):
            if j == (len(list_data[i]) - 1):
                my_file.write(str(list_data[i][j]))
            else:
                my_file.write(str(list_data[i][j]) + ';')
        my_file.write('\n')
    my_file.close()
    return print('End of writing list in file')


def choice_speed_data_with_lead_time(speed_wind):
    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])
    return speed_wind_with_lead_time_on_this_day


def get_wind_speed_for_point(dirs, points_to_calculate, speed_wind, reference_num):
    for file in sorted(os.listdir(PATH + dirs)):
        if re.match('\d{10}_\d{2}', file):
            current_file = PATH + dirs + '/' + file
            file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
            data_from_file = file_reader.values.tolist()
            num_rows = 0
            for i in range(0, 70):
                data_from_file[i] = data_from_file[i][0].split()
                if (data_from_file[i][0] == "04" or "05") and data_from_file[i][1] == '21':
                    if data_from_file[i][0] == '04':
                        correct_data_UGRD = calc_point(data_from_file,
                                                       getting_need_data_for_point(points_to_calculate,
                                                                                   data_from_file,
                                                                                   num_rows),
                                                       num_rows)
                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = calc_point(data_from_file,
                                                       getting_need_data_for_point(points_to_calculate,
                                                                                   data_from_file,
                                                                                   num_rows),
                                                       num_rows)

                num_rows += 1

            speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

            calculates_the_day_based_on_the_lead_time(speed_wind, reference_num)
            calculates_month_based_on_day(speed_wind, reference_num)
            calculation_of_the_year_based_on_month(speed_wind, reference_num)
            reference_num += 1

    return speed_wind


def get_wind_speed_for_area(dirs, low_point_number, top_point_number, speed_wind, reference_num):
    for file in sorted(os.listdir(PATH + dirs)):
        if re.match('\d{10}_\d{2}', file):
            current_file = PATH + dirs + '/' + file
            file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
            data_from_file = file_reader.values.tolist()

            num_rows = 0
            for i in range(0, 70):
                data_from_file[i] = data_from_file[i][0].split()
                if (data_from_file[i][0] == "04" or "05") and data_from_file[i][1] == '21':
                    if data_from_file[i][0] == '04':
                        correct_data_UGRD = calc_for_area(data_from_file,
                                                          getting_need_data_for_area(data_from_file,
                                                                                     low_point_number,
                                                                                     top_point_number,
                                                                                     num_rows),
                                                          num_rows)

                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = calc_for_area(data_from_file,
                                                          getting_need_data_for_area(data_from_file,
                                                                                     low_point_number,
                                                                                     top_point_number,
                                                                                     num_rows),
                                                          num_rows)

                num_rows += 1
            speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

            calculates_the_day_based_on_the_lead_time(speed_wind, reference_num)
            calculates_month_based_on_day(speed_wind, reference_num)
            calculation_of_the_year_based_on_month(speed_wind, reference_num)
            reference_num += 1

    return speed_wind


def main(value):
    reference_num = 0
    speed_wind = []
    speed_wind_for_forecast_data = []
    if value == '1':
        points_to_calculate = calculation_of_the_point_number() + 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind = get_wind_speed_for_point(dirs, points_to_calculate, speed_wind, reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_for_forecast_data = get_wind_speed_for_point(dirs, points_to_calculate,
                                                                        speed_wind_for_forecast_data, reference_num)

        write_in_file(PATH, 'forecast_for_point_data', speed_wind)
        write_in_file(PATH, 'forecast_for_point_data_', speed_wind_for_forecast_data)

    elif value == '2':
        low_point_number, top_point_number = calculation_of_the_area_of_points()
        low_point_number += 1
        top_point_number += 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind = get_wind_speed_for_area(dirs, low_point_number, top_point_number, speed_wind,
                                                     reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_for_forecast_data = get_wind_speed_for_area(dirs, low_point_number, top_point_number,
                                                                       speed_wind_for_forecast_data, reference_num)

        write_in_file(PATH, 'forecast_for_area_data', speed_wind)
        write_in_file(PATH, 'forecast_for_area_data_', speed_wind_for_forecast_data)

    return speed_wind, speed_wind_for_forecast_data
