import pandas as pd
import os
import re

PATH = "/home/kirill/Downloads/Data/gfs/2016/"


# Calculation of the point number based on the specified coordinates
def calculation_of_the_point_number():
    lat = float(input('Input latitude: ') or 55.03)
    lon = float(input('Input longitude: ') or 82.6)
    point_number_in_gfc = ((lat - 43.5) * 2) * ((lon - 49.5) * 2)
    point_number_in_gfc = int(point_number_in_gfc + (0.5 if point_number_in_gfc > 0 else -0.5))
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
    for j in range(0, len(data_from_file[num_item])):
        if j == point_to_calculate:
            correct_data = data_from_file[num_item][j]
    return correct_data


def getting_need_data_for_area(data_from_file, low_points_to_calculate, top_points_to_calculate, num_item):
    correct_data = []
    for j in range(0, len(data_from_file[num_item])):
        if low_points_to_calculate < j < top_points_to_calculate:
            correct_data.append(data_from_file[num_item][j])
    return correct_data


def adding_data_to_the_speed_list(file):
    # Adding file name, year, month, day, time
    wind_data = [file, file[slice(0, 4)], int(file[slice(4, 6)]), int(file[slice(6, 8)]), int(file[slice(11, 13)])]
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


def write_data_to_a_file(speed, write_file, name_file):
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


def write_list_in_file(write_file, list_data):
    my_file = open(PATH + write_file, 'w')
    print(list_data)
    for i in range(0, len(list_data)):
        for j in range(0, len(list_data[i])):
            for k in range(0, len(list_data[i][j])):
                if k == (len(list_data[i][j]) - 1):
                    my_file.write(str(list_data[i][j][k]))
                else:
                    my_file.write(str(list_data[i][j][k]) + ';')
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


def main(value):
    reference_num = 0
    speed_wind = []

    if value == '1':
        points_to_calculate = calculation_of_the_point_number() + 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_([0,1][0-9]|21)', file):
                current_file = PATH + file
                file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
                data_from_file = file_reader.values.tolist()
                num_rows = 0
                for i in range(0, 70):
                    data_from_file[i] = data_from_file[i][0].split()
                    if (data_from_file[i][0] == "04" or "05") and data_from_file[i][1] == '21':
                        if data_from_file[i][0] == '04':
                            correct_data_UGRD = calc_point(data_from_file,
                                                           getting_need_data_for_point(points_to_calculate,
                                                                                       data_from_file, num_rows),
                                                           num_rows)
                        if data_from_file[i][0] == '05':
                            correct_data_VGRD = calc_point(data_from_file,
                                                           getting_need_data_for_point(points_to_calculate,
                                                                                       data_from_file, num_rows),
                                                           num_rows)

                    num_rows += 1

                speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

                calculates_the_day_based_on_the_lead_time(speed_wind, reference_num)
                calculates_month_based_on_day(speed_wind, reference_num)
                calculation_of_the_year_based_on_month(speed_wind, reference_num)
                reference_num += 1
    elif value == '2':
        low_point_number, top_point_number = calculation_of_the_area_of_points()
        low_point_number += 1
        top_point_number += 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_([0,1][0-9]|21)', file):
                current_file = PATH + file
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
                                                                                         top_point_number, num_rows),
                                                              num_rows)

                        if data_from_file[i][0] == '05':
                            correct_data_VGRD = calc_for_area(data_from_file,
                                                              getting_need_data_for_area(data_from_file,
                                                                                         low_point_number,
                                                                                         top_point_number, num_rows),
                                                              num_rows)

                    num_rows += 1
                speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file))

                calculates_the_day_based_on_the_lead_time(speed_wind, reference_num)
                calculates_month_based_on_day(speed_wind, reference_num)
                calculation_of_the_year_based_on_month(speed_wind, reference_num)
                reference_num += 1

    return choice_speed_data_with_lead_time(speed_wind)


def main_for_difference_lead_time(value):
    reference_num = 0
    speed_wind = []
    lead_time_0_hours = []
    lead_time_3_hours = []
    lead_time_6_hours = []
    lead_time_9_hours = []
    lead_time_12_hours = []
    lead_time_15_hours = []
    lead_time_18_hours = []
    lead_time_21_hours = []
    lead_time_24_hours = []
    lead_time_27_hours = []
    lead_time_30_hours = []
    lead_time_33_hours = []
    lead_time_36_hours = []
    lead_time_39_hours = []
    lead_time_42_hours = []
    lead_time_45_hours = []
    lead_time_48_hours = []
    lead_time_51_hours = []
    lead_time_54_hours = []
    lead_time_57_hours = []
    lead_time_60_hours = []
    lead_time_63_hours = []
    lead_time_66_hours = []
    lead_time_69_hours = []
    lead_time_72_hours = []
    lead_time_75_hours = []
    lead_time_78_hours = []

    if value == '1':
        points_to_calculate = calculation_of_the_point_number() + 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_\d{2}', file):
                print(file)
                current_file = PATH + file
                file_reader = pd.read_csv(current_file, sep='/s', skiprows=1, header=None, engine='python')
                data_from_file = file_reader.values.tolist()
                num_rows = 0
                for i in range(0, 70):
                    data_from_file[i] = data_from_file[i][0].split()
                    if (data_from_file[i][0] == "04" or "05") and data_from_file[i][1] == '21':
                        if data_from_file[i][0] == '04':
                            correct_data_UGRD = calc_point(data_from_file,
                                                           getting_need_data_for_point(points_to_calculate,
                                                                                       data_from_file, num_rows),
                                                           num_rows)
                        if data_from_file[i][0] == '05':
                            correct_data_VGRD = calc_point(data_from_file,
                                                           getting_need_data_for_point(points_to_calculate,
                                                                                       data_from_file, num_rows),
                                                           num_rows)

                    num_rows += 1

                speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD, file))
                calculates_the_day_based_on_the_lead_time(speed_wind, reference_num)
                calculates_month_based_on_day(speed_wind, reference_num)
                calculation_of_the_year_based_on_month(speed_wind, reference_num)
                reference_num += 1

        for i in range(0, len(speed_wind)):
            lead_time = speed_wind[i][0][11:13]
            if lead_time == '00':
                lead_time_0_hours.append(speed_wind[i])
            if lead_time == '03':
                lead_time_3_hours.append(speed_wind[i])
            if lead_time == '06':
                lead_time_6_hours.append(speed_wind[i])
            if lead_time == '09':
                lead_time_9_hours.append(speed_wind[i])
            if lead_time == '12':
                lead_time_12_hours.append(speed_wind[i])
            if lead_time == '15':
                lead_time_15_hours.append(speed_wind[i])
            if lead_time == '18':
                lead_time_18_hours.append(speed_wind[i])
            if lead_time == '21':
                lead_time_21_hours.append(speed_wind[i])
            if lead_time == '24':
                lead_time_24_hours.append(speed_wind[i])
            if lead_time == '27':
                lead_time_27_hours.append(speed_wind[i])
            if lead_time == '30':
                lead_time_30_hours.append(speed_wind[i])
            if lead_time == '33':
                lead_time_33_hours.append(speed_wind[i])
            if lead_time == '36':
                lead_time_36_hours.append(speed_wind[i])
            if lead_time == '39':
                lead_time_39_hours.append(speed_wind[i])
            if lead_time == '42':
                lead_time_42_hours.append(speed_wind[i])
            if lead_time == '45':
                lead_time_45_hours.append(speed_wind[i])
            if lead_time == '48':
                lead_time_48_hours.append(speed_wind[i])
            if lead_time == '51':
                lead_time_51_hours.append(speed_wind[i])
            if lead_time == '54':
                lead_time_54_hours.append(speed_wind[i])
            if lead_time == '57':
                lead_time_57_hours.append(speed_wind[i])
            if lead_time == '60':
                lead_time_60_hours.append(speed_wind[i])
            if lead_time == '63':
                lead_time_63_hours.append(speed_wind[i])
            if lead_time == '66':
                lead_time_66_hours.append(speed_wind[i])
            if lead_time == '69':
                lead_time_69_hours.append(speed_wind[i])
            if lead_time == '72':
                lead_time_72_hours.append(speed_wind[i])
            if lead_time == '75':
                lead_time_75_hours.append(speed_wind[i])
            if lead_time == '78':
                lead_time_78_hours.append(speed_wind[i])
        '''print('lead_time_0_hours')
        print(lead_time_0_hours)
        print('lead_time_3_hours')
        print(lead_time_3_hours)
        print('lead_time_5_hours')
        print(lead_time_6_hours)
        print('lead_time_9_hours')
        print(lead_time_9_hours)
        print('lead_time_12_hours')
        print(lead_time_12_hours)
        print('lead_time_15_hours')
        print(lead_time_15_hours)
        print('lead_time_18_hours')
        print(lead_time_18_hours)
        print('lead_time_21_hours')
        print(lead_time_21_hours)
        print('lead_time_24_hours')
        print(lead_time_24_hours)
        print('lead_time_27_hours')
        print(lead_time_27_hours)
        print('lead_time_30_hours')
        print(lead_time_30_hours)
        print('lead_time_33_hours')
        print(lead_time_33_hours)
        print('lead_time_36_hours')
        print(lead_time_36_hours)
        print('lead_time_39_hours')
        print(lead_time_39_hours)
        print('lead_time_42_hours')
        print(lead_time_42_hours)
        print('lead_time_45_hours')
        print(lead_time_45_hours)
        print('lead_time_48_hours')
        print(lead_time_48_hours)
        print('lead_time_51_hours')
        print(lead_time_51_hours)
        print('lead_time_54_hours')
        print(lead_time_54_hours)
        print('lead_time_57_hours')
        print(lead_time_57_hours)
        print('lead_time_60_hours')
        print(lead_time_60_hours)
        print('lead_time_63_hours')
        print(lead_time_63_hours)
        print('lead_time_66_hours')
        print(lead_time_66_hours)
        print('lead_time_69_hours')
        print(lead_time_69_hours)
        print('lead_time_72_hours')
        print(lead_time_72_hours)
        print('lead_time_75_hours')
        print(lead_time_75_hours)
        print('lead_time_78_hours')
        print(lead_time_78_hours)'''
        speed_wind_with_lead_time = [lead_time_0_hours, lead_time_3_hours, lead_time_6_hours, lead_time_9_hours,
                                     lead_time_12_hours, lead_time_15_hours, lead_time_18_hours, lead_time_21_hours,
                                     lead_time_24_hours, lead_time_27_hours, lead_time_30_hours, lead_time_33_hours,
                                     lead_time_36_hours, lead_time_39_hours, lead_time_42_hours, lead_time_45_hours,
                                     lead_time_48_hours, lead_time_51_hours, lead_time_54_hours, lead_time_57_hours,
                                     lead_time_60_hours, lead_time_63_hours, lead_time_66_hours, lead_time_69_hours,
                                     lead_time_72_hours, lead_time_75_hours, lead_time_78_hours]
    elif value == '2':
        low_point_number, top_point_number = calculation_of_the_area_of_points()
        low_point_number += 1
        top_point_number += 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_\d{2}', file):
                current_file = PATH + file
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
                                                                                         top_point_number, num_rows),
                                                              num_rows)
    #print(speed_wind_with_lead_time)
    write_list_in_file('list_data', speed_wind_with_lead_time)
    return speed_wind_with_lead_time
#main_for_difference_lead_time('1')
