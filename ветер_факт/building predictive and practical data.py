import wind_forecast
import practical_wind_forecast
import plotting
import matplotlib.pyplot as plt

speed_wind_predictive = wind_forecast.main()
plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 2, 'b', 'GFS')

value = input("Practical data: If you need to calculate a point, press 1, if you need to calculate an area, "
              "press 2 or 3: ")
if value == '1':
    speed_wind_practical = practical_wind_forecast.main()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'АВ-6, Наблюдение')
elif value == '2':
    speed_wind_practical = practical_wind_forecast.main_area()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r', 'АВ-6, Наблюдение для диапазона '
                                                                                 'времени (+-30 мин)')
elif value == '3':
    speed_wind_practical = practical_wind_forecast.main_area_with_every_minute()
    plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 1, 'r',
                                 'АВ-6, Наблюдение для диапазона времени (+-30 мин), учитывая каждую минуту')


diff = []
for i in range(0, len(speed_wind_predictive)):
    diff1 = []
    diff1.append(speed_wind_practical[i][0])
    for j in range(2, len(speed_wind_predictive[i])):
         diff1.append(speed_wind_practical[i][j-1] - speed_wind_predictive[i][j])
    diff.append(diff1)


diff_winter = []
diff_spring = []
diff_summer = []
diff_autumn = []

for i in range(0, len(diff)):
    if diff[i][0][5:7] == '11':
        diff_winter.append(diff[i])
    elif diff[i][0][5:7] == '12':
        diff_winter.append(diff[i])
    elif diff[i][0][5:7] == '01':
        diff_winter.append(diff[i])
    elif diff[i][0][5:7] == '02':
        diff_winter.append(diff[i])
    elif diff[i][0][5:7] == '03':
        diff_winter.append(diff[i])
    elif diff[i][0][5:7] == '04':
        diff_spring.append(diff[i])
    elif diff[i][0][5:7] == '05':
        diff_spring.append(diff[i])
    elif diff[i][0][5:7] == '07':
        diff_summer.append(diff[i])
    elif diff[i][0][5:7] == '08':
        diff_summer.append(diff[i])
    elif diff[i][0][5:7] == '09':
        diff_autumn.append(diff[i])
    elif diff[i][0][5:7] == '10':
        diff_autumn.append(diff[i])


average_diff_winter = 0
for i in range(0, len(diff_winter)):
    average_diff_winter += diff_winter[i][1]
average_diff_winter = average_diff_winter / len(diff_winter)

average_diff_spring = 0
for i in range(0, len(diff_spring)):
    average_diff_spring += diff_spring[i][1]
average_diff_spring = average_diff_spring / len(diff_spring)

average_diff_summer = 0
for i in range(0, len(diff_summer)):
    average_diff_summer += diff_summer[i][1]
average_diff_summer = average_diff_summer / len(diff_summer)

average_diff_autumn = 0
for i in range(0, len(diff_autumn)):
    average_diff_autumn += diff_autumn[i][1]
average_diff_autumn = average_diff_autumn / len(diff_autumn)

print('Средняя разность за зимний период:')
print(average_diff_winter)
print('Средняя  разность за весенний период:')
print(average_diff_spring)
print('Средняя  разность за летний период:')
print(average_diff_summer)
print('Средняя  разность за осениий период:')
print(average_diff_autumn)




#for i in range(0, len(diff_winter)):
#    print('winter')
#    print(diff_winter[i])
#for i in range(0, len(diff_spring)):
#    print('spring')
#    print(diff_spring[i])
#for i in range(0, len(diff_summer)):
#    print('summer')
#    print(diff_summer[i])
#for i in range(0, len(diff_autumn)):
#    print('autumn')
#    print(diff_autumn[i])

plt.show()
