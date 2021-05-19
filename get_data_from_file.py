import wind_forecast
import practical_wind_forecast
import pandas as pd


def forecast_data():
    tmp = input('Press 1 if you want to calculate forecast values: ')
    if tmp == "1":
        value = input(
            "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
        if value == '1':
            wind_forecast.main(value)
        elif value == '2':
            wind_forecast.main(value)

    current_file = "/home/kirill/Downloads/Data/gfs/list_data_by_season"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_predictive = file_reader.values.tolist()
    return speed_wind_predictive


def observation_data():
    tmp = input('Press 1 if you want to calculate observation values: ')
    if tmp == "1":
        value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
                      "press 2 or 3: ")
        if value == '1':
            practical_wind_forecast.main(value)
        elif value == '2':
            practical_wind_forecast.main(value)
        elif value == '3':
            practical_wind_forecast.main(value)

    current_file = "/home/kirill/Downloads/Data/АВ6/practical_data_training"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_practical = file_reader.values.tolist()
    return speed_wind_practical
