import math


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
