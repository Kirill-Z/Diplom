import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import get_data
import pandas as pd
from calc_error import separation_of_data_by_seasons, separation_data_by_lead_time_forecast, \
                       separation_data_by_lead_time_observation


def write_in_speed_forecast(lead_time: str, speed_wind_forecast):
    local_speed_wind = []
    for i in range(0, len(speed_wind_forecast)):
        if speed_wind_forecast[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_forecast[i])
    return local_speed_wind


def linear_regression(predictant, predictor, forecast_test, observation_test):

    x = np.array(predictant).reshape((-1, 1))
    y = np.array(predictor).reshape((-1, 1))
    observation_test = np.array(observation_test).reshape((-1, 1))
    forecast_test = np.array(forecast_test).reshape((-1, 1))
    model = LinearRegression().fit(x, y)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    y_pred = model.predict(observation_test)
    plt.scatter(observation_test, forecast_test, color='gray')
    plt.plot(observation_test, y_pred)
    plt.show()


def main():
    #  Training data
    speed_wind_forecast_training = get_data.forecast_data()
    speed_wind_observation_training = get_data.observation_data()

    winter_forecast_training, spring_forecast_training, summer_forecast_training, autumn_forecast_training \
        = separation_of_data_by_seasons(speed_wind_forecast_training)

    lead_time_forecast_winter_training = separation_data_by_lead_time_forecast(winter_forecast_training)
    lead_time_forecast_spring_training = separation_data_by_lead_time_forecast(spring_forecast_training)
    lead_time_forecast_summer_training = separation_data_by_lead_time_forecast(summer_forecast_training)
    lead_time_forecast_autumn_training = separation_data_by_lead_time_forecast(autumn_forecast_training)

    winter_observation_training, spring_observation_training, summer_observation_training, autumn_observation_training \
        = separation_of_data_by_seasons(speed_wind_observation_training)

    lead_time_observation_winter_training = separation_data_by_lead_time_observation(winter_observation_training)
    lead_time_observation_spring_training = separation_data_by_lead_time_observation(spring_observation_training)
    lead_time_observation_summer_training = separation_data_by_lead_time_observation(summer_observation_training)
    lead_time_observation_autumn_training = separation_data_by_lead_time_observation(autumn_observation_training)

    #  Test data
    current_file = "/home/kirill/Downloads/Data/gfs/forecast_for_point_data_"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_forecast_test = file_reader.values.tolist()
    
    current_file = "/home/kirill/Downloads/Data/gfs/observation_data_test_hour_by_hour"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_observation_test = file_reader.values.tolist()

    winter_forecast_test, spring_forecast_test, summer_forecast_test, autumn_forecast_test \
        = separation_of_data_by_seasons(speed_wind_forecast_test)

    lead_time_forecast_winter_test = separation_data_by_lead_time_forecast(winter_forecast_test)
    lead_time_forecast_spring_test = separation_data_by_lead_time_forecast(spring_forecast_test)
    lead_time_forecast_summer_test = separation_data_by_lead_time_forecast(summer_forecast_test)
    lead_time_forecast_autumn_test = separation_data_by_lead_time_forecast(autumn_forecast_test)

    winter_observation_test, spring_observation_test, summer_observation_test, autumn_observation_test \
        = separation_of_data_by_seasons(speed_wind_observation_test)

    lead_time_observation_winter_test = separation_data_by_lead_time_observation(winter_observation_test)
    lead_time_observation_spring_test = separation_data_by_lead_time_observation(spring_observation_test)
    lead_time_observation_summer_test = separation_data_by_lead_time_observation(summer_observation_test)
    lead_time_observation_autumn_test = separation_data_by_lead_time_observation(autumn_observation_test)

    linear_regression()


main()
