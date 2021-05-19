import wind_forecast
import practical_wind_forecast
import pandas as pd
import difference_by_season as different
import abs_error_by_season as abs
import root_mean_square_error_by_season as rmse
import correl_coef_by_season as correl


def get_forecast_data():
    tmp = input('Press 1 if you want to calculate values')
    if tmp == "1":
        value = input(
            "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
        if value == '1':
            wind_forecast.main(value)
        elif value == '2':
            wind_forecast.main(value)

    current_file = "/home/kirill/Downloads/Data/gfs/list_data_by_season"  # Path to the predicted wind speed file
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
        month = str(diff[i][0][5:7])
        diff_value = diff[i]
        if month == '11':
            diff_winter.append(diff_value)
        if month == '12':
            diff_winter.append(diff_value)

        if month == '01':
            diff_winter.append(diff_value)
        if month == '1-':
            diff_winter.append(diff_value)

        if month == '02':
            diff_winter.append(diff_value)
        if month == '2-':
            diff_winter.append(diff_value)

        if month == '03':
            diff_winter.append(diff_value)
        if month == '3-':
            diff_winter.append(diff_value)

        if month == '04':
            diff_spring.append(diff_value)
        if month == '4-':
            diff_spring.append(diff_value)

        if month == '05':
            diff_spring.append(diff_value)
        if month == '5-':
            diff_spring.append(diff_value)

        if month == '06':
            diff_summer.append(diff_value)
        if month == '6-':
            diff_summer.append(diff_value)

        if month == '07':
            diff_summer.append(diff_value)
        if month == '7-':
            diff_summer.append(diff_value)

        if month == '08':
            diff_summer.append(diff_value)
        if month == '8-':
            diff_summer.append(diff_value)

        if month == '09':
            diff_autumn.append(diff_value)
        if month == '9-':
            diff_autumn.append(diff_value)

        if month == '10':
            diff_autumn.append(diff_value)

    return diff_winter, diff_spring, diff_summer, diff_autumn


def test_for_emptiness(diff, calc_func):
    if len(diff) != 0:
        diff_season = calc_func
    return diff_season


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
    estimate = int(input("Calculation number: "))
    if estimate == 1:
        diff = different.calc_diff(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        average_diff_winter = test_for_emptiness(diff_winter, different.calc_the_average_diff(diff_winter))
        average_diff_spring = test_for_emptiness(diff_spring, different.calc_the_average_diff(diff_spring))
        average_diff_summer = test_for_emptiness(diff_summer, different.calc_the_average_diff(diff_summer))
        average_diff_autumn = test_for_emptiness(diff_autumn, different.calc_the_average_diff(diff_autumn))

        print(f'Средняя разность за зимний период:    {average_diff_winter}')
        print(f'Средняя  разность за весенний период: {average_diff_spring}')
        print(f'Средняя  разность за летний период:   {average_diff_summer}')
        print(f'Средняя  разность за осениий период:  {average_diff_autumn}')
    if estimate == 2:
        diff = abs.cacl_abs_diff(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        abs_diff_winter = test_for_emptiness(diff_winter, abs.calc_abs(diff_winter))
        abs_diff_spring = test_for_emptiness(diff_spring, abs.calc_abs(diff_spring))
        abs_diff_summer = test_for_emptiness(diff_summer, abs.calc_abs(diff_summer))
        abs_diff_autumn = test_for_emptiness(diff_autumn, abs.calc_abs(diff_autumn))

        print(f'Абсолютная погрешность за зимний период:   {abs_diff_winter}')
        print(f'Абсолютная погрешность за весенний период: {abs_diff_spring}')
        print(f'Абсолютная погрешность за летний период:   {abs_diff_summer}')
        print(f'Абсолютная погрешность за осениий период:  {abs_diff_autumn}')
    if estimate == 3:
        diff = rmse.calc_squared_difference(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        rmse_winter = test_for_emptiness(diff_winter, rmse.calc_rmse(diff_winter))
        rmse_spring = test_for_emptiness(diff_spring, rmse.calc_rmse(diff_spring))
        rmse_summer = test_for_emptiness(diff_summer, rmse.calc_rmse(diff_summer))
        rmse_autumn = test_for_emptiness(diff_autumn, rmse.calc_rmse(diff_autumn))

        print(f'Среднеквадратичная ошибка за зимний период:   {rmse_winter}')
        print(f'Среднеквадратичная ошибка за весенний период: {rmse_spring}')
        print(f'Среднеквадратичная ошибка за летний период:   {rmse_summer}')
        print(f'Среднеквадратичная ошибка за осениий период:  {rmse_autumn}')
    if estimate == 4:
        diff_winter_predictive, \
        diff_spring_predictive, \
        diff_summer_predictive, \
        diff_autumn_predictive = division_of_data_by_seasons(speed_wind_predictive)

        diff_winter_practical, \
        diff_spring_practical, \
        diff_summer_practical, \
        diff_autumn_practical = division_of_data_by_seasons(speed_wind_practical)

        if (len(diff_winter_predictive) and len(diff_winter_practical)) != 0:
            correl_coef_winter = correl.calc_correl_coef(diff_winter_predictive, diff_winter_practical)
        if (len(diff_spring_predictive) and len(diff_spring_practical)) != 0:
            correl_coef_spring = correl.calc_correl_coef(diff_spring_predictive, diff_spring_practical)
        if (len(diff_summer_predictive) and len(diff_summer_practical)) != 0:
            correl_coef_summer = correl.calc_correl_coef(diff_summer_predictive, diff_summer_practical)
        if (len(diff_autumn_predictive) and len(diff_autumn_practical)) != 0:
            correl_coef_autumn = correl.calc_correl_coef(diff_autumn_predictive, diff_autumn_practical)

        print(f'Коэффициент корреляции за зимний период:   {correl_coef_winter}')
        print(f'Коэффициент корреляции за весенний период: {correl_coef_spring}')
        print(f'Коэффициент корреляции за летний период:   {correl_coef_summer}')
        print(f'Коэффициент корреляции за осениий период:  {correl_coef_autumn}')


main()
