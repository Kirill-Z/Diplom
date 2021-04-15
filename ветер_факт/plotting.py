import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt

def plotting_wind_speed(data):
    lengthData = len(data)

    for i in range(lengthData):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]

    fmt = dates.DateFormatter('%Y-%m-%d-%H')

    data_for_delete = []
    x_data = []
    y_data = []

    for i in range(lengthData):
        x_data.append(dt.datetime.strptime(data[i][0], '%Y-%m-%d-%H'))
        y_data.append(data[i][2])
    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_locator(dates.DayLocator())
    plt.xlabel('Date')
    plt.ylabel('Wind Speed')
    plt.title('Wind Speed')
    plt.scatter(x_data, y_data, label='data')
    plt.gcf().autofmt_xdate()
    plt.show()
