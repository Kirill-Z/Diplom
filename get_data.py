import forecast
import observation
import pandas as pd


def get_date_and_speed(data):
    """Cleansing data from unnecessary values."""
    for i in range(0, len(data)):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]
    return data


def get_data_from_file(module_name, directory, filename, choice_area_or_point=None, choice_model=None):
    print('Choose a way to get data:')
    print(10 * ' ' + '1. Calculate data')
    print(10 * ' ' + 'Press Enter. Get data from file')
    choice_num = input('Desired value: ')
    print('\n')
    if choice_num == '1':
        module_name.main(choice_area_or_point, choice_model)
    current_file = '/home/kirill/Downloads/Data/' + directory + '/' + filename  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python', usecols=[0, 1, 2, 3, 4, 5, 6])
    speed_wind = file_reader.values.tolist()

    return speed_wind


def forecast_data():
    print('Model COSMO or GFS:')
    print(10 * ' ' + '1. COSMO')
    print(10 * ' ' + '2. GFS')
    choice_model = input('Model number: ')
    choice_num = 0
    if choice_model == '1':
        speed_wind_forecast = get_data_from_file(forecast, 'cosmo_data', 'forecast_for_point_data_training_cosmo', choice_num, choice_model)
    elif choice_model == '2':
        print('Forecast data:')
        print(10 * ' ' + '1. Data for the point')
        print(10 * ' ' + '2. Data for the 5 points')
        choice_num = input('Desired value: ')
        print('\n')
        if choice_num == '1':
            speed_wind_forecast = get_data_from_file(forecast, 'gfs', 'forecast_for_point_data_training', choice_num, choice_model)
        elif choice_num == '2':
            speed_wind_forecast = get_data_from_file(forecast, 'gfs', 'forecast_for_five_point_data_training', choice_num, choice_model)
    else:
        print('Unknown command, please re-enter')
        speed_wind_forecast, choice_num = forecast_data()

    return speed_wind_forecast, choice_num


def observation_data():
    print('Observation data:')
    print(10 * ' ' + '1. Data hour per hour')
    print(10 * ' ' + '2. Data in the time range (+ -30 minutes)')
    print(10 * ' ' + '3. Data in the time range (+ -30 minutes), taking into account every minute')
    choice_num = input('Desired value: ')
    print('\n')
    if choice_num == '1':
        speed_wind_observation = get_data_from_file(observation, 'АВ6', 'observation_data_training_hour_by_hour')
    elif choice_num == '2':
        speed_wind_observation = get_data_from_file(observation, 'АВ6', 'observation_data_training_time_range')
    elif choice_num == '3':
        speed_wind_observation = get_data_from_file(observation, 'АВ6',
                                                    'observation_data_training_time_range_with_every_minute')
    else:
        print('Unknown command, please re-enter')
        speed_wind_observation, choice_num = observation_data()

    return speed_wind_observation, choice_num
