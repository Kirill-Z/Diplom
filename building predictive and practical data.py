import wind_forecast
import practical_wind_forecast
import plotting
import matplotlib.pyplot as plt

value = input("Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
if value == '1':
    speed_wind_predictive = wind_forecast.main(value)
    plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 1, 'b', 'GFS, Прогноз для точки')
elif value == '2':
    speed_wind_predictive = wind_forecast.main(value)
    plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 1, 'b', 'GFS, Прогноз для области')


value = input("Observation data: If you need to calculate a point, press 1, if you need to calculate an area, "
              "press 2 or 3: ")
if value == '1':
    speed_wind_practical = practical_wind_forecast.main(value)
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'АВ-6, Наблюдение')
elif value == '2':
    speed_wind_practical = practical_wind_forecast.main_area(value)
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'АВ-6, Наблюдение для диапазона '
                                                                                 'времени (+-30 мин)')
elif value == '3':
    speed_wind_practical = practical_wind_forecast.main_area_with_every_minute(value)
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r',
                                 'АВ-6, Наблюдение для диапазона времени (+-30 мин), учитывая каждую минуту')

plt.show()