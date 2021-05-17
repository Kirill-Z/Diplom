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


def get_forecast_data():
    calc_time = int(input('Press 1 if you want to read the regression for the season or 2 if you want to read the '
                          'regression for the lead time'))
    if calc_time == 1:
        tmp = input('Press 1 if you want to calculate values')
        if tmp == "1":
            value = input(
                "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
            if value == '1':
                wind_forecast.main(value)
            elif value == '2':
                wind_forecast.main(value)

        current_file = "/home/kirill/Downloads/Data/gfs/2016/list_data_by_season"  # Path to the predicted wind speed file
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

    print(length_list_data)
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


def linear_regression_by_season(predictant, predictor):
    x = np.array(predictant).reshape((-1, 1))
    y = np.array(predictor)
    print(x)
    print(y)
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)
    print('predicted response:', y_pred, sep='\n')
    plt.plot(x, y_pred)
    plt.show()

def main():
    np.set_printoptions(threshold=sys.maxsize)
    speed_wind_predictive = get_forecast_data()
    speed_wind_practical = get_observation_data()
    value = int(input('Press 1 if linear regression by season or press 2 for lead time'))
    if value == 1:
        predictive_winter, predictive_spring, predictive_summer, predictive_autumn, practical_winter, practical_spring, practical_summer, practical_autumn = division_of_data_by_seasons(speed_wind_predictive, speed_wind_practical)

        linear_regression_by_season(practical_winter, predictive_winter)
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
