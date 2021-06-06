import os
import re
import pandas as pd

PATH = "/home/kirill/Downloads/Data/gfs/"  # Path to files with forecast data


def calc_point_number():
    """Calculation of the point number based on the specified coordinates."""
    lat = float(input('Input latitude: ') or 55.03)
    lon = float(input('Input longitude: ') or 82.6)
    point_number_in_gfc = ((lat - 43.5) * 2) * ((lon - 49.5) * 2)
    point_number_in_gfc = int(point_number_in_gfc + (0.5 if point_number_in_gfc > 0 else -0.5))
    print(f"Point number  in gfs: {point_number_in_gfc}")
    return point_number_in_gfc


def calc_area_of_points():
    """Calculation of the area of points by the specified coordinates."""
    low_lat = float(input('Enter the lower value latitude: ') or 54.8)
    low_lon = float(input('Enter the lower value longitude: ') or 82.1)
    top_lat = float(input('Enter the top value latitude: ') or 55.8)
    top_lon = float(input('Enter the top value longitude: ') or 83.1)
    low_point_number_in_gfc = ((low_lat - 43.5) * 2) * ((low_lon - 49.5) * 2)
    low_point_number_in_gfc = int(low_point_number_in_gfc + (0.5 if low_point_number_in_gfc > 0 else -0.5))
    top_point_number_in_gfc = ((top_lat - 43.5) * 2) * ((top_lon - 49.5) * 2)
    top_point_number_in_gfc = int(top_point_number_in_gfc + (0.5 if top_point_number_in_gfc > 0 else -0.5))
    print(f"Low point number  in gfs: {low_point_number_in_gfc}")
    print(f"Top point number  in gfs: {top_point_number_in_gfc}")
    return low_point_number_in_gfc, top_point_number_in_gfc


def calc_five_points():
    """The required point is taken and 4 points around."""
    lat = float(input('Input latitude: ') or 55.03)
    lon = float(input('Input longitude: ') or 82.6)
    need_point = ((lat - 43.5) * 2) * ((lon - 49.5) * 2)
    need_point = int(need_point + (0.5 if need_point > 0 else -0.5))
    first_lat = lat - 0.5
    first_lon = lon - 0.5
    first_point = ((first_lat - 43.5) * 2) * ((first_lon - 49.5) * 2)
    first_point = int(first_point + (0.5 if first_point > 0 else -0.5))
    second_lat = lat - 0.5
    second_lon = lon
    second_point = ((second_lat - 43.5) * 2) * ((second_lon - 49.5) * 2)
    second_point = int(second_point + (0.5 if second_point > 0 else -0.5))
    third_lat = lat + 0.5
    third_lon = lon - 0.5
    third_point = ((third_lat - 43.5) * 2) * ((third_lon - 49.5) * 2)
    third_point = int(third_point + (0.5 if third_point > 0 else -0.5))
    fourth_lat = lat + 0.5
    fourth_lon = lon + 0.5
    fourth_point = ((fourth_lat - 43.5) * 2) * ((fourth_lon - 49.5) * 2)
    fourth_point = int(fourth_point + (0.5 if fourth_point > 0 else -0.5))
    print(f'First point number in gfs: {first_point}')
    print(f'Second point number in gfs: {second_point}')
    print(f'Third point number in gfs: {third_point}')
    print(f'Fourth point number in gfs: {fourth_point}')
    print(f'Need point number in gfs: {need_point}')

    return first_point, second_point, third_point, fourth_point, need_point


def add_information(data_from_file, get_data, num_item):
    correct_data = [data_from_file[num_item][0], data_from_file[num_item][1]]
    speed_data = get_data
    if len(speed_data) > 2:  # Executed if an area of points is present
        for i in range(0, len(speed_data)):
            correct_data.append(speed_data[i])
    else:  # Executed if point is present
        correct_data.append(speed_data)
    return correct_data


def get_need_data_for_point(point_to_calculate, data_from_file, num_item):
    """Obtaining data on the direction of wind speed for point."""
    correct_data = data_from_file[num_item][point_to_calculate]
    return correct_data


def get_need_data_for_area(data_from_file, low_points_to_calculate, top_points_to_calculate, num_item):
    """Obtaining wind speed direction data for a point area."""
    correct_data = []
    for j in range(low_points_to_calculate, top_points_to_calculate):
        correct_data.append(data_from_file[num_item][j])
    return correct_data


def get_need_data_for_five_point(data_from_file,  first_point, second_point, third_point, fourth_point, need_point,
                                 num_item):
    correct_data = [data_from_file[num_item][first_point], data_from_file[num_item][second_point],
                    data_from_file[num_item][third_point], data_from_file[num_item][fourth_point],
                    data_from_file[num_item][need_point]]
    return correct_data


def add_data_to_the_speed_list(file):
    """Adding file name, year, month, day, time."""
    wind_data = [file, file[slice(0, 4)], file[slice(4, 6)], int(file[slice(6, 8)]), int(file[slice(11, 13)])]
    return wind_data


def calc_wind_speed(correct_data_VGRD, correct_data_UGRD, file):
    speed = add_data_to_the_speed_list(file)
    for j in range(2, len(correct_data_VGRD)):
        speed.append(((float(correct_data_UGRD[j]) ** 2) +
                      (float(correct_data_VGRD[j]) ** 2)) ** (1 / 2))
    if len(speed) > 6:
        speed[5] = calc_average_speed_in_the_range(speed)
    return speed


def calc_average_speed_in_the_range(speed):
    num_of_points = 0
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
            speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - hours_in_a_day[i]
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + i

    return speed_wind


def calc_month_based_on_day(speed_wind, reference_num):
    """Used when the number of days in a month exceeds the allowable."""
    day_in_month = {1: 31, 2: (29 if (int(speed_wind[reference_num][1]) % 4 == 0) else 28), 3: 31, 4: 30, 5: 31,
                    6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for num_of_days in day_in_month.keys():
        if (int(speed_wind[reference_num][2]) == num_of_days) and \
                (speed_wind[reference_num][3] > day_in_month[num_of_days]):
            speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]
            speed_wind[reference_num][2] = int(speed_wind[reference_num][2]) + 1
    return speed_wind


def calc_year_based_on_month(speed_wind, reference_num):
    """Used when the month value overflows > 13."""
    if int(speed_wind[reference_num][2]) > 12:
        speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
        speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1
    return speed_wind


def calc_point(data_from_file, get_data, num_item):
    correct_data = add_information(data_from_file, get_data, num_item)
    return correct_data


def calc_for_area(data_from_file, get_data, num_item):
    correct_data = add_information(data_from_file, get_data, num_item)
    return correct_data


def write_in_file(path_to_dir, write_file, list_data):
    """Writing the required data to a separate file.

    We will use the recording of the necessary data, in this case, the name of the file
    from which the values were taken, year, month, day, lead time, hour of calculation
    and wind speed in a separate file, since the files with predicted data contain a large
    amount of information and, if necessary, make calculations for these points, it will be
    much faster to retrieve data from a file that contains only the necessary information

    """
    my_file = open(path_to_dir + write_file, 'w')
    print(list_data)
    for i in range(0, len(list_data)):
        for j in range(0, len(list_data[i])):
            if j == (len(list_data[i]) - 1):
                my_file.write(str(list_data[i][j]))
            else:
                my_file.write(str(list_data[i][j]) + ';')
        my_file.write('\n')
    my_file.close()
    return print('End of writing list in file')


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
                                                       get_need_data_for_point(points_to_calculate,
                                                                                   data_from_file,
                                                                                   num_rows),
                                                       num_rows)
                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = calc_point(data_from_file,
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
                                                          get_need_data_for_area(data_from_file,
                                                                                     low_point_number,
                                                                                     top_point_number,
                                                                                     num_rows),
                                                          num_rows)

                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = calc_for_area(data_from_file,
                                                          get_need_data_for_area(data_from_file,
                                                                                     low_point_number,
                                                                                     top_point_number,
                                                                                     num_rows),
                                                          num_rows)

                num_rows += 1
            speed_wind.append(calc_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

            speed_wind = calc_day_based_on_lead_time(speed_wind, reference_num)
            speed_wind = calc_month_based_on_day(speed_wind, reference_num)
            speed_wind = calc_year_based_on_month(speed_wind, reference_num)
            reference_num += 1

    return speed_wind


def get_wind_speed_for_five_point(dirs, first_point, second_point, third_point, fourth_point, need_point,
                                  speed_wind, reference_num):
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
                                                       get_need_data_for_five_point(data_from_file, first_point,
                                                                                    second_point, third_point,
                                                                                    fourth_point, need_point, num_rows),
                                                       num_rows)
                    if data_from_file[i][0] == '05':
                        correct_data_VGRD = calc_point(data_from_file,
                                                       get_need_data_for_five_point(data_from_file, first_point,
                                                                                    second_point, third_point,
                                                                                    fourth_point, need_point, num_rows),
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
    if value == '1':
        points_to_calculate = calc_point_number() + 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind_training = get_wind_speed_for_point(dirs, points_to_calculate, speed_wind_training,
                                                               reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_test = get_wind_speed_for_point(dirs, points_to_calculate, speed_wind_test, reference_num)

        write_in_file(PATH, 'forecast_for_point_data', speed_wind_training)
        write_in_file(PATH, 'forecast_for_point_data_', speed_wind_test)

    elif value == '2':
        low_point_number, top_point_number = calc_area_of_points()
        low_point_number += 1
        top_point_number += 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind_training = get_wind_speed_for_area(dirs, low_point_number, top_point_number,
                                                              speed_wind_training, reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_test = get_wind_speed_for_area(dirs, low_point_number, top_point_number,
                                                          speed_wind_test, reference_num)

        write_in_file(PATH, 'forecast_for_area_data', speed_wind_training)
        write_in_file(PATH, 'forecast_for_area_data_', speed_wind_test)

    elif value == '3':
        first_point, second_point, third_point, fourth_point, need_point = calc_five_points()
        first_point += 1
        second_point += 1
        third_point += 1
        fourth_point += 1
        need_point += 1
        for dirs in sorted(os.listdir(PATH)):
            if re.match('201[6,7]', dirs):
                speed_wind_training, reference_num = get_wind_speed_for_five_point(dirs, first_point, second_point, third_point,
                                                                    fourth_point, need_point, speed_wind_training,
                                                                    reference_num)
            elif re.match('2018', dirs):
                reference_num = 0
                speed_wind_test, reference_num = get_wind_speed_for_five_point(dirs, first_point, second_point, third_point,
                                                                fourth_point, need_point, speed_wind_test,
                                                                reference_num)
        write_in_file(PATH, 'forecast_for_five_point_data', speed_wind_training)
        write_in_file(PATH, 'forecast_for_five_point_data_', speed_wind_test)
    return speed_wind_training, speed_wind_test
