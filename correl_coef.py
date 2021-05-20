import math
import calc_error


def get_correl_coef_for_season_and_lead_time(lead_time_forecast, lead_time_practical):
    average_diff = []
    lead_time = 0
    for predictive, practical in zip(lead_time_forecast[0: 8], lead_time_practical):
        average_diff.append(
            [lead_time, calc_correl_coef(calc_error.get_need_data(predictive), calc_error.get_need_data(practical))])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[8: 16], lead_time_practical):
        average_diff.append([lead_time, calc_correl_coef(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[16: 24], lead_time_practical):
        average_diff.append([lead_time, calc_correl_coef(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[24:27], lead_time_practical[0:3]):
        average_diff.append([lead_time, calc_correl_coef(calc_error.get_need_data(predictive), practical)])
        lead_time += 3

    return average_diff


def print_correl_coef(season, correl_coef):
    for i in range(0, len(correl_coef)):
        print(f'Коэффициент корреляции {season} за период и заблаговременность {correl_coef[i][0]}: {correl_coef[i][1]}')
    print('\n')


def calc_correl_coef(speed_wind_predictive, speed_wind_practical):
    x_avg = 0
    y_avg = 0

    if len(speed_wind_predictive) < len(speed_wind_practical):
        lenght = int(len(speed_wind_predictive))
    elif len(speed_wind_practical) < len(speed_wind_predictive):
        lenght = int(len(speed_wind_practical))
    else:
        lenght = int(len(speed_wind_predictive))


    for i in range(0, lenght):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            x_avg += speed_wind_practical[i][1]
            y_avg += speed_wind_predictive[i][1]
    x_avg /= lenght
    y_avg /= lenght

    numerator = 0
    x = 0
    y = 0
    for i in range(0, lenght):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            numerator += (speed_wind_practical[i][1] - x_avg)*(speed_wind_predictive[i][1] - y_avg)
            x += (speed_wind_practical[i][1] - x_avg)**2
            y += (speed_wind_predictive[i][1] - y_avg)**2
    denominator = math.sqrt(x*y)
    correl_coef = numerator / denominator

    return correl_coef
