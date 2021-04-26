import pandas as pd
import os
import re


def main():
    PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/2016/"

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

    def adding_information(get_data, num_item):
        correct_data = [data_from_file[num_item][0], data_from_file[num_item][1]]
        speed_data = get_data
        if len(speed_data) > 2:

            for i in range(0, len(speed_data)):
                correct_data.append(speed_data[i])
        else:
            correct_data.append(speed_data)
        return correct_data

    # Obtaining data on the direction of wind speed
    def getting_need_data_for_point(point_to_calculate, num_item):
        for j in range(0, len(data_from_file[num_item])):
            if j == point_to_calculate:
                correct_data = data_from_file[num_item][j]
        return correct_data

    def getting_need_data_for_area(low_points_to_calculate, top_points_to_calculate, num_item):
        correct_data = []
        for j in range(0, len(data_from_file[num_item])):
            if low_points_to_calculate < j < top_points_to_calculate:
                correct_data.append(data_from_file[num_item][j])
        return correct_data

    def adding_data_to_the_speed_list():
        # Adding file name, year, month, day, time
        wind_data = [file, file[slice(0, 4)], int(file[slice(4, 6)]), int(file[slice(6, 8)]), int(file[slice(11, 13)])]
        return wind_data

    def calculation_wind_speed(correct_data_VGRD, correct_data_UGRD):
        speed = adding_data_to_the_speed_list()
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

    def calculates_the_day_based_on_the_lead_time():
        hours_in_a_day = {1: 24, 2: 48, 3: 72, 4: 96}
        for i in hours_in_a_day:
            if hours_in_a_day[i] <= int(speed_wind[reference_num][4]) < hours_in_a_day[i + 1]:
                speed_wind[reference_num][4] = int(speed_wind[reference_num][4]) - hours_in_a_day[i]
                speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) + i

    def calculates_month_based_on_day():
        day_in_month = {1: 31, 2: (29 if (int(speed_wind[reference_num][1]) % 4 == 0) else 28), 3: 31, 4: 30, 5: 31,
                        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for num_of_days in day_in_month.keys():
            if int(speed_wind[reference_num][2] == num_of_days) and \
                    speed_wind[reference_num][3] > day_in_month[num_of_days]:
                speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]
                speed_wind[reference_num][2] += 1

    def calculation_of_the_year_based_on_month():  # Used when the month value overflows > 13
        if int(speed_wind[reference_num][2]) > 12:
            speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
            speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1

    def calc_point(get_data, num_item):
        correct_data = adding_information(get_data, num_item)
        return correct_data

    def calc_for_area(get_data):
        correct_data = adding_information(get_data, num_rows)
        return correct_data

    def write_data_to_a_file(speed, write_file):
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

    reference_num = 0
    speed_wind = []
    value = input("If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")

    if value == '1':
        #my_file = open(PATH + 'data_out_for_Tolmachevo_point_01_2016', 'w')
        #my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
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
                            correct_data_UGRD = calc_point(getting_need_data_for_point(points_to_calculate, num_rows),
                                                           num_rows)
                        if data_from_file[i][0] == '05':
                            correct_data_VGRD = calc_point(getting_need_data_for_point(points_to_calculate, num_rows),
                                                           num_rows)

                    num_rows += 1

                speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD))

                calculates_the_day_based_on_the_lead_time()
                calculates_month_based_on_day()
                calculation_of_the_year_based_on_month()
                reference_num += 1

        #write_data_to_a_file(speed_wind, my_file)

    elif value == '2':
        #my_file = open(PATH + 'data_for_points_around_Tolmachevo_01_2016 ', 'w')
        #my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
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
                            correct_data_UGRD = calc_for_area(
                                getting_need_data_for_area(low_point_number, top_point_number, num_rows))

                        if data_from_file[i][0] == '05':
                            correct_data_VGRD = calc_for_area(
                                getting_need_data_for_area(low_point_number, top_point_number, num_rows))

                    num_rows += 1
                speed_wind.append(calculation_wind_speed(correct_data_VGRD, correct_data_UGRD))

                calculates_the_day_based_on_the_lead_time()
                calculates_month_based_on_day()
                calculation_of_the_year_based_on_month()
                reference_num += 1

        #write_data_to_a_file(speed_wind, my_file)

    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])

    return speed_wind_with_lead_time_on_this_day