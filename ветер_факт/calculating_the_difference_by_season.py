import math
import wind_forecast
import practical_wind_forecast

value = input("Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
if value == '1':
    speed_wind_predictive = wind_forecast.main(value)
elif value == '2':
    speed_wind_predictive = wind_forecast.main(value)

value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
              "press 2 or 3: ")
if value == '1':
    speed_wind_practical = practical_wind_forecast.main(value)
elif value == '2':
    speed_wind_practical = practical_wind_forecast.main(value)
elif value == '3':
    speed_wind_practical = practical_wind_forecast.main(value)


def calc_the_average_diff_for_the_season(diff_season):
    average_diff = 0
    for i in range(0, len(diff_season)):
        if len(diff_season[i]) > 1:
            average_diff += diff_season[i][1]
    average_diff = average_diff / len(diff_season)
    return average_diff

def get_need_data(data):
    for i in range(len(data)):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]

def main(speed_wind_predictive, speed_wind_practical):
    get_need_data(speed_wind_predictive)
    get_need_data(speed_wind_practical)
    diff = []
    for i in range(0, len(speed_wind_predictive)):
        diff1 = [speed_wind_practical[i][0]]
        for j in range(1, len(speed_wind_predictive[i])):
            if float(speed_wind_predictive[i][j]) >= 9999 or math.isnan(float(speed_wind_practical[i][j])):
                continue
            else:
                diff1.append(speed_wind_practical[i][j] - speed_wind_predictive[i][j])
        diff.append(diff1)
    diff_winter = []
    diff_spring = []
    diff_summer = []
    diff_autumn = []

    for i in range(0, len(diff)):
        month = diff[i][0][5:7]
        diff_value = diff[i]
        if month == '11':
            diff_winter.append(diff_value)
        if month == '12':
            diff_winter.append(diff_value)
        if month == '01':
            diff_winter.append(diff_value)
        if month == '02':
            diff_winter.append(diff_value)
        if month == '03':
            diff_winter.append(diff_value)
        if month == '04':
            diff_spring.append(diff_value)
        if month == '05':
            diff_spring.append(diff_value)
        if month == '06':
            diff_summer.append(diff_value)
        if month == '07':
            diff_summer.append(diff_value)
        if month == '08':
            diff_summer.append(diff_value)
        if month == '09':
            diff_autumn.append(diff_value)
        if month == '10':
            diff_autumn.append(diff_value)

    average_diff_winter = calc_the_average_diff_for_the_season(diff_winter)
    average_diff_spring = calc_the_average_diff_for_the_season(diff_spring)
    average_diff_summer = calc_the_average_diff_for_the_season(diff_summer)
    average_diff_autumn = calc_the_average_diff_for_the_season(diff_autumn)

    print('Средняя разность за зимний период:')
    print(average_diff_winter)
    print('Средняя  разность за весенний период:')
    print(average_diff_spring)
    print('Средняя  разность за летний период:')
    print(average_diff_summer)
    print('Средняя  разность за осениий период:')
    print(average_diff_autumn)


main(speed_wind_predictive, speed_wind_practical)
