import wind_forecast
import practical_wind_forecast
import plotting
import matplotlib.pyplot as plt

speed_wind_predictive = wind_forecast.main()
plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 2, 'b', 'Прогноз')

value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
if value == '1':
    speed_wind_practical = practical_wind_forecast.main()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'Наблюдение')
elif value == '2':
    speed_wind_practical = practical_wind_forecast.main_area()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'Прогноз для диапазона времени (+-30 мин)')
elif value == '3':
    speed_wind_practical = practical_wind_forecast.main_area_with_every_minute()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r',
                                 'Прогноз для диапазона времени (+-30 мин)')

plt.show()




