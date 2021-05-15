import math


def cacl_abs_diff(speed_wind_predictive, speed_wind_practical):
    diff = []

    if speed_wind_predictive < speed_wind_practical:
        lenght_ = int(len(speed_wind_predictive))
    elif speed_wind_practical < speed_wind_predictive:
        lenght = int(len(speed_wind_practical))

    for i in range(0, lenght):
        diff1 = [speed_wind_practical[i][0]]
        for j in range(1, len(speed_wind_predictive[i])):
            if float(speed_wind_predictive[i][j]) >= 9999 or math.isnan(float(speed_wind_practical[i][j])):
                continue
            else:
                diff1.append(math.fabs(speed_wind_practical[i][j] - speed_wind_predictive[i][j]))
        diff.append(diff1)
    return diff


def calc_abs(diff_season):
    average_diff = 0
    for i in range(0, len(diff_season)):
        if len(diff_season[i]) > 1:
            average_diff += diff_season[i][1]
    average_diff = average_diff / len(diff_season)
    return average_diff
