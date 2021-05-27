import math
import get_data


def get_diff_abs_for_season_and_lead_time(lead_time_forecast, lead_time_observation):
    average_diff = []
    lead_time = 0
    for forecast, observation in zip(lead_time_forecast[0: 8], lead_time_observation):
        average_diff.append(
            [lead_time, calc_abs(get_data.get_date_and_speed(forecast), get_data.get_date_and_speed(observation))])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[8: 16], lead_time_observation):
        average_diff.append([lead_time, calc_abs(get_data.get_date_and_speed(forecast), observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[16: 24], lead_time_observation):
        average_diff.append([lead_time, calc_abs(get_data.get_date_and_speed(forecast), observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[24:27], lead_time_observation[0:3]):
        average_diff.append([lead_time, calc_abs(get_data.get_date_and_speed(forecast), observation)])
        lead_time += 3

    return average_diff


def print_average_diff_abs(season, average_diff):
    for i in range(0, len(average_diff)):
        print(f'Абсолютная погрешность {season} за период и заблаговременность {average_diff[i][0]}: '
              f'{average_diff[i][1]}')
    print('\n')


def calc_abs_diff(speed_wind_forecast, speed_wind_observation):
    diff = []

    if len(speed_wind_forecast) < len(speed_wind_observation):
        length = len(speed_wind_forecast)
    elif len(speed_wind_observation) < len(speed_wind_forecast):
        length = len(speed_wind_observation)
    else:
        length = int(len(speed_wind_forecast))

    for i in range(0, length):
        diff1 = [speed_wind_observation[i][0]]
        for j in range(1, len(speed_wind_forecast[i])):
            if float(speed_wind_forecast[i][j]) >= 9999 or math.isnan(float(speed_wind_observation[i][j])):
                continue
            else:
                diff1.append(math.fabs(speed_wind_observation[i][j] - speed_wind_forecast[i][j]))
        diff.append(diff1)
    return diff


def calc_abs(forecast_data, observation_data):
    diff_lead_time = calc_abs_diff(forecast_data, observation_data)
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        if len(diff_lead_time[i]) > 1:
            average_diff += diff_lead_time[i][1]
    average_diff = average_diff / len(diff_lead_time)
    return average_diff


def calc_abs_diff_for_recovery_data(recovery_data_forecast, observation_data):
    diff = []
    for i in range(0, len(recovery_data_forecast)):
        if math.isnan(float(observation_data[i])):
            pass
        else:
            diff.append(math.fabs(observation_data[i] - recovery_data_forecast[i][0]))

    return diff


def calc_abs_recovery_data(recovery_data_forecast, observation_data):
    diff_lead_time = calc_abs_diff_for_recovery_data(recovery_data_forecast, observation_data)
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        average_diff += diff_lead_time[i]
    average_diff = average_diff / len(diff_lead_time)
    return average_diff


def get_diff_abs_for_season_and_lead_time_recovery(lead_time_forecast_recovery, lead_time_observation):
    average_diff = []
    lead_time = 0
    for forecast, observation in zip(lead_time_forecast_recovery[0:8], lead_time_observation):
        average_diff.append([lead_time, calc_abs_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[8:16], lead_time_observation):
        average_diff.append([lead_time, calc_abs_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[16:24], lead_time_observation):
        average_diff.append([lead_time, calc_abs_recovery_data(forecast, observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast_recovery[24:27], lead_time_observation[0:3]):
        average_diff.append([lead_time, calc_abs_recovery_data(forecast, observation)])
        lead_time += 3

    return average_diff
