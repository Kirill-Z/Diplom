import math
import pandas as pd
import wind_forecast
import practical_wind_forecast

#value = input("Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
#if value == '1':
#speed_wind_predictive = wind_forecast.main_for_difference_lead_time('1')
# elif value == '2':
#    speed_wind_predictive = wind_forecast.main(value)#
current_file = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/gfc/2016/list_data"
file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
print(file_reader)
speed_wind_predictive_true = []
speed_wind_predictive = file_reader.values.tolist()


def write_in_speed_predictive(lead_time: str):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


speed_wind_predictive_true.append(write_in_speed_predictive('00'))
speed_wind_predictive_true.append(write_in_speed_predictive('03'))
speed_wind_predictive_true.append(write_in_speed_predictive('06'))
speed_wind_predictive_true.append(write_in_speed_predictive('09'))
speed_wind_predictive_true.append(write_in_speed_predictive('12'))
speed_wind_predictive_true.append(write_in_speed_predictive('15'))
speed_wind_predictive_true.append(write_in_speed_predictive('18'))
speed_wind_predictive_true.append(write_in_speed_predictive('21'))
speed_wind_predictive_true.append(write_in_speed_predictive('24'))
speed_wind_predictive_true.append(write_in_speed_predictive('27'))
speed_wind_predictive_true.append(write_in_speed_predictive('30'))
speed_wind_predictive_true.append(write_in_speed_predictive('33'))
speed_wind_predictive_true.append(write_in_speed_predictive('36'))
speed_wind_predictive_true.append(write_in_speed_predictive('39'))
speed_wind_predictive_true.append(write_in_speed_predictive('42'))
speed_wind_predictive_true.append(write_in_speed_predictive('45'))
speed_wind_predictive_true.append(write_in_speed_predictive('48'))
speed_wind_predictive_true.append(write_in_speed_predictive('51'))
speed_wind_predictive_true.append(write_in_speed_predictive('54'))
speed_wind_predictive_true.append(write_in_speed_predictive('57'))
speed_wind_predictive_true.append(write_in_speed_predictive('60'))
speed_wind_predictive_true.append(write_in_speed_predictive('63'))
speed_wind_predictive_true.append(write_in_speed_predictive('66'))
speed_wind_predictive_true.append(write_in_speed_predictive('69'))
speed_wind_predictive_true.append(write_in_speed_predictive('72'))
speed_wind_predictive_true.append(write_in_speed_predictive('75'))
speed_wind_predictive_true.append(write_in_speed_predictive('78'))



#print(speed_wind_predictive_true)
speed_wind_practical = practical_wind_forecast.main('1')
#print("speed_practical")
#print(len(speed_wind_practical))
#print("practical_end")


def calc_diff(lead_time, diff_num_lead_time):
    if speed_wind_predictive_true[i][j][0][11:13] == lead_time:


        #if j > len(speed_wind_practical[i + j * 8])
        #print(speed_wind_predictive_true[i][j][3])
        #print(speed_wind_predictive[i][j][0])
        #print(speed_wind_practical[i + j * 8][3])
        #print('i')
        #print(i)
        #print('j')
        #print(j)
        print(i + j * 8)
        if i + j * 8 < (len(speed_wind_practical) - 1):
            if speed_wind_predictive_true[i][j][3] == int(speed_wind_practical[i + j * 8][3]):

                #diff_num_lead_time.append(speed_wind_predictive_true[i][j][0])
                #print(speed_wind_practical[i + j * 8])
                #print(speed_wind_predictive[i][j])
                #print(speed_wind_practical[i + j * 8][5])
                #print(" - ")
                #print(speed_wind_predictive[i][j][5])
                diff_num_lead_time.append(
                    float(speed_wind_practical[i + j * 8][5]) - float(speed_wind_predictive_true[i][j][5]))
                #print(diff_num_lead_time)

    return diff_num_lead_time


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
        diff_0_lead_time = calc_diff('00', diff_0_lead_time)
        diff_3_lead_time = (calc_diff('03', diff_3_lead_time))
        diff_6_lead_time = (calc_diff('06', diff_6_lead_time))
        diff_9_lead_time = (calc_diff('09', diff_9_lead_time))
        diff_12_lead_time = (calc_diff('12', diff_12_lead_time))
        diff_15_lead_time = (calc_diff('15', diff_15_lead_time))
        diff_18_lead_time = (calc_diff('18', diff_18_lead_time))
        diff_21_lead_time = (calc_diff('21', diff_21_lead_time))
        diff_24_lead_time = (calc_diff('24', diff_24_lead_time))
        diff_27_lead_time = (calc_diff('27', diff_27_lead_time))
        diff_30_lead_time = (calc_diff('30', diff_30_lead_time))
        diff_33_lead_time = (calc_diff('33', diff_33_lead_time))
        diff_36_lead_time = (calc_diff('36', diff_36_lead_time))
        diff_39_lead_time = (calc_diff('39', diff_39_lead_time))
        diff_42_lead_time = (calc_diff('42', diff_42_lead_time))
        diff_45_lead_time = (calc_diff('45', diff_45_lead_time))
        diff_48_lead_time = (calc_diff('48', diff_48_lead_time))
        diff_51_lead_time = (calc_diff('51', diff_51_lead_time))
        diff_54_lead_time = (calc_diff('54', diff_54_lead_time))
        diff_57_lead_time = (calc_diff('57', diff_57_lead_time))
        diff_60_lead_time = (calc_diff('60', diff_60_lead_time))
        diff_63_lead_time = (calc_diff('63', diff_63_lead_time))
        diff_66_lead_time = (calc_diff('66', diff_66_lead_time))
        diff_69_lead_time = (calc_diff('69', diff_69_lead_time))
        diff_72_lead_time = (calc_diff('72', diff_72_lead_time))
        diff_75_lead_time = (calc_diff('75', diff_75_lead_time))
        diff_78_lead_time = (calc_diff('78', diff_78_lead_time))


def calc_the_average_diff_for_the_lead_time(diff_lead_time):
    #print(diff_lead_time)
    average_diff: int = 0
    for i in range(1, len(diff_lead_time), 2):
        #print(diff_lead_time[i])
        average_diff += diff_lead_time[i]
    average_diff = average_diff / (len(diff_lead_time) / 2)
    #print(average_diff)
    return average_diff

print(diff_0_lead_time )
print(diff_3_lead_time )
print(diff_6_lead_time )
print(diff_9_lead_time )
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


print('Средняя разность для заблаговременности 0 часов:')
print(average_diff_0)
print('Средняя разность для заблаговременности 3 часа:')
print(average_diff_3)
print('Средняя разность для заблаговременности 6 часов:')
print(average_diff_6)
print('Средняя разность для заблаговременности 9 часов:')
print(average_diff_9)
print('Средняя разность для заблаговременности 12 часов:')
print(average_diff_12)
print('Средняя разность для заблаговременности 15 часов:')
print(average_diff_15)
print('Средняя разность для заблаговременности 18 часов:')
print(average_diff_18)
print('Средняя разность для заблаговременности 21 час:')
print(average_diff_21)
print('Средняя разность для заблаговременности 24 часа:')
print(average_diff_24)
print('Средняя разность для заблаговременности 27 часов:')
print(average_diff_27)
print('Средняя разность для заблаговременности 30 часов:')
print(average_diff_30)
print('Средняя разность для заблаговременности 33 часа:')
print(average_diff_33)
print('Средняя разность для заблаговременности 36 часов:')
print(average_diff_36)
print('Средняя разность для заблаговременности 39 часов:')
print(average_diff_39)
print('Средняя разность для заблаговременности 42 часа:')
print(average_diff_42)
print('Средняя разность для заблаговременности 45 часов:')
print(average_diff_45)
print('Средняя разность для заблаговременности 48 часов:')
print(average_diff_48)
print('Средняя разность для заблаговременности 51 час:')
print(average_diff_51)
print('Средняя разность для заблаговременности 54 часа:')
print(average_diff_54)
print('Средняя разность для заблаговременности 57 часов:')
print(average_diff_57)
print('Средняя разность для заблаговременности 60 часов:')
print(average_diff_60)
print('Средняя разность для заблаговременности 63 часа:')
print(average_diff_63)
print('Средняя разность для заблаговременности 66 часов:')
print(average_diff_66)
print('Средняя разность для заблаговременности 69 часов:')
print(average_diff_69)
print('Средняя разность для заблаговременности 72 часа:')
print(average_diff_72)
print('Средняя разность для заблаговременности 75 часов:')
print(average_diff_75)
print('Средняя разность для заблаговременности 78 часов:')
print(average_diff_78)
