import wind_forecast
import observation_wind
import pandas as pd


def get_date_and_speed(data):
    for i in range(0, len(data)):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]
    return data


def get_data_from_file(module_name, directory, filename, choice_num):
    tmp = input(
        'Press 1 if you want to calculate observation choice_nums or press enter if you want get data from file: ')
    if tmp == '1':
        module_name.main(choice_num)
    current_file = '/home/kirill/Downloads/Data/' + directory + '/' + filename  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python', usecols=[0, 1, 2, 3, 4, 5, 6])
    speed_wind = file_reader.values.tolist()

    return speed_wind


def forecast_data():
    choice_num = input(
        'Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ')
    if choice_num == '1':
        speed_wind_forecast = get_data_from_file(wind_forecast, 'gfs', 'forecast_for_point_data', choice_num)
    elif choice_num == '2':
        speed_wind_forecast = get_data_from_file(wind_forecast, 'gfs', 'forecast_for_area_data', choice_num)
    else:
        print('Unknown command, please re-enter')
        speed_wind_forecast = forecast_data()

    return speed_wind_forecast


def observation_data():
    choice_num = input(
        'Observation data: If you need to calculate a point, press 1, if you need to calculate an area, press 2 or 3: ')
    if choice_num == '1':
        speed_wind_observation = get_data_from_file(observation_wind, 'АВ6', 'observation_data_training_hour_by_hour',
                                                    choice_num)
    elif choice_num == '2':
        speed_wind_observation = get_data_from_file(observation_wind, 'АВ6', 'observation_data_training_time_range',
                                                    choice_num)
    elif choice_num == '3':
        speed_wind_observation = get_data_from_file(observation_wind, 'АВ6',
                                                    'observation_data_training_time_range_with_every_minute',
                                                    choice_num)
    else:
        print('Unknown command, please re-enter')
        speed_wind_observation = observation_data()

    return speed_wind_observation
