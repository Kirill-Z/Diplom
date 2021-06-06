import plotting
import matplotlib.pyplot as plt
import get_data


def choice_speed_data_with_lead_time(speed_wind):
    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])
    return speed_wind_with_lead_time_on_this_day


value = input("Forecast data: If you need to get data for the point, press 1, if you need to get data for an area, "
              "press 2 and press 3, if you need to get data for the 5 points: ")
if value == '1':
    speed_wind_predictive = get_data.forecast_data()
    speed_wind_predictive = choice_speed_data_with_lead_time(speed_wind_predictive)
    plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 'b', 'GFS, Прогноз для точки', 'o')
elif value == '2':
    speed_wind_predictive = get_data.forecast_data()
    speed_wind_predictive = choice_speed_data_with_lead_time(speed_wind_predictive)
    plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 'b', 'GFS, Прогноз для области', 'o')
elif value == '3':
    speed_wind_predictive = get_data.forecast_data()
    speed_wind_predictive = choice_speed_data_with_lead_time(speed_wind_predictive)
    plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 'b', 'GFS, Прогноз для 5 точек', 'o')


value = input("Observation data: If you need to get data hour per hour, press 1, "
              "if you need to get data in the time range (+ -30 minutes), press 2 and if you need to calculate data "
              "in the time range (+ -30 minutes), taking into account every minute, press 3: ")
if value == '1':
    speed_wind_practical = get_data.observation_data()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r', 'АВ-6, Наблюдение', 's')
elif value == '2':
    speed_wind_practical = get_data.observation_data()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r',
                                 'АВ-6, Наблюдение для диапазона времени (+-30 мин)', 's')
elif value == '3':
    speed_wind_practical = get_data.observation_data()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r',
                                 'АВ-6, Наблюдение для диапазона времени (+-30 мин), учитывая каждую минуту', 's')

plt.show()
