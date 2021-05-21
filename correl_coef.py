import math
import get_data


def get_correlation_coefficient_for_season_and_lead_time(lead_time_forecast, lead_time_observation):
    average_diff = []
    lead_time = 0
    for forecast, observation in zip(lead_time_forecast[0: 8], lead_time_observation):
        average_diff.append(
            [lead_time, calc_correlation_coefficient(get_data.get_date_and_speed(forecast),
                                                     get_data.get_date_and_speed(observation))])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[8: 16], lead_time_observation):
        average_diff.append([lead_time, calc_correlation_coefficient(get_data.get_date_and_speed(forecast),
                                                                     observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[16: 24], lead_time_observation):
        average_diff.append([lead_time, calc_correlation_coefficient(get_data.get_date_and_speed(forecast),
                                                                     observation)])
        lead_time += 3

    for forecast, observation in zip(lead_time_forecast[24:27], lead_time_observation[0:3]):
        average_diff.append([lead_time, calc_correlation_coefficient(get_data.get_date_and_speed(forecast),
                                                                     observation)])
        lead_time += 3

    return average_diff


def print_correlation_coefficient(season, correlation_coefficient):
    for i in range(0, len(correlation_coefficient)):
        print(f'Коэффициент корреляции {season} за период и заблаговременность {correlation_coefficient[i][0]}: '
              f'{correlation_coefficient[i][1]}')
    print('\n')


def calc_correlation_coefficient(speed_wind_forecast, speed_wind_observation):
    x_avg = 0
    y_avg = 0

    if len(speed_wind_forecast) < len(speed_wind_observation):
        length = int(len(speed_wind_forecast))
    elif len(speed_wind_observation) < len(speed_wind_forecast):
        length = int(len(speed_wind_observation))
    else:
        length = int(len(speed_wind_forecast))

    for i in range(0, length):
        if float(speed_wind_forecast[i][1]) >= 9999 or math.isnan(float(speed_wind_observation[i][1])):
            continue
        else:
            x_avg += speed_wind_observation[i][1]
            y_avg += speed_wind_forecast[i][1]
    x_avg /= length
    y_avg /= length

    numerator = 0
    x = 0
    y = 0
    for i in range(0, length):
        if float(speed_wind_forecast[i][1]) >= 9999 or math.isnan(float(speed_wind_observation[i][1])):
            continue
        else:
            numerator += (speed_wind_observation[i][1] - x_avg)*(speed_wind_forecast[i][1] - y_avg)
            x += (speed_wind_observation[i][1] - x_avg)**2
            y += (speed_wind_forecast[i][1] - y_avg)**2
    denominator = math.sqrt(x*y)
    correlation_coefficient = numerator / denominator

    return correlation_coefficient
