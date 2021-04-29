import pandas as pd
import os
import re



def main_for_point():
    reference_num = 0
    speed_wind = []

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

    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])

    return speed_wind_with_lead_time_on_this_day


def main_for_area():
    reference_num = 0
    speed_wind = []

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

    # write_data_to_a_file(speed_wind, my_file)

    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])

    return speed_wind_with_lead_time_on_this_day
