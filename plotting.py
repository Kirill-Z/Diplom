import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt
import get_data


def plotting_wind_speed(data, data_format, color, label):

    data = get_data.get_date_and_speed(data)

    fmt = dates.DateFormatter(data_format)

    x_data = []
    y_data = []

    for i in range(0, len(data)):
        if data[i][1] >= 9999:
            continue
        else:
            x_data.append(dt.datetime.strptime(data[i][0], data_format))
            y_data.append(data[i][1])

    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_locator(dates.DayLocator())
    plt.xlabel('Date')
    plt.ylabel('Wind Speed')
    plt.title('Wind Speed')
    plt.scatter(x_data, y_data, label=label, edgecolors=color)
    plt.legend()
    plt.gcf().autofmt_xdate()


def plotting_graph_for_error(data, text_information, chart_signature):

    x_data = []
    y_data = []

    for i in range(0, len(data)):
        x_data.append(data[i][0])
        y_data.append(data[i][1])

    plt.xlabel('Заблаговременность')
    plt.ylabel('Оценка')
    plt.xticks(x_data)
    plt.title(chart_signature)
    plt.scatter(x_data, y_data)
    plt.plot(x_data, y_data, label=text_information)
    plt.legend()
