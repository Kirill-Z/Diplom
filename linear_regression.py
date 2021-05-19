import math
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import sys
import matplotlib.pyplot as plt
import correl_coef_for_lead_time as correl
import get_data_from_file


def write_in_speed_predictive(lead_time: str, speed_wind_predictive):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


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
    plt.scatter(speed_wind_practical_2018, forecast, color='gray')
    plt.plot(speed_wind_practical_2018, y_pred)
    plt.show()


def main():
    value = int(input('Press 1 if linear regression by season or press 2 for lead time: '))
    np.set_printoptions(threshold=sys.maxsize)
    speed_wind_predictive = get_data_from_file.forecast_data(value)
    speed_wind_practical, speed_wind_practical_2018 = get_data_from_file.observation_data()

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
        print(speed_wind_practical)
        lead_time_predictive = [
            lead_time_0_predictive, lead_time_3_predictive, lead_time_6_predictive, lead_time_9_predictive,
            lead_time_12_predictive, lead_time_15_predictive, lead_time_18_predictive, lead_time_21_predictive,
            lead_time_24_predictive, lead_time_27_predictive, lead_time_30_predictive, lead_time_33_predictive,
            lead_time_36_predictive, lead_time_39_predictive, lead_time_42_predictive, lead_time_45_predictive,
            lead_time_48_predictive, lead_time_51_predictive, lead_time_54_predictive, lead_time_57_predictive,
            lead_time_60_predictive, lead_time_63_predictive, lead_time_66_predictive, lead_time_69_predictive,
            lead_time_72_predictive, lead_time_75_predictive,
            lead_time_78_predictive] = correl.separation_data_by_lead_time(speed_wind_predictive)

        lead_time_practical = [
            lead_time_0_practical, lead_time_3_practical, lead_time_6_practical, lead_time_9_practical,
            lead_time_12_practical, lead_time_15_practical, lead_time_18_practical,
            lead_time_21_practical] = correl.separation_data_by_lead_time_practical(speed_wind_practical)



def division_of_data_by_lead_time(predictive, practical):
    lead_time_0_predictive = []
    lead_time_3_predictive = []
    lead_time_6_predictive = []
    lead_time_9_predictive = []
    lead_time_12_predictive = []
    lead_time_15_predictive = []
    lead_time_18_predictive = []
    lead_time_21_predictive = []
    lead_time_24_predictive = []
    lead_time_27_predictive = []
    lead_time_30_predictive = []
    lead_time_33_predictive = []
    lead_time_36_predictive = []
    lead_time_39_predictive = []
    lead_time_42_predictive = []
    lead_time_45_predictive = []
    lead_time_48_predictive = []
    lead_time_51_predictive = []
    lead_time_54_predictive = []
    lead_time_57_predictive = []
    lead_time_60_predictive = []
    lead_time_63_predictive = []
    lead_time_66_predictive = []
    lead_time_69_predictive = []
    lead_time_72_predictive = []
    lead_time_75_predictive = []
    lead_time_78_predictive = []

    for i, j in zip(predictive[0:8], practical):
        if float(predictive[i][5]) >= 9999 or math.isnan(float(practical[i][5])):
            continue
        else:
            pass
    for i, j in zip(predictive[8:16], practical):
        if float(predictive[i][5]) >= 9999 or math.isnan(float(practical[i][5])):
            continue
        else:
            pass
    for i, j in zip(predictive[16:24], practical):
        if float(predictive[i][5]) >= 9999 or math.isnan(float(practical[i][5])):
            continue
        else:
            pass
    for i, j in zip(predictive[24:27], practical):
        if float(predictive[i][5]) >= 9999 or math.isnan(float(practical[i][5])):
            continue
        else:
            pass


main()
