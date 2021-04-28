import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt

def plotting_wind_speed(data, data_format, num_param, color, label):
    lengthData = len(data)

    for i in range(lengthData):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]
    fmt = dates.DateFormatter(data_format)

    x_data = []
    y_data = []

    for i in range(lengthData):
        if data[i][1] >= 9999:
            continue
        else:
            x_data.append(dt.datetime.strptime(data[i][0], data_format))
            y_data.append(data[i][num_param])

    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_locator(dates.DayLocator())
    plt.xlabel('Date')
    plt.ylabel('Wind Speed')
    plt.title('Wind Speed')
    plt.scatter(x_data, y_data, label=label, edgecolors=color)
    plt.legend()
    plt.gcf().autofmt_xdate()

