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


    b0_winter = []
    b1_winter = []
    b0_spring = []
    b1_spring = []
    b0_summer = []
    b1_summer = []
    b0_autumn = []
    b1_autumn = []

    print(10 * ' ' + 'Коэффициенты для зимнего периода')
    lead_time = 0
    for i in range(0, 8):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_winter_training[i], lead_time_forecast_winter_training[i])
        b0_winter.append(b0)
        b1_winter.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    for i in range(8, 10):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_winter_training[i - 8], lead_time_forecast_winter_training[i])
        b0_winter.append(b0)
        b1_winter.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    print(10 * ' ' + 'Коэффициенты для весеннего периода')
    lead_time = 0
    for i in range(0, 8):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_spring_training[i], lead_time_forecast_spring_training[i])
        b0_spring.append(b0)
        b1_spring.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    for i in range(8, 10):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_spring_training[i - 8], lead_time_forecast_spring_training[i])
        b0_spring.append(b0)
        b1_spring.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    print(10 * ' ' + 'Коэффициенты для летнего периода')
    lead_time = 0
    for i in range(0, 8):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_summer_training[i], lead_time_forecast_summer_training[i])
        b0_summer.append(b0)
        b1_summer.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    for i in range(8, 10):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_summer_training[i - 8], lead_time_forecast_summer_training[i])
        b0_summer.append(b0)
        b1_summer.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    print(10 * ' ' + 'Коэффициенты для осеннего периода')
    lead_time = 0
    for i in range(0, 8):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_autumn_training[i], lead_time_forecast_autumn_training[i])
        b0_autumn.append(b0)
        b1_autumn.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    for i in range(8, 10):
        b0, b1 = get_coefficient_for_linear_regression(lead_time_observation_autumn_training[i - 8], lead_time_forecast_autumn_training[i])
        b0_autumn.append(b0)
        b1_autumn.append(b1)
        print(f'Отрезок для заблаговременности {lead_time}: {b0}')
        print(f'Наклон для заблаговременности {lead_time}: {b1}\n')
        lead_time += 3

    # Winter
    recovered_data_winter = []
    lead_time = 0
    for i in range(0, 8):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i], b0_winter[i],
                          b1_winter[i], lead_time, 'Зимний период'))
        lead_time += 3
    for i in range(8, 10):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-8], b0_winter[i],
                          b1_winter[i], lead_time, 'Зимний период'))
        lead_time += 3
    for i in range(10, 18):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-10], b0_winter[i-10],
                            b1_winter[i-10], lead_time, 'Зимний период'))
        lead_time += 3
    for i in range(18, 20):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-16], b0_winter[i-10],
                          b1_winter[i-10], lead_time, 'Зимний период'))
        lead_time += 3
    for i in range(20, 24):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i - 16],
                            b0_winter[i - 20], b1_winter[i - 20], lead_time, 'Зимний период'))
        lead_time += 3
    for i in range(24, 27):
        recovered_data_winter.append(linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i - 24],
                            b0_winter[i - 20], b1_winter[i - 20], lead_time, 'Зимний период'))
        lead_time += 3

    # Spring
    recovery_data_spring = []
    lead_time = 0
    for i in range(0, 8):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i], b0_spring[i],
                          b1_spring[i], lead_time, 'Весенний период'))
        lead_time += 3
    for i in range(8, 10):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 8], b0_spring[i],
                          b1_spring[i], lead_time, 'Весенний период'))
        lead_time += 3
    for i in range(10, 18):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 10],
                          b0_spring[i - 10], b1_spring[i - 10], lead_time, 'Весенний период'))
        lead_time += 3
    for i in range(18, 20):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 16],
                          b0_spring[i - 10], b1_spring[i - 10], lead_time, 'Весенний период'))
        lead_time += 3
    for i in range(20, 24):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 16],
                          b0_spring[i - 20], b1_spring[i - 20], lead_time, 'Весенний период'))
        lead_time += 3
    for i in range(24, 27):
        recovery_data_spring.append(linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 24],
                          b0_spring[i - 20], b1_spring[i - 20], lead_time, 'Весенний период'))
        lead_time += 3

    # Summer
    recovery_data_summer = []
    lead_time = 0
    for i in range(0, 8):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i], b0_summer[i],
                            b1_summer[i], lead_time, 'Летний период'))
        lead_time += 3
    for i in range(8, 10):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 8], b0_summer[i],
                            b1_summer[i], lead_time, 'Летний период'))
        lead_time += 3
    for i in range(10, 18):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 10],
                            b0_summer[i - 10], b1_summer[i - 10], lead_time, 'Летний период'))
        lead_time += 3
    for i in range(18, 20):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 16],
                            b0_summer[i - 10], b1_summer[i - 10], lead_time, 'Летний период'))
        lead_time += 3
    for i in range(20, 24):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 16],
                            b0_summer[i - 20], b1_summer[i - 20], lead_time, 'Летний период'))
        lead_time += 3
    for i in range(24, 27):
        recovery_data_summer.append(linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 24],
                            b0_summer[i - 20], b1_summer[i - 20], lead_time, 'Летний период'))
        lead_time += 3

    # Autumn
    recovery_data_autumn = []
    lead_time = 0
    for i in range(0, 8):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i], b0_autumn[i],
                          b1_autumn[i], lead_time, 'Осенний период'))
        lead_time += 3
    for i in range(8, 10):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 8], b0_autumn[i],
                          b1_autumn[i], lead_time, 'Осенний период'))
        lead_time += 3
    for i in range(10, 18):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 10],
                          b0_autumn[i - 10], b1_autumn[i - 10], lead_time, 'Осенний период'))
        lead_time += 3
    for i in range(18, 20):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 16],
                          b0_autumn[i - 10], b1_autumn[i - 10], lead_time, 'Осенний период'))
        lead_time += 3
    for i in range(20, 24):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 16],
                          b0_autumn[i - 20], b1_autumn[i - 20], lead_time, 'Осенний период'))
        lead_time += 3
    for i in range(24, 27):
        recovery_data_autumn.append(linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 24],
                          b0_autumn[i - 20], b1_autumn[i - 20], lead_time, 'Осенний период'))
        lead_time += 3

    average_diff_recovery_winter = get_diff_for_season_and_lead_time_recovery(recovered_data_winter,
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
    for i in range(0, len(lead_time_forecast_winter_test)):
        for j in range(0, len(lead_time_forecast_winter_test[i])):
            if (i == 0 and j == 0):
                plt.scatter(i * 3, lead_time_forecast_winter_test[i][j], c='blue',
                            label='Зимний период. Модельные данные за 2018 год')
            else:
                plt.scatter(i * 3, lead_time_forecast_winter_test[i][j], c='blue')
            
    for i in range(0, len(lead_time_forecast_spring_test)):
        for j in range(0, len(lead_time_forecast_spring_test[i])):
            if (i == 0 and j == 0):
                plt.scatter(i*3, lead_time_forecast_spring_test[i][j], c='orange',
                            label='Весенний период. Модельные данные за 2018 год')
            else:
                plt.scatter(i*3, lead_time_forecast_spring_test[i][j], c='orange')

    for i in range(0, len(lead_time_forecast_summer_test)):
        for j in range(0, len(lead_time_forecast_summer_test[i])):
            if (i == 0 and j == 0):
                plt.scatter(i*3, lead_time_forecast_summer_test[i][j], c='green',
                            label='Летний период. Модельные данные за 2018 год')
            else:
                plt.scatter(i*3, lead_time_forecast_summer_test[i][j], c='green')

    for i in range(0, len(lead_time_forecast_autumn_test)):
        for j in range(0, len(lead_time_forecast_autumn_test[i])):
            if (i == 0 and j == 0):
                plt.scatter(i*3, lead_time_forecast_autumn_test[i][j], c='red',
                            label='Осенний период. Модельные данные за 2018 год')
            else:
                plt.scatter(i*3, lead_time_forecast_autumn_test[i][j], c='red')
    plt.legend()
    plt.show()

    for i in range(0, len(recovered_data_winter)):
        for j in range(0, len(recovered_data_winter[i])):
            if (i == 0 and j == 0):
                plt.scatter(i * 3, recovered_data_winter[i][j], c='blue',
                        label='Зимний период. Восстановленные данные за 2018 год')
            else:
                plt.scatter(i * 3, recovered_data_winter[i][j], c='blue')

    for i in range(0, len(recovery_data_spring)):
        for j in range(0, len(recovery_data_spring[i])):
            if (i == 0 and j == 0):
                plt.scatter(i * 3, recovery_data_spring[i][j], c='orange',
                        label='Весенний период. Восстановленные данные за 2018 год')
            else:
                plt.scatter(i * 3, recovery_data_spring[i][j], c='orange')

    for i in range(0, len(recovery_data_summer)):
        for j in range(0, len(recovery_data_summer[i])):
            if (i == 0 and j == 0):
                plt.scatter(i * 3, recovery_data_summer[i][j], c='green',
                        label='Летний период. Восстановленные данные за 2018 год')
            else:
                plt.scatter(i * 3, recovery_data_summer[i][j], c='green')

    for i in range(0, len(recovery_data_autumn)):
        for j in range(0, len(recovery_data_autumn[i])):
            if (i == 0 and j == 0):
                plt.scatter(i * 3, recovery_data_autumn[i][j], c='red',
                        label='Осенний период. Восстановленные данные за 2018 год')
            else:
                plt.scatter(i * 3, recovery_data_autumn[i][j], c='red')
    plt.legend()
    plt.show()


main()
