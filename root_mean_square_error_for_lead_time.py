import math


def calc_squared_difference(lead_time, diff_num_lead_time, speed_wind_predictive_true, speed_wind_practical, i, j):
    if speed_wind_predictive_true[i][j][0][11:13] == lead_time:
        if i + j * 8 < (len(speed_wind_practical) - 1):
            if speed_wind_predictive_true[i][j][3] == int(speed_wind_practical[i + j * 8][3]):
                if float(speed_wind_predictive_true[i][j][5]) >= 9999 or math.isnan(float(speed_wind_practical[i + j * 8][5])):
                    pass
                else:
                    diff_num_lead_time.append((float(speed_wind_practical[i + j * 8][5]) - float(speed_wind_predictive_true[i][j][5]))**2)

    return diff_num_lead_time


def calc_rmse(diff_lead_time):
    average_diff: int = 0
    for i in range(1, len(diff_lead_time), 2):
        average_diff += diff_lead_time[i]

    average_diff = math.sqrt(average_diff / len(diff_lead_time))
    return average_diff


def print_rmse(hour: str, average_diff):
    print(f'Среднеквадратичная ошибка для заблаговременности {hour}' + f': {average_diff}')
