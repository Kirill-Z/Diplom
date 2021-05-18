import math
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import wind_forecast
import practical_wind_forecast
import sys
import matplotlib.pyplot as plt


def write_in_speed_predictive(lead_time: str, speed_wind_predictive):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


def get_forecast_data(calc_time):
    if calc_time == 1:
        tmp = input('Press 1 if you want to calculate values: ')
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
    elif calc_time == 2:
        tmp = input('Press 1 if you want to calculate values')
        if tmp == "1":
            value = input(
                "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
            if value == '1':
                wind_forecast.main_for_difference_lead_time(value)
            elif value == '2':
                wind_forecast.main_for_difference_lead_time(value)

        current_file = "/home/kirill/Downloads/Data/gfs/2016/list_data"  # Path to the predicted wind speed file
        file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
        speed_wind_predictive = []
        speed_wind = file_reader.values.tolist()

        lead_time = (
            '00', '03', '06', '09', '12', '15', '18', '21', '24', '27', '30', '33', '36', '39', '42', '45', '48', '51',
            '54', '57', '60', '63', '66', '69', '72', '75', '78')

        for i in lead_time:
            speed_wind_predictive.append(write_in_speed_predictive(i, speed_wind))

    return speed_wind_predictive


def get_observation_data():
    value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
                  "press 2 or 3: ")
    if value == '1':
        speed_wind_practical = practical_wind_forecast.main(value)
    elif value == '2':
        speed_wind_practical = practical_wind_forecast.main(value)
    elif value == '3':
        speed_wind_practical = practical_wind_forecast.main(value)

    return speed_wind_practical

'''
def clear_data(predictive, practical):
    if len(predictive) < len(practical):
        tmp = int(len(predictive))
    elif len(practical) < len(predictive):
        tmp = int(len(practical))

    speed_wind_practical = []
    speed_wind_predictive = []
    for i in range(0, tmp):
        if float(speed_wind_predictive[i]) >= 9999 or math.isnan(float(speed_wind_practical[i])):
            continue
        else:
            speed_wind_practical.append(practical[i])
            speed_wind_predictive.append(predictive[i])

    return speed_wind_practical, speed_wind_predictive
'''

def division_of_data_by_seasons(predictive, practical):
    predictive_winter = []
    predictive_spring = []
    predictive_summer = []
    predictive_autumn = []
    practical_winter = []
    practical_spring = []
    practical_summer = []
    practical_autumn = []

    if len(predictive) < len(practical):
        length_list_data = len(predictive)
    elif len(practical) < len(predictive):
        length_list_data = len(practical)
    else:
        length_list_data = len(predictive)

    for i in range(0, length_list_data):
        if float(predictive[i][5]) >= 9999 or math.isnan(float(practical[i][5])):
            continue
        else:
            month = str(predictive[i][0][4:6])
            if month == '11':
                predictive_winter.append(predictive[i][5])
                practical_winter.append(practical[i][5])

            if month == '12':
                predictive_winter.append(predictive[i][5])
                practical_winter.append(practical[i][5])

            if month in ('01', '1-'):
                predictive_winter.append(predictive[i][5])
                practical_winter.append(practical[i][5])

            if month in ('02', '2-'):
                predictive_winter.append(predictive[i][5])
                practical_winter.append(practical[i][5])

            if month in ('03', '3-'):
                predictive_winter.append(predictive[i][5])
                practical_winter.append(practical[i][5])

            if month in ('04', '4-'):
                predictive_spring.append(predictive[i][5])
                practical_spring.append(practical[i][5])

            if month in ('05', '5-'):
                predictive_spring.append(predictive[i][5])
                practical_spring.append(practical[i][5])

            if month in ('06', '6-'):
                predictive_summer.append(predictive[i][5])
                practical_summer.append(practical[i][5])

            if month in ('07', '7-'):
                predictive_summer.append(predictive[i][5])
                practical_summer.append(practical[i][5])

            if month in ('08', '8-'):
                predictive_summer.append(predictive[i][5])
                practical_summer.append(practical[i][5])

            if month in ('09', '9-'):
                predictive_autumn.append(predictive[i][5])
                practical_autumn.append(practical[i][5])

            if month == '10':
                predictive_autumn.append(predictive[i][5])
                practical_autumn.append(practical[i][5])

    return predictive_winter, predictive_spring, predictive_summer, predictive_autumn, practical_winter, practical_spring, practical_summer, practical_autumn


def division_of_data_by_seasons_for_forecast(forecast):
    forecast_winter = []
    forecast_spring = []
    forecast_summer = []
    forecast_autumn = []



    for i in range(0, len(forecast)):
        if float(forecast[i][5]) >= 9999:
            continue
        else:
            month = str(forecast[i][0][4:6])
            if month == '11':
                forecast_winter.append(forecast[i][5])

            if month == '12':
                forecast_winter.append(forecast[i][5])

            if month in ('01', '1-'):
                forecast_winter.append(forecast[i][5])

            if month in ('02', '2-'):
                forecast_winter.append(forecast[i][5])

            if month in ('03', '3-'):
                forecast_winter.append(forecast[i][5])

            if month in ('04', '4-'):
                forecast_spring.append(forecast[i][5])

            if month in ('05', '5-'):
                forecast_spring.append(forecast[i][5])

            if month in ('06', '6-'):
                forecast_summer.append(forecast[i][5])

            if month in ('07', '7-'):
                forecast_summer.append(forecast[i][5])

            if month in ('08', '8-'):
                forecast_summer.append(forecast[i][5])

            if month in ('09', '9-'):
                forecast_autumn.append(forecast[i][5])

            if month == '10':
                forecast_autumn.append(forecast[i][5])

    return forecast_winter, forecast_spring, forecast_summer, forecast_autumn


def linear_regression_by_season(predictant, predictor, forecast, speed_wind_practical_2018):
    x = np.array(predictant).reshape((-1, 1))
    y = np.array(predictor).reshape((-1, 1))
    speed_wind_practical_2018 = np.array(speed_wind_practical_2018).reshape((-1, 1))
    forecast = np.array(forecast).reshape((-1, 1))
    #print(x)
    #print(y)
    print(speed_wind_practical_2018)
    model = LinearRegression().fit(x, y)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    y_pred = model.predict(speed_wind_practical_2018)
    #print('predicted response:', y_pred, sep='\n')
    print(len(y_pred))
    #plt.scatter(speed_wind_practical_2018, forecast, color='gray')
    plt.plot(speed_wind_practical_2018, y_pred)
    plt.show()


def main():
    value = int(input('Press 1 if linear regression by season or press 2 for lead time: '))
    np.set_printoptions(threshold=sys.maxsize)
    speed_wind_predictive = get_forecast_data(value)
    speed_wind_practical, speed_wind_practical_2018 = get_observation_data()

    if value == 1:
        predictive_winter, predictive_spring, predictive_summer, predictive_autumn, practical_winter, practical_spring, practical_summer, practical_autumn = division_of_data_by_seasons(speed_wind_predictive, speed_wind_practical)

        current_file = "/home/kirill/Downloads/Data/gfs/list_data_by_season_forecast"  # Path to the predicted wind speed file
        file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
        forecast = file_reader.values.tolist()

        forecast_winter, forecast_spring, forecast_summer, forecast_autumn, pr_winter, pr_spring, pr_summer, pr_autumn = division_of_data_by_seasons(forecast, speed_wind_practical_2018)

        linear_regression_by_season(practical_winter, predictive_winter, forecast_winter, pr_winter)
        linear_regression_by_season(practical_spring, predictive_spring, forecast_spring, pr_spring)
        linear_regression_by_season(practical_summer, predictive_summer, forecast_summer, pr_summer)
        linear_regression_by_season(practical_autumn, predictive_autumn, forecast_autumn, pr_autumn)
    if value == 2:
        pass

'''
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('Coefficient of determination: ', r_sq)

print('intercept:', model.intercept_)
print('slope:', model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
'''
main()
