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


def calc_correl_coef():
    x_avg = 0
    y_avg = 0
    for i in range(0, len(speed_wind_predictive)):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            x_avg += speed_wind_practical[i][1]
            y_avg += speed_wind_predictive[i][1]
    x_avg /= len(speed_wind_predictive)
    y_avg /= len(speed_wind_predictive)

    numerator = 0
    x = 0
    y = 0
    for i in range(0, len(speed_wind_predictive)):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            numerator += (speed_wind_practical[i][1] - x_avg)*(speed_wind_predictive[i][1] - y_avg)
            x += (speed_wind_practical[i][1] - x_avg)**2
            y += (speed_wind_predictive[i][1] - y_avg)**2
    denominator = math.sqrt(x*y)
    correl_coef = numerator / denominator

    return correl_coef


def distribution_by_month():
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
    print(speed_wind_predictive)
    print(speed_wind_practical)
    diff = []
    diff = calc_correl_coef()
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


    #print('Коэффициент корреляции за зимний период:')
    #print(average_diff_winter)
    #print('Коэффициент корреляции за весенний период:')
    #print(average_diff_spring)
    #print('Коэффициент корреляции за летний период:')
    #print(average_diff_summer)
    #print('Коэффициент корреляции за осениий период:')
    #print(average_diff_autumn)


main(speed_wind_predictive, speed_wind_practical)