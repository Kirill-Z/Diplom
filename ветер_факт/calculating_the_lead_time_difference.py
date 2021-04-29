import math
import wind_forecast
import practical_wind_forecast

value = input("Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
if value == '1':
    speed_wind_predictive = wind_forecast.main_for_difference_lead_time(value)
# elif value == '2':
#    speed_wind_predictive = wind_forecast.main(value)

speed_wind_practical = practical_wind_forecast.main(1)
print(len(speed_wind_predictive[0]))


def calc_diff(lead_time, diff_num_lead_time):
    if speed_wind_predictive[i][j][0][11:13] == lead_time:
        if speed_wind_predictive[i][j][3] == int(speed_wind_practical[i + j * 8][3]):
            diff_num_lead_time.append(speed_wind_predictive[i][j][0])
            diff_num_lead_time.append(
                float(speed_wind_practical[i + j * 8][5]) - float(speed_wind_predictive[i][j][5]))

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
for i in range(0, len(speed_wind_predictive)):
    for j in range(0, len(speed_wind_predictive[i])):
        diff_0_lead_time.append(calc_diff('00', diff_0_lead_time))
        diff_3_lead_time.append(calc_diff('03', diff_3_lead_time))
        diff_6_lead_time.append(calc_diff('06', diff_6_lead_time))
        diff_9_lead_time.append(calc_diff('09', diff_9_lead_time))
        diff_12_lead_time.append(calc_diff('12', diff_12_lead_time))
        diff_15_lead_time.append(calc_diff('15', diff_15_lead_time))
        diff_18_lead_time.append(calc_diff('18', diff_18_lead_time))
        diff_21_lead_time.append(calc_diff('21', diff_21_lead_time))
        diff_24_lead_time.append(calc_diff('24', diff_24_lead_time))
        diff_27_lead_time.append(calc_diff('27', diff_27_lead_time))
        diff_30_lead_time.append(calc_diff('30', diff_30_lead_time))
        diff_33_lead_time.append(calc_diff('33', diff_33_lead_time))
        diff_36_lead_time.append(calc_diff('36', diff_36_lead_time))
        diff_39_lead_time.append(calc_diff('39', diff_39_lead_time))
        diff_42_lead_time.append(calc_diff('42', diff_42_lead_time))
        diff_45_lead_time.append(calc_diff('45', diff_45_lead_time))
        diff_48_lead_time.append(calc_diff('48', diff_48_lead_time))
        diff_51_lead_time.append(calc_diff('51', diff_51_lead_time))
        diff_54_lead_time.append(calc_diff('54', diff_54_lead_time))
        diff_57_lead_time.append(calc_diff('57', diff_57_lead_time))
        diff_60_lead_time.append(calc_diff('60', diff_60_lead_time))
        diff_63_lead_time.append(calc_diff('63', diff_63_lead_time))
        diff_66_lead_time.append(calc_diff('66', diff_66_lead_time))
        diff_69_lead_time.append(calc_diff('69', diff_69_lead_time))
        diff_72_lead_time.append(calc_diff('72', diff_72_lead_time))
        diff_75_lead_time.append(calc_diff('75', diff_75_lead_time))
        diff_78_lead_time.append(calc_diff('78', diff_78_lead_time))

def calc_the_average_diff_for_the_lead_time(diff_lead_time):
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        if len(diff_lead_time[i]) > 1:
            average_diff += diff_lead_time[i][1]
    average_diff = average_diff / len(diff_lead_time)
    return average_diff

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

print('Средняя разность дял заблаговременности 0 часов:')
