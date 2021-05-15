import wind_forecast
import practical_wind_forecast
import pandas as pd
import difference_by_season as different
import abs_error_by_season as abs
import root_mean_square_error_by_season as rmse


def get_forecast_data():
    tmp = input('Press 1 if you want to calculate values')
    if tmp == "1":
        value = input(
            "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
        if value == '1':
            wind_forecast.main_for_difference_lead_time(value)
        elif value == '2':
            wind_forecast.main_for_difference_lead_time(value)

    current_file = "/home/kirill/Downloads/Data/gfs/2016/list_data"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_predictive = file_reader.values.tolist()
    return speed_wind_predictive


def get_observation_data():
    value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
                  "press 2 or 3: ")
    if value == '1':
        speed_wind_practical = practical_wind_forecast.main(value)
    elif value == '2':
        speed_wind_practical = practical_wind_forecast.main(value)
    elif value == '3':
        speed_wind_practical = practical_wind_forecast.main(value)

    return speed_wind_practical


def get_need_data(data):
    for i in range(len(data)):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]


def division_of_data_by_seasons(diff):
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
    return diff_winter, diff_spring, diff_summer, diff_autumn


def main():
    speed_wind_predictive = get_forecast_data()
    speed_wind_practical = get_observation_data()

    get_need_data(speed_wind_predictive)
    get_need_data(speed_wind_practical)

    print("Select calculation number:")
    print(10 * " " + "1. Different")
    print(10 * " " + "2. Absolute")
    print(10 * " " + "3. RMSE")
    print(10 * " " + "4. Correl coef")
    estimate = int(input())
    if estimate == 1:
        diff = different.calc_diff(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        average_diff_winter = different.calc_the_average_diff(diff_winter)
        average_diff_spring = different.calc_the_average_diff(diff_spring)
        average_diff_summer = different.calc_the_average_diff(diff_summer)
        average_diff_autumn = different.calc_the_average_diff(diff_autumn)

        print('Средняя разность за зимний период:')
        print(average_diff_winter)
        print('Средняя  разность за весенний период:')
        print(average_diff_spring)
        print('Средняя  разность за летний период:')
        print(average_diff_summer)
        print('Средняя  разность за осениий период:')
        print(average_diff_autumn)
    if estimate == 2:
        diff = abs.cacl_abs_diff(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        average_diff_winter = abs.calc_abs_diff(diff_winter)
        average_diff_spring = abs.calc_abs_diff(diff_spring)
        average_diff_summer = abs.calc_abs_diff(diff_summer)
        average_diff_autumn = abs.calc_abs_diff(diff_autumn)

        print('Абсолютная погрешность за зимний период:')
        print(average_diff_winter)
        print('Абсолютная погрешность за весенний период:')
        print(average_diff_spring)
        print('Абсолютная погрешность за летний период:')
        print(average_diff_summer)
        print('Абсолютная погрешность за осениий период:')
        print(average_diff_autumn)
    if estimate == 3:
        diff = rmse.calc_squared_difference(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        average_diff_winter = rmse.calc_rmse(diff_winter)
        average_diff_spring = rmse.calc_rmse(diff_spring)
        average_diff_summer = rmse.calc_rmse(diff_summer)
        average_diff_autumn = rmse.calc_rmse(diff_autumn)

        print('Среднеквадратичная ошибка за зимний период:')
        print(average_diff_winter)
        print('Среднеквадратичная ошибка за весенний период:')
        print(average_diff_spring)
        print('Среднеквадратичная ошибка за летний период:')
        print(average_diff_summer)
        print('Среднеквадратичная ошибка за осениий период:')
        print(average_diff_autumn)
    if estimate == 4:
        pass


main()
