import math
import calc_error


def get_diff_for_season_and_lead_time(lead_time_forecast, lead_time_practical):
    average_diff = []
    lead_time = 0
    for predictive, practical in zip(lead_time_forecast[0: 8], lead_time_practical):
        average_diff.append(
            [lead_time, calc_the_average_diff(calc_error.get_need_data(predictive), calc_error.get_need_data(practical))])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[8: 16], lead_time_practical):
        average_diff.append([lead_time, calc_the_average_diff(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[16: 24], lead_time_practical):
        average_diff.append([lead_time,calc_the_average_diff(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[24:27], lead_time_practical[0:3]):
        average_diff.append([lead_time, calc_the_average_diff(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    return average_diff


def print_average_diff(season, average_diff):
    for i in range(0, len(average_diff)):
        print(f'Средняя разность {season} за период и заблаговременность {average_diff[i][0]}: {average_diff[i][1]}')
    print('\n')


def calc_diff(speed_wind_predictive, speed_wind_practical):
    diff = []

    if len(speed_wind_predictive) <= len(speed_wind_practical):
        length = len(speed_wind_predictive)
    elif len(speed_wind_practical) < len(speed_wind_predictive):
        length = len(speed_wind_practical)

    for i in range(0, length):
        diff1 = [speed_wind_practical[i][0]]
        for j in range(1, len(speed_wind_predictive[i])):
            if float(speed_wind_predictive[i][j]) >= 9999 or math.isnan(float(speed_wind_practical[i][j])):
                continue
            else:
                diff1.append(speed_wind_practical[i][j] - speed_wind_predictive[i][j])
        diff.append(diff1)
    return diff


def calc_the_average_diff(predictive_data, practical_data):
    diff_lead_time = calc_diff(predictive_data, practical_data)
    average_diff = 0
    for i in range(0, len(diff_lead_time)):
        if len(diff_lead_time[i]) > 1:
            average_diff += diff_lead_time[i][1]
    average_diff = average_diff / len(diff_lead_time)
    return average_diff
