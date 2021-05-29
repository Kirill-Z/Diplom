import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import get_data
import pandas as pd
import math
from calc_error import separation_of_data_by_seasons, separation_data_by_lead_time_forecast, \
                       separation_data_by_lead_time_observation
from difference import get_diff_for_season_and_lead_time_recovery, print_average_diff
import abs_error as abs
import plotting
import root_mean_square_error as rmse
import correl_coef as correlation


def write_in_speed_forecast(lead_time: str, speed_wind_forecast):
    local_speed_wind = []
    for i in range(0, len(speed_wind_forecast)):
        if speed_wind_forecast[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_forecast[i])
    return local_speed_wind


def get_coefficient_for_linear_regression(predictant, predictor):
    true_predictant = []
    true_predictor = []
    for i in range(0, len(predictant)):
        if float(predictor[i]) >= 9999 or math.isnan(float(predictant[i])):
            continue
        else:
            true_predictant.append(predictant[i])
            true_predictor.append(predictor[i])
    x = np.array(true_predictant).reshape((-1, 1))
    y = np.array(true_predictor).reshape((-1, 1))

    if len(x) < len(y):
        length_array = len(x)
    elif len(y) < len(x):
        length_array = len(y)
    else:
        length_array = len(x)

    model = LinearRegression().fit(y[0:length_array], x[0:length_array])
    coefficient = [model.intercept_, model.coef_]
    return coefficient


def linear_regression(forecast_test, b0, b1):
    forecast_test = np.array(forecast_test).reshape((-1, 1))
    y_pred = b0 + b1 * forecast_test

    return y_pred.tolist()


def plot_data(lead_time_forecast, label, color):
    for i in range(0, len(lead_time_forecast)):
        for j in range(0, len(lead_time_forecast[i])):
            if i == 0 and j == 0:
                plt.scatter(i * 3, lead_time_forecast[i][j], c=color,
                            label=label)
            else:
                plt.scatter(i * 3, lead_time_forecast[i][j], c=color)
                    

def get_correl_coef_regression_for_season(season, lead_time_observation, lead_time_forecast):
    b0_season = []
    b1_season = []
    print(10 * ' ' + f'Коэффициенты для {season} периода')
    lead_time = 0
    print(lead_time_forecast[0])
    print('observation')
    print(lead_time_observation[0])
    for i in range(0, 8):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation[i],
                                                        lead_time_forecast[i])
        b0_season.append(b0)
        b1_season.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3
    for i in range(8, 10):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation[i - 8],
                                                        lead_time_forecast[i])
        b0_season.append(b0)
        b1_season.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    return b0_season, b1_season


def get_recovery_data_for_season(lead_time_forecast_season, b0, b1):
    recovery_data = []
    lead_time = 0
    for i in range(0, 8):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i], b1[i]))
        lead_time += 3
    for i in range(8, 10):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i], b1[i]))
        lead_time += 3
    for i in range(10, 18):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i-10], b1[i-10]))
        lead_time += 3
    for i in range(18, 20):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i-10], b1[i-10]))
        lead_time += 3
    for i in range(20, 24):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i-20], b1[i-20]))
        lead_time += 3
    for i in range(24, 27):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], b0[i-20], b1[i-20]))
        lead_time += 3

    return recovery_data


def main():
    #  Training data
    speed_wind_forecast_training = get_data.forecast_data()
    speed_wind_observation_training = get_data.observation_data()
    winter_forecast_training, spring_forecast_training, summer_forecast_training, autumn_forecast_training\
        = separation_of_data_by_seasons(speed_wind_forecast_training)
    winter_observation_training, spring_observation_training, summer_observation_training, autumn_observation_training \
        = separation_of_data_by_seasons(speed_wind_observation_training)

    lead_time_forecast_winter_training = separation_data_by_lead_time_forecast(winter_forecast_training)
    lead_time_forecast_spring_training = separation_data_by_lead_time_forecast(spring_forecast_training)
    lead_time_forecast_summer_training = separation_data_by_lead_time_forecast(summer_forecast_training)
    lead_time_forecast_autumn_training = separation_data_by_lead_time_forecast(autumn_forecast_training)

    lead_time_observation_winter_training = separation_data_by_lead_time_observation(winter_observation_training)
    lead_time_observation_spring_training = separation_data_by_lead_time_observation(spring_observation_training)
    lead_time_observation_summer_training = separation_data_by_lead_time_observation(summer_observation_training)
    lead_time_observation_autumn_training = separation_data_by_lead_time_observation(autumn_observation_training)

    #  Test data
    current_file = "/home/kirill/Downloads/Data/gfs/forecast_for_point_data_"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_forecast_test = file_reader.values.tolist()
    
    current_file = "/home/kirill/Downloads/Data/АВ6/observation_data_test_hour_by_hour"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_observation_test = file_reader.values.tolist()

    winter_forecast_test, spring_forecast_test, summer_forecast_test, autumn_forecast_test \
        = separation_of_data_by_seasons(speed_wind_forecast_test)
    winter_observation_test, spring_observation_test, summer_observation_test, autumn_observation_test \
        = separation_of_data_by_seasons(speed_wind_observation_test)

    lead_time_forecast_winter_test = separation_data_by_lead_time_forecast(winter_forecast_test)
    lead_time_forecast_spring_test = separation_data_by_lead_time_forecast(spring_forecast_test)
    lead_time_forecast_summer_test = separation_data_by_lead_time_forecast(summer_forecast_test)
    lead_time_forecast_autumn_test = separation_data_by_lead_time_forecast(autumn_forecast_test)

    lead_time_observation_winter_test = separation_data_by_lead_time_observation(winter_observation_test)
    lead_time_observation_spring_test = separation_data_by_lead_time_observation(spring_observation_test)
    lead_time_observation_summer_test = separation_data_by_lead_time_observation(summer_observation_test)
    lead_time_observation_autumn_test = separation_data_by_lead_time_observation(autumn_observation_test)

    b0_winter, b1_winter = get_correl_coef_regression_for_season('зимнего', lead_time_observation_winter_training,
                                                                 lead_time_forecast_winter_training)
    b0_spring, b1_spring = get_correl_coef_regression_for_season('весеннего', lead_time_observation_spring_training,
                                                                 lead_time_forecast_spring_training)
    b0_summer, b1_summer = get_correl_coef_regression_for_season('летнего', lead_time_observation_summer_training,
                                                                 lead_time_forecast_summer_training)
    b0_autumn, b1_autumn = get_correl_coef_regression_for_season('осеннего', lead_time_observation_autumn_training,
                                                                 lead_time_forecast_autumn_training)

    recovery_data_winter = get_recovery_data_for_season(lead_time_forecast_winter_test, b0_winter, b1_winter)
    recovery_data_spring = get_recovery_data_for_season(lead_time_forecast_spring_test, b0_spring, b1_spring)
    recovery_data_summer = get_recovery_data_for_season(lead_time_forecast_summer_test, b0_summer, b1_summer)
    recovery_data_autumn = get_recovery_data_for_season(lead_time_forecast_autumn_test, b0_autumn, b1_autumn)

    print("Select calculation number:")
    print(10 * " " + "1. Different for recovered data")
    print(10 * " " + "2. Absolute for recovered data")
    print(10 * " " + "3. RMSE for recovered data")
    print(10 * " " + "4. correlation coefficient for recovered data")
    estimate = int(input("Calculation number: "))
    if estimate == 1:
        average_diff_recovery_winter = get_diff_for_season_and_lead_time_recovery(recovery_data_winter,
                                                                                  lead_time_observation_winter_test)
        average_diff_recovery_spring = get_diff_for_season_and_lead_time_recovery(recovery_data_spring,
                                                                                  lead_time_observation_spring_test)
        average_diff_recovery_summer = get_diff_for_season_and_lead_time_recovery(recovery_data_summer,
                                                                                  lead_time_observation_summer_test)
        average_diff_recovery_autumn = get_diff_for_season_and_lead_time_recovery(recovery_data_autumn,
                                                                                  lead_time_observation_autumn_test)

        print_average_diff('зимний', average_diff_recovery_winter)
        print_average_diff('весенний', average_diff_recovery_spring)
        print_average_diff('летний', average_diff_recovery_summer)
        print_average_diff('осенний', average_diff_recovery_autumn)

        #plotting.plotting_graph_for_error(average_diff_recovery_winter, 'Зимний период',
        #                                  'Средняя арифметическая погрешность')
        #plotting.plotting_graph_for_error(average_diff_recovery_spring, 'Весенний период',
        #                                  'Средняя арифметическая погрешность')
        #plotting.plotting_graph_for_error(average_diff_recovery_summer, 'Летний период',
        #                                  'Средняя арифметическая погрешность')
        #plotting.plotting_graph_for_error(average_diff_recovery_autumn, 'Осенний период',
        #                                  'Средняя арифметическая погрешность')
        #plt.show()
        return average_diff_recovery_winter, average_diff_recovery_spring, average_diff_recovery_summer, \
               average_diff_recovery_autumn

    if estimate == 2:
        abs_diff_recovery_winter = abs.get_diff_abs_for_season_and_lead_time_recovery(recovery_data_winter,
                                                                                      lead_time_observation_winter_test)
        abs_diff_recovery_spring = abs.get_diff_abs_for_season_and_lead_time_recovery(recovery_data_spring,
                                                                                      lead_time_observation_spring_test)
        abs_diff_recovery_summer = abs.get_diff_abs_for_season_and_lead_time_recovery(recovery_data_summer,
                                                                                      lead_time_observation_summer_test)
        abs_diff_recovery_autumn = abs.get_diff_abs_for_season_and_lead_time_recovery(recovery_data_autumn,
                                                                                      lead_time_observation_autumn_test)

        abs.print_average_diff_abs('зимний', abs_diff_recovery_winter)
        abs.print_average_diff_abs('весенний', abs_diff_recovery_spring)
        abs.print_average_diff_abs('летний', abs_diff_recovery_summer)
        abs.print_average_diff_abs('осенний', abs_diff_recovery_autumn)
        #plotting.plotting_graph_for_error(abs_diff_recovery_winter, 'Зимний период', 'Абсолютная погрешность')
        #plotting.plotting_graph_for_error(abs_diff_recovery_spring, 'Весенний период', 'Абсолютная погрешность')
        #plotting.plotting_graph_for_error(abs_diff_recovery_summer, 'Летний период', 'Абсолютная погрешность')
        #plotting.plotting_graph_for_error(abs_diff_recovery_autumn, 'Осенний период', 'Абсолютная погрешность')
        #plt.show()
        return abs_diff_recovery_winter, abs_diff_recovery_spring, abs_diff_recovery_summer, abs_diff_recovery_autumn

    if estimate == 3:
        rmse_recovery_winter = rmse.get_rmse_for_season_and_lead_time_recovery(recovery_data_winter,
                                                                               lead_time_observation_winter_test)
        rmse_recovery_spring = rmse.get_rmse_for_season_and_lead_time_recovery(recovery_data_spring,
                                                                               lead_time_observation_spring_test)
        rmse_recovery_summer = rmse.get_rmse_for_season_and_lead_time_recovery(recovery_data_summer,
                                                                               lead_time_observation_summer_test)
        rmse_recovery_autumn = rmse.get_rmse_for_season_and_lead_time_recovery(recovery_data_autumn,
                                                                               lead_time_observation_autumn_test)
        rmse.print_average_rmse('зимний', rmse_recovery_winter)
        rmse.print_average_rmse('весенний', rmse_recovery_spring)
        rmse.print_average_rmse('летний', rmse_recovery_summer)
        rmse.print_average_rmse('осенний', rmse_recovery_autumn)
        #plotting.plotting_graph_for_error(rmse_recovery_winter, 'Зимний период', 'Среднеквадратичная погрешность')
        #plotting.plotting_graph_for_error(rmse_recovery_spring, 'Весенний период', 'Среднеквадратичная погрешность')
        #plotting.plotting_graph_for_error(rmse_recovery_summer, 'Летний период', 'Среднеквадратичная погрешность')
        #plotting.plotting_graph_for_error(rmse_recovery_autumn, 'Осенний период', 'Среднеквадратичная погрешность')
        #plt.show()
        return rmse_recovery_winter, rmse_recovery_spring, rmse_recovery_summer, rmse_recovery_autumn

    if estimate == 4:
        correlation_coefficient_recovery_winter = correlation.get_correlation_coefficient_for_season_and_lead_time_recovery(
            recovery_data_winter, lead_time_observation_winter_test)
        correlation_coefficient_recovery_spring = correlation.get_correlation_coefficient_for_season_and_lead_time_recovery(
            recovery_data_spring, lead_time_observation_spring_test)
        correlation_coefficient_recovery_summer = correlation.get_correlation_coefficient_for_season_and_lead_time_recovery(
            recovery_data_summer, lead_time_observation_summer_test)
        correlation_coefficient_recovery_autumn = correlation.get_correlation_coefficient_for_season_and_lead_time_recovery(
            recovery_data_autumn, lead_time_observation_autumn_test)
        correlation.print_correlation_coefficient('зимний', correlation_coefficient_recovery_winter)
        correlation.print_correlation_coefficient('весенний', correlation_coefficient_recovery_spring)
        correlation.print_correlation_coefficient('летний', correlation_coefficient_recovery_summer)
        correlation.print_correlation_coefficient('осенний', correlation_coefficient_recovery_autumn)
        #plotting.plotting_graph_for_error(correlation_coefficient_recovery_winter, 'Зимний период',
                                          #'Коэффициент корреляции')
        #plotting.plotting_graph_for_error(correlation_coefficient_recovery_spring, 'Весенний период',
                                          #'Коэффициент корреляции')
        #plotting.plotting_graph_for_error(correlation_coefficient_recovery_summer, 'Летний период',
                                          #'Коэффициент корреляции')
        #plotting.plotting_graph_for_error(correlation_coefficient_recovery_autumn, 'Осенний период',
                                          #'Коэффициент корреляции')
        #plt.show()
        return correlation_coefficient_recovery_winter, correlation_coefficient_recovery_spring, \
               correlation_coefficient_recovery_spring, correlation_coefficient_recovery_autumn

    plot_data(lead_time_forecast_winter_test, 'Зимний период. Модельные данные за 2018 год', 'blue')
    plot_data(lead_time_forecast_spring_test, 'Весенний период. Модельные данные за 2018 год', 'orange')
    plot_data(lead_time_forecast_summer_test, 'Летний период. Модельные данные за 2018 год', 'green')
    plot_data(lead_time_forecast_autumn_test, 'Осенний период. Модельные данные за 2018 год', 'red')
    plt.legend()
    plt.show()

    plot_data(recovery_data_winter, 'Зимний период. Восстановленные данные за 2018 год', 'blue')
    plot_data(recovery_data_spring, 'Весенний период. Восстановленные данные за 2018 год', 'orange')
    plot_data(recovery_data_summer, 'Летний период. Восстановленные данные за 2018 год', 'green')
    plot_data(recovery_data_autumn, 'Осенний период. Восстановленные данные за 2018 год', 'red')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()


