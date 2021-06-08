import math


def get_rmse_for_season_and_lead_time(lead_time_forecast, lead_time_practical):
    average_diff = []
    lead_time = 0
    for predictive, practical in zip(lead_time_forecast[0: 8], lead_time_practical):
        average_diff.append(
            [lead_time, calc_rmse(predictive, practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[8: 16], lead_time_practical):
        average_diff.append([lead_time, calc_rmse(predictive, practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[16: 24], lead_time_practical):
        average_diff.append([lead_time, calc_rmse(predictive, practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[24:27], lead_time_practical[0:3]):
        average_diff.append([lead_time, calc_rmse(predictive, practical)])
        lead_time += 3

    return average_diff


def print_average_rmse(season, rmse):
    for i in range(0, len(rmse)):
        print(f'Средняя квадратическая погрешность {season} за период и заблаговременность {rmse[i][0]}: {rmse[i][1]}')
    print('\n')


def calc_squared_difference(speed_wind_predictive, speed_wind_practical):
    diff = []

    if len(speed_wind_predictive) <= len(speed_wind_practical):
        length = len(speed_wind_predictive)
    elif len(speed_wind_practical) < len(speed_wind_predictive):
        length = len(speed_wind_practical)
    else:
        length = len(speed_wind_predictive)

    for i in range(0, length):
        if float(speed_wind_predictive[i]) >= 50 or math.isnan(float(speed_wind_practical[i])):
            continue
        else:
            diff.append((speed_wind_practical[i] - speed_wind_predictive[i]) ** 2)
    return diff


def calc_rmse(predictive_data, practical_data):
    diff_lead_time = calc_squared_difference(predictive_data, practical_data)
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        average_diff += diff_lead_time[i]
    average_diff = math.sqrt(average_diff / len(diff_lead_time))
    return average_diff


def calc_squaared_diff_for_recovery_data(recovery_data_forecast, observation_data):
    diff = []
    for i in range(0, len(recovery_data_forecast)):
        if float(recovery_data_forecast[i][0]) >= 50 or math.isnan(float(observation_data[i])):
            pass
        else:
            diff.append((observation_data[i] - recovery_data_forecast[i][0]) ** 2)

    return diff


def calc_rmse_for_recovery_data(recovery_data_forecast, observation_data):
    diff_lead_time = calc_squaared_diff_for_recovery_data(recovery_data_forecast, observation_data)
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        average_diff += diff_lead_time[i]
    average_diff = math.sqrt(average_diff / len(diff_lead_time))
    return average_diff


def get_rmse_for_season_and_lead_time_recovery(lead_time_forecast_recovery, lead_time_observation):
    average_diff = []
    lead_time = 0
    for forecast, observation in zip(lead_time_forecast_recovery[0:8], lead_time_observation):
        average_diff.append([lead_time, calc_rmse_for_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[8:16], lead_time_observation):
        average_diff.append([lead_time, calc_rmse_for_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[16:24], lead_time_observation):
        average_diff.append([lead_time, calc_rmse_for_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[24:27], lead_time_observation[0:3]):
        average_diff.append([lead_time, calc_rmse_for_recovery_data(forecast, observation)])
        lead_time += 3

    return average_diff