import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt
import get_data


def plotting_wind_speed(data, data_format, color, label, marker):
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
    plt.xticks(fontsize=28)
    plt.yticks(fontsize=28)
    plt.xlabel('Дата', fontsize=32)
    plt.ylabel('Скорость ветра', fontsize=32)
    plt.title('Скорость ветра', fontsize=32)
    plt.scatter(x_data, y_data, label=label, c=color, marker=marker, s=32)
    plt.legend(fontsize=28)
    plt.gcf().autofmt_xdate()


def plotting_graph_for_error(data, text_information, chart_signature, linestyle):

    x_data = []
    y_data = []

    for i in range(0, len(data)):
        x_data.append(data[i][0])
        y_data.append(data[i][1])

    plt.xlabel('Заблаговременность', fontsize=32)
    plt.ylabel('Оценка', fontsize=32)
    plt.xticks(x_data, fontsize=28)
    plt.yticks(fontsize=28)
    plt.title(chart_signature, fontsize=32)
    plt.scatter(x_data, y_data)
    plt.plot(x_data, y_data, label=text_information, linestyle=linestyle)
    plt.legend(fontsize=24, loc='center right', bbox_to_anchor=(1.35, 0.5))
