import wind_forecast
import practical_wind
import pandas as pd


def get_data_from_file(module_name, directory, filename, value):
    tmp = input('Press 1 if you want to calculate observation values or press enter if you want get data from file: ')
    if tmp == "1":
        module_name.main(value)
    current_file = "/home/kirill/Downloads/Data/" + directory + "/" + filename  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python', usecols=[0, 1, 2, 3, 4, 5, 6])
    speed_wind = file_reader.values.tolist()

    return speed_wind


def forecast_data():
    value = input(
        "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
    if value == '1':
        speed_wind_predictive = get_data_from_file(wind_forecast, 'gfs', 'list_data_with_point', value)
    elif value == '2':
        speed_wind_predictive = get_data_from_file(wind_forecast, 'gfs', 'list_data_by_with_area', value)

    return speed_wind_predictive


def observation_data():
    value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
                  "press 2 or 3: ")
    if value == '1':
        speed_wind_practical = get_data_from_file(practical_wind, 'АВ6', 'practical_data_training_hour_by_hour', value)
    elif value == '2':
        speed_wind_practical = get_data_from_file(practical_wind, 'АВ6', 'practical_data_training_time_range', value)
    elif value == '3':
        speed_wind_practical = get_data_from_file(practical_wind, 'АВ6',
                                                  'practical_data_training_time_range_with_every_minute', value)

    return speed_wind_practical
