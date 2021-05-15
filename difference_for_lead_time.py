import math
import pandas as pd
import wind_forecast
import practical_wind_forecast


def write_in_speed_predictive(lead_time: str, speed_wind_predictive):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


#def calc_diff(lead_time, diff_num_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j):
    if speed_wind_predictive_true[i][j][0][11:13] == lead_time:
        if i + j * 8 < (len(speed_wind_practical) - 1):
            if speed_wind_predictive_true[i][j][3] == int(speed_wind_practical[i + j * 8][3]):
                if float(speed_wind_predictive_true[i][j][5]) >= 9999 or math.isnan(
                        float(speed_wind_practical[i + j * 8][5])):
                    pass
                else:
                    diff_num_lead_time.append(
                        float(speed_wind_practical[i + j * 8][5]) - float(speed_wind_predictive_true[i][j][5]))

    return diff_num_lead_time


def calc_the_average_diff_for_the_lead_time(diff_lead_time):
    average_diff: int = 0
    for i in range(1, len(diff_lead_time), 2):
        average_diff += diff_lead_time[i]
    average_diff = average_diff / len(diff_lead_time)
    return average_diff


def print_avrega_dif(hour: str, average_diff):
    print('Средняя разность для заблаговременности ' + hour)
    print(average_diff)


def get_forecat_data():
    tmp = input('Press 1 if you want to calculate values')
    if tmp == "1":
        value = input(
            "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
        if value == '1':
            speed_wind_predictive = wind_forecast.main_for_difference_lead_time(value)
        elif value == '2':
            speed_wind_predictive = wind_forecast.main_for_difference_lead_time(value)

    current_file = "/home/kirill/Downloads/Data/gfs/2016/list_data"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_predictive_true = []
    speed_wind_predictive = file_reader.values.tolist()

    lead_time = (
        '00', '03', '06', '09', '12', '15', '18', '21', '24', '27', '30', '33', '36', '39', '42', '45', '48', '51',
        '54', '57', '60', '63', '66', '69', '72', '75', '78')

    for i in lead_time:
        speed_wind_predictive_true.append(write_in_speed_predictive(i, speed_wind_predictive))
    return speed_wind_predictive_true


def get_observation_data():
    speed_wind_practical = practical_wind_forecast.main('1')
    return speed_wind_practical


def calc_for_lead_time(calc_func, calc_average):
    speed_wind_predictive_true = get_observation_data()
    speed_wind_practical = get_observation_data()

    diff_0_lead_time = []
    diff_3_lead_time = []
    diff_6_lead_time = []
    diff_9_lead_time = []
    diff_12_lead_time = []
    diff_15_lead_time = []
    diff_18_lead_time = []
    diff_21_lead_time = []
    diff_24_lead_time = []
    diff_27_lead_time = []
    diff_30_lead_time = []
    diff_33_lead_time = []
    diff_36_lead_time = []
    diff_39_lead_time = []
    diff_42_lead_time = []
    diff_45_lead_time = []
    diff_48_lead_time = []
    diff_51_lead_time = []
    diff_54_lead_time = []
    diff_57_lead_time = []
    diff_60_lead_time = []
    diff_63_lead_time = []
    diff_66_lead_time = []
    diff_69_lead_time = []
    diff_72_lead_time = []
    diff_75_lead_time = []
    diff_78_lead_time = []

    for i in range(0, len(speed_wind_predictive_true)):
        for j in range(0, len(speed_wind_predictive_true[i])):
            diff_0_lead_time = calc_func('00', diff_0_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_3_lead_time = calc_func('03', diff_3_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_6_lead_time = calc_func('06', diff_6_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_9_lead_time = calc_func('09', diff_9_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_12_lead_time = calc_func('12', diff_12_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_15_lead_time = calc_func('15', diff_15_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_18_lead_time = calc_func('18', diff_18_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_21_lead_time = calc_func('21', diff_21_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_24_lead_time = calc_func('24', diff_24_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_27_lead_time = calc_func('27', diff_27_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_30_lead_time = calc_func('30', diff_30_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_33_lead_time = calc_func('33', diff_33_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_36_lead_time = calc_func('36', diff_36_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_39_lead_time = calc_func('39', diff_39_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_42_lead_time = calc_func('42', diff_42_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_45_lead_time = calc_func('45', diff_45_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_48_lead_time = calc_func('48', diff_48_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_51_lead_time = calc_func('51', diff_51_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_54_lead_time = calc_func('54', diff_54_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_57_lead_time = calc_func('57', diff_57_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_60_lead_time = calc_func('60', diff_60_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_63_lead_time = calc_func('63', diff_63_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_66_lead_time = calc_func('66', diff_66_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_69_lead_time = calc_func('69', diff_69_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_72_lead_time = calc_func('72', diff_72_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_75_lead_time = calc_func('75', diff_75_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)
            diff_78_lead_time = calc_func('78', diff_78_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j)

    average_diff_0 = calc_average(diff_0_lead_time)
    average_diff_3 = calc_average(diff_3_lead_time)
    average_diff_6 = calc_average(diff_6_lead_time)
    average_diff_9 = calc_average(diff_9_lead_time)
    average_diff_12 = calc_average(diff_12_lead_time)
    average_diff_15 = calc_average(diff_15_lead_time)
    average_diff_18 = calc_average(diff_18_lead_time)
    average_diff_21 = calc_average(diff_21_lead_time)
    average_diff_24 = calc_average(diff_24_lead_time)
    average_diff_27 = calc_average(diff_27_lead_time)
    average_diff_30 = calc_average(diff_30_lead_time)
    average_diff_33 = calc_average(diff_33_lead_time)
    average_diff_36 = calc_average(diff_36_lead_time)
    average_diff_39 = calc_average(diff_39_lead_time)
    average_diff_42 = calc_average(diff_42_lead_time)
    average_diff_45 = calc_average(diff_45_lead_time)
    average_diff_48 = calc_average(diff_48_lead_time)
    average_diff_51 = calc_average(diff_51_lead_time)
    average_diff_54 = calc_average(diff_54_lead_time)
    average_diff_57 = calc_average(diff_57_lead_time)
    average_diff_60 = calc_average(diff_60_lead_time)
    average_diff_63 = calc_average(diff_63_lead_time)
    average_diff_66 = calc_average(diff_66_lead_time)
    average_diff_69 = calc_average(diff_69_lead_time)
    average_diff_72 = calc_average(diff_72_lead_time)
    average_diff_75 = calc_average(diff_75_lead_time)
    average_diff_78 = calc_average(diff_78_lead_time)

    print_avrega_dif('0 часов', average_diff_0)
    print_avrega_dif('3 часа', average_diff_3)
    print_avrega_dif('6 часов', average_diff_6)
    print_avrega_dif('9 часов', average_diff_9)
    print_avrega_dif('12 часов', average_diff_12)
    print_avrega_dif('15 часов', average_diff_15)
    print_avrega_dif('18 часов', average_diff_18)
    print_avrega_dif('21 час', average_diff_21)
    print_avrega_dif('24 часа', average_diff_24)
    print_avrega_dif('27 часов', average_diff_27)
    print_avrega_dif('30 часов', average_diff_30)
    print_avrega_dif('33 часа', average_diff_33)
    print_avrega_dif('36 часов', average_diff_36)
    print_avrega_dif('39 часов', average_diff_39)
    print_avrega_dif('42 часа', average_diff_42)
    print_avrega_dif('45 часов', average_diff_45)
    print_avrega_dif('48 часов', average_diff_48)
    print_avrega_dif('51 час', average_diff_51)
    print_avrega_dif('54 часа', average_diff_54)
    print_avrega_dif('57 часов', average_diff_57)
    print_avrega_dif('60 часов', average_diff_60)
    print_avrega_dif('63 часа', average_diff_63)
    print_avrega_dif('66 часов', average_diff_66)
    print_avrega_dif('69 часов', average_diff_69)
    print_avrega_dif('72 часа', average_diff_72)
    print_avrega_dif('75 часов', average_diff_75)
    print_avrega_dif('78 часов', average_diff_78)
