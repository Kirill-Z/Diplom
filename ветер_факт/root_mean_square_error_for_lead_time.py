import math
import pandas as pd
import wind_forecast
import practical_wind_forecast


def write_in_speed_predictive(lead_time: str):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


def calc_diff_of_squares_of_squares(lead_time, diff_num_lead_time):
    if speed_wind_predictive_true[i][j][0][11:13] == lead_time:
        if i + j * 8 < (len(speed_wind_practical) - 1):
            if speed_wind_predictive_true[i][j][3] == int(speed_wind_practical[i + j * 8][3]):
                if float(speed_wind_predictive_true[i][j][5]) >= 9999 or math.isnan(float(speed_wind_practical[i + j * 8][5])):
                    pass
                else:
                    diff_num_lead_time.append((float(speed_wind_practical[i + j * 8][5]) - float(speed_wind_predictive_true[i][j][5]))**2)

    return diff_num_lead_time


def calc_the_average_diff_for_the_lead_time(diff_lead_time):
    average_diff: int = 0
    for i in range(1, len(diff_lead_time), 2):
        average_diff += diff_lead_time[i]

    average_diff = average_diff / len(diff_lead_time)
    return average_diff


tmp = input(
    'Press 1 if you want to calculate values or press 2 if you want to select ready-made speed data from a file: ')
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

speed_wind_practical = practical_wind_forecast.main('3')
#print(speed_wind_predictive)
#print(speed_wind_practical)
lead_time = ('00', '03', '06', '09', '12', '15', '18', '21', '24', '27', '30', '33', '36', '39', '42', '45', '48', '51',
             '54', '57', '60', '63', '66', '69', '72', '75', '78')

for i in lead_time:
    speed_wind_predictive_true.append(write_in_speed_predictive(i))




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
        diff_0_lead_time = calc_diff_of_squares_of_squares('00', diff_0_lead_time)
        diff_3_lead_time = (calc_diff_of_squares_of_squares('03', diff_3_lead_time))
        diff_6_lead_time = (calc_diff_of_squares_of_squares('06', diff_6_lead_time))
        diff_9_lead_time = (calc_diff_of_squares_of_squares('09', diff_9_lead_time))
        diff_12_lead_time = (calc_diff_of_squares_of_squares('12', diff_12_lead_time))
        diff_15_lead_time = (calc_diff_of_squares_of_squares('15', diff_15_lead_time))
        diff_18_lead_time = (calc_diff_of_squares_of_squares('18', diff_18_lead_time))
        diff_21_lead_time = (calc_diff_of_squares_of_squares('21', diff_21_lead_time))
        diff_24_lead_time = (calc_diff_of_squares_of_squares('24', diff_24_lead_time))
        diff_27_lead_time = (calc_diff_of_squares_of_squares('27', diff_27_lead_time))
        diff_30_lead_time = (calc_diff_of_squares_of_squares('30', diff_30_lead_time))
        diff_33_lead_time = (calc_diff_of_squares_of_squares('33', diff_33_lead_time))
        diff_36_lead_time = (calc_diff_of_squares_of_squares('36', diff_36_lead_time))
        diff_39_lead_time = (calc_diff_of_squares_of_squares('39', diff_39_lead_time))
        diff_42_lead_time = (calc_diff_of_squares_of_squares('42', diff_42_lead_time))
        diff_45_lead_time = (calc_diff_of_squares_of_squares('45', diff_45_lead_time))
        diff_48_lead_time = (calc_diff_of_squares_of_squares('48', diff_48_lead_time))
        diff_51_lead_time = (calc_diff_of_squares_of_squares('51', diff_51_lead_time))
        diff_54_lead_time = (calc_diff_of_squares_of_squares('54', diff_54_lead_time))
        diff_57_lead_time = (calc_diff_of_squares_of_squares('57', diff_57_lead_time))
        diff_60_lead_time = (calc_diff_of_squares_of_squares('60', diff_60_lead_time))
        diff_63_lead_time = (calc_diff_of_squares_of_squares('63', diff_63_lead_time))
        diff_66_lead_time = (calc_diff_of_squares_of_squares('66', diff_66_lead_time))
        diff_69_lead_time = (calc_diff_of_squares_of_squares('69', diff_69_lead_time))
        diff_72_lead_time = (calc_diff_of_squares_of_squares('72', diff_72_lead_time))
        diff_75_lead_time = (calc_diff_of_squares_of_squares('75', diff_75_lead_time))
        diff_78_lead_time = (calc_diff_of_squares_of_squares('78', diff_78_lead_time))




'''
print(diff_0_lead_time)
print(diff_3_lead_time)
print(diff_6_lead_time)
print(diff_9_lead_time)
print(diff_12_lead_time)
print(diff_15_lead_time)
print(diff_18_lead_time)
print(diff_21_lead_time)
print(diff_24_lead_time)
print(diff_27_lead_time)
print(diff_30_lead_time)
print(diff_33_lead_time)
print(diff_36_lead_time)
print(diff_39_lead_time)
print(diff_42_lead_time)
print(diff_45_lead_time)
print(diff_48_lead_time)
print(diff_51_lead_time)
print(diff_54_lead_time)
print(diff_57_lead_time)
print(diff_60_lead_time)
print(diff_63_lead_time)
print(diff_66_lead_time)
print(diff_69_lead_time)
print(diff_72_lead_time)
print(diff_75_lead_time)
print(diff_78_lead_time)
'''

average_diff_0 = calc_the_average_diff_for_the_lead_time(diff_0_lead_time)
average_diff_3 = calc_the_average_diff_for_the_lead_time(diff_3_lead_time)
average_diff_6 = calc_the_average_diff_for_the_lead_time(diff_6_lead_time)
average_diff_9 = calc_the_average_diff_for_the_lead_time(diff_9_lead_time)
average_diff_12 = calc_the_average_diff_for_the_lead_time(diff_12_lead_time)
average_diff_15 = calc_the_average_diff_for_the_lead_time(diff_15_lead_time)
average_diff_18 = calc_the_average_diff_for_the_lead_time(diff_18_lead_time)
average_diff_21 = calc_the_average_diff_for_the_lead_time(diff_21_lead_time)
average_diff_24 = calc_the_average_diff_for_the_lead_time(diff_24_lead_time)
average_diff_27 = calc_the_average_diff_for_the_lead_time(diff_27_lead_time)
average_diff_30 = calc_the_average_diff_for_the_lead_time(diff_30_lead_time)
average_diff_33 = calc_the_average_diff_for_the_lead_time(diff_33_lead_time)
average_diff_36 = calc_the_average_diff_for_the_lead_time(diff_36_lead_time)
average_diff_39 = calc_the_average_diff_for_the_lead_time(diff_39_lead_time)
average_diff_42 = calc_the_average_diff_for_the_lead_time(diff_42_lead_time)
average_diff_45 = calc_the_average_diff_for_the_lead_time(diff_45_lead_time)
average_diff_48 = calc_the_average_diff_for_the_lead_time(diff_48_lead_time)
average_diff_51 = calc_the_average_diff_for_the_lead_time(diff_51_lead_time)
average_diff_54 = calc_the_average_diff_for_the_lead_time(diff_54_lead_time)
average_diff_57 = calc_the_average_diff_for_the_lead_time(diff_57_lead_time)
average_diff_60 = calc_the_average_diff_for_the_lead_time(diff_60_lead_time)
average_diff_63 = calc_the_average_diff_for_the_lead_time(diff_63_lead_time)
average_diff_66 = calc_the_average_diff_for_the_lead_time(diff_66_lead_time)
average_diff_69 = calc_the_average_diff_for_the_lead_time(diff_69_lead_time)
average_diff_72 = calc_the_average_diff_for_the_lead_time(diff_72_lead_time)
average_diff_75 = calc_the_average_diff_for_the_lead_time(diff_75_lead_time)
average_diff_78 = calc_the_average_diff_for_the_lead_time(diff_78_lead_time)


print('Среднеквадратичная ошибка для заблаговременности 0 часов:')
print(average_diff_0)
print('Среднеквадратичная ошибка для заблаговременности 3 часа:')
print(average_diff_3)
print('Среднеквадратичная ошибка для заблаговременности 6 часов:')
print(average_diff_6)
print('Среднеквадратичная ошибка для заблаговременности 9 часов:')
print(average_diff_9)
print('Среднеквадратичная ошибка для заблаговременности 12 часов:')
print(average_diff_12)
print('Среднеквадратичная ошибка для заблаговременности 15 часов:')
print(average_diff_15)
print('Среднеквадратичная ошибка для заблаговременности 18 часов:')
print(average_diff_18)
print('Среднеквадратичная ошибка для заблаговременности 21 час:')
print(average_diff_21)
print('Среднеквадратичная ошибка для заблаговременности 24 часа:')
print(average_diff_24)
print('Среднеквадратичная ошибка для заблаговременности 27 часов:')
print(average_diff_27)
print('Среднеквадратичная ошибка для заблаговременности 30 часов:')
print(average_diff_30)
print('Среднеквадратичная ошибка для заблаговременности 33 часа:')
print(average_diff_33)
print('Среднеквадратичная ошибка для заблаговременности 36 часов:')
print(average_diff_36)
print('Среднеквадратичная ошибка для заблаговременности 39 часов:')
print(average_diff_39)
print('Среднеквадратичная ошибка для заблаговременности 42 часа:')
print(average_diff_42)
print('Среднеквадратичная ошибка для заблаговременности 45 часов:')
print(average_diff_45)
print('Среднеквадратичная ошибка для заблаговременности 48 часов:')
print(average_diff_48)
print('Среднеквадратичная ошибка для заблаговременности 51 час:')
print(average_diff_51)
print('Среднеквадратичная ошибка для заблаговременности 54 часа:')
print(average_diff_54)
print('Среднеквадратичная ошибка для заблаговременности 57 часов:')
print(average_diff_57)
print('Среднеквадратичная ошибка для заблаговременности 60 часов:')
print(average_diff_60)
print('Среднеквадратичная ошибка для заблаговременности 63 часа:')
print(average_diff_63)
print('Среднеквадратичная ошибка для заблаговременности 66 часов:')
print(average_diff_66)
print('Среднеквадратичная ошибка для заблаговременности 69 часов:')
print(average_diff_69)
print('Среднеквадратичная ошибка для заблаговременности 72 часа:')
print(average_diff_72)
print('Среднеквадратичная ошибка для заблаговременности 75 часов:')
print(average_diff_75)
print('Среднеквадратичная ошибка для заблаговременности 78 часов:')
print(average_diff_78)
