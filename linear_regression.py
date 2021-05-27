import numpy as np
import pylab as pl
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import get_data
import pandas as pd
import math
from calc_error import separation_of_data_by_seasons, separation_data_by_lead_time_forecast, \
                       separation_data_by_lead_time_observation
from difference import get_diff_for_season_and_lead_time_recovery, print_average_diff
import plotting


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

    model = LinearRegression().fit(x[0:length_array], y[0:length_array])
    coefficient = [model.intercept_, model.coef_]
    return coefficient


def linear_regression(forecast_test, observation_test, b0, b1, lead_time, season):
    observation_test = np.array(observation_test).reshape((-1, 1))
    forecast_test = np.array(forecast_test).reshape((-1, 1))
    y_pred = b0 + b1 * forecast_test
    #plt.scatter(observation_test, forecast_test, color='red')
    #plt.title(season)
    #plt.xlabel('Предиктант')
    #plt.ylabel('Предиктор')
    #plt.plot(observation_test, y_pred, label=f'Заблаговременность {lead_time}')
    #plt.legend()
    #plt.show()

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


def get_recovery_data_for_season(lead_time_forecast_season, lead_time_observation_season, b0, b1, season):
    recovery_data = []
    lead_time = 0
    for i in range(0, 8):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i],
                                                b0[i], b1[i], lead_time, season))
        lead_time += 3
    for i in range(8, 10):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i - 8],
                                                b0[i], b1[i], lead_time, season))
        lead_time += 3
    for i in range(10, 18):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i - 10],
                                                b0[i - 10], b1[i - 10], lead_time, season))
        lead_time += 3
    for i in range(18, 20):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i - 16],
                                                b0[i - 10], b1[i - 10], lead_time, season))
        lead_time += 3
    for i in range(20, 24):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i - 16],
                                                b0[i - 20], b1[i - 20], lead_time, season))
        lead_time += 3
    for i in range(24, 27):
        recovery_data.append(linear_regression(lead_time_forecast_season[i], lead_time_observation_season[i - 24],
                                                b0[i - 20], b1[i - 20], lead_time, season))
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

    recovery_data_winter = get_recovery_data_for_season(lead_time_forecast_winter_test,
                                                        lead_time_observation_winter_test, b0_winter, b1_winter,
                                                        'Зимний период')
    recovery_data_spring = get_recovery_data_for_season(lead_time_forecast_spring_test,
                                                        lead_time_observation_spring_test, b0_spring, b1_spring,
                                                        'Весенний период')
    recovery_data_summer = get_recovery_data_for_season(lead_time_forecast_summer_test,
                                                        lead_time_observation_summer_test, b0_summer, b1_summer,
                                                        'Летний период')
    recovery_data_autumn = get_recovery_data_for_season(lead_time_forecast_autumn_test,
                                                        lead_time_observation_autumn_test, b0_autumn, b1_autumn,
                                                        'Осенний период')

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

    plotting.plotting_graph_for_error(average_diff_recovery_winter, 'Зимний период', 'Средняя арифметическая погрешность')
    plotting.plotting_graph_for_error(average_diff_recovery_spring, 'Весенний период', 'Средняя арифметическая погрешность')
    plotting.plotting_graph_for_error(average_diff_recovery_summer, 'Летний период', 'Средняя арифметическая погрешность')
    plotting.plotting_graph_for_error(average_diff_recovery_autumn, 'Осенний период', 'Средняя арифметическая погрешность')

    plt.show()


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


main()
