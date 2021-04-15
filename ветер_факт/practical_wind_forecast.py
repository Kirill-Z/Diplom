import pandas as pd
import os
import re
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt

PATH = "/media/kirill/e61c7b4d-3c04-47cc-aabb-23d698198ced/home/kirill/Downloads/Data/АВ6_Толмачево/2016/01 январь 2016/"


def add_data_to_the_speed_list(data, i):
    speed_wind = []
    speed_wind.append(file[2:])
    speed_wind.append(file[2:6])
    speed_wind.append(file[6:8])
    speed_wind.append(file[8:10])
    speed_wind.append(data[i][0])
    speed_wind.append(data[i][2])
    return speed_wind


def write_data_to_a_file(speed_wind, my_file):
    for i in range(0, len(speed_wind)):
        for j in range(0, len(speed_wind[i])):
            if len(str(speed_wind[i][j])) == 1:
                my_file.write(str(speed_wind[i][j]) + '  |  ')
            elif len(str(speed_wind[i][j])) == 3:
                my_file.write(str(speed_wind[i][j]) + '|   ')
            else:
                my_file.write(str(speed_wind[i][j]) + ' |  ')
        my_file.write('\n')

    my_file.close()
    return print('The end write in file')


my_file = open(PATH + 'data_practical_wind_01_2016.csv', 'w')
my_file.write('File name    |  Year |Month| Day |  Time  |Speed|\n')
speed_wind = []
for file in sorted(os.listdir(PATH)):

    if re.match('av*', file):
        currentFile = PATH + file
        file_reader = pd.read_csv(currentFile, sep=';', header=None, engine='python')
        data_from_file = file_reader.values.tolist()

        for i in range(0, len(data_from_file)):
            hour1 = data_from_file[i][0][0]
            hour2 = data_from_file[i][0][1]
            hour = hour1 + hour2

            minute1 = data_from_file[i][0][3]
            minute2 = data_from_file[i][0][4]
            minute = minute1 + minute2

            if int(hour) % 3 == 0 and int(minute) == 0:
                speed_wind.append(add_data_to_the_speed_list(data_from_file, i))

write_data_to_a_file(speed_wind, my_file)


data = speed_wind
lengthData = len(data)

for i in range(lengthData):
    data[i][0] = str(data[i][1])+'-'+str(data[i][2])+'-'+str(data[i][3])+'-'+str(data[i][4])
    del data[i][4]
    del data[i][3]
    del data[i][2]
    del data[i][1]

fmt = dates.DateFormatter('%Y-%m-%d-%H:%M')

data_for_delete = []
x_data = []
y_data = []

for i in range(lengthData):
    x_data.append(dt.datetime.strptime(data[i][0], '%Y-%m-%d-%H:%M'))
    y_data.append(data[i][1])
plt.gca().xaxis.set_major_formatter(fmt)
plt.gca().xaxis.set_major_locator(dates.DayLocator())
plt.xlabel('Date')
plt.ylabel('Wind Speed')
plt.title('Wind Speed')
plt.scatter(x_data, y_data, label='data')
plt.gcf().autofmt_xdate()
plt.show()



