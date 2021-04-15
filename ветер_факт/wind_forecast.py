import pandas as pd
import os
import re
import plotting

def main():
    PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/part_of_directory_2016/"

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

    def adding_information(get_data, num_rows):
        correct_data = []
        correct_data.append(data_from_file[num_rows][0])  # Adding wind direction information
        correct_data.append(data_from_file[num_rows][1])  # Adding Level Information

        correct_data.append(get_data)  # Call getting_need_data function
        return correct_data

    # Obtaining data on the direction of wind speed
    def getting_need_data_for_point(point_to_calculate, num_rows):
        for j in range(0, len(data_from_file[num_rows])):
            if j == point_to_calculate:
                correct_data = data_from_file[num_rows][j]
                return correct_data

    def getting_need_data_for_area(low_points_to_calculate, top_points_to_calculate, num_rows):
        for j in range(0, len(data_from_file[num_rows])):
            if low_points_to_calculate < j < top_points_to_calculate:
                correct_data = (data_from_file[num_rows][j])
                return correct_data

    def adding_data_to_the_speed_list(list_correct_data):
        speed_wind = 'speed_wind_' + file
        speed_wind = []
        speed_wind.append(file)  # Adding a file name
        speed_wind.append(file[slice(0, 4)])  # Adding the year
        speed_wind.append(int(file[slice(4, 6)]))  # Adding a month
        speed_wind.append(int(file[slice(6, 8)]))  # Adding a day
        speed_wind.append(int(file[slice(11, 13)]))  # Adding lead times
        speed_wind.append(list_correct_data[1])  # Adding a level
        return speed_wind

    def calculation_wind_speed(correct_data_VGRD, correct_data_UGRD):
        speed_wind = adding_data_to_the_speed_list(correct_data_VGRD)
        for j in range(2, len(correct_data_VGRD)):
            speed_wind.append(((float(correct_data_UGRD[j]) ** 2) +
                               (float(correct_data_VGRD[j]) ** 2)) ** (1 / 2))
        if len(speed_wind) > 7:
            speed_wind[6] = calculation_of_the_average_speed_in_the_range(speed_wind)
        return speed_wind

    def calculation_of_the_average_speed_in_the_range(speed_wind):
        num_of_points = 0
        for i in range(7, len(speed_wind)):
            speed_wind[6] += speed_wind[i]
            num_of_points += 1
        speed_wind[6] /= num_of_points
        return speed_wind[6]

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
            if int(speed_wind[reference_num][2] == num_of_days) and speed_wind[reference_num][3] > day_in_month[
                num_of_days]:
                speed_wind[reference_num][3] = int(speed_wind[reference_num][3]) - day_in_month[num_of_days]
                speed_wind[reference_num][2] += 1

    def calculation_of_the_year_based_on_month():  # Used when the month value overflows > 13
        if int(speed_wind[reference_num][2]) > 12:
            speed_wind[reference_num][2] = speed_wind[reference_num][2] - 12
            speed_wind[reference_num][1] = int(speed_wind[reference_num][1]) + 1

    def calc_point(get_data, num_rows):
        correct_data = adding_information(get_data, num_rows)
        return correct_data

    def calc_for_area(get_data):
        correct_data = adding_information(get_data, num_rows)
        return correct_data

    def write_data_to_a_file(speed_wind, my_file):
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
        return print('The end of the script')

    reference_num = 0
    speed_wind = []
    value = input("If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")

    if value == '1':
        my_file = open(PATH + 'data_out_for_Tolmachevo_point_01_2016', 'w')
        my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
        points_to_calculate = calculation_of_the_point_number() + 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_\d{2}', file):
                currentFile = PATH + file
                file_reader = pd.read_csv(currentFile, sep='/s', skiprows=1, header=None, engine='python')
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

        # print(len(speed_wind))
        write_data_to_a_file(speed_wind, my_file)

    elif value == '2':
        my_file = open(PATH + 'data_for_points_around_Tolmachevo_01_2016 ', 'w')
        my_file.write('File name     |   Year |Month |  Day |Lead Time|Level|         Wind Speed\n')
        low_point_number, top_point_number = calculation_of_the_area_of_points()
        low_point_number += 1
        top_point_number += 1
        for file in sorted(os.listdir(PATH)):
            if re.match('\d{10}_\d{2}', file):
                currentFile = PATH + file
                file_reader = pd.read_csv(currentFile, sep='/s', skiprows=1, header=None, engine='python')
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

        # print(speed_wind)
        # print(len(speed_wind))
        write_data_to_a_file(speed_wind, my_file)

    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) <= 21:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])



    return speed_wind_with_lead_time_on_this_day




