import datetime

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
    plt.xlim(datetime.date(2015, 12, 31), datetime.date(2016, 1, 31))
    plt.ylim(-1, 10)
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=28)
    plt.xlabel('Дата', fontsize=32)
    plt.ylabel('Скорость ветра', fontsize=32)
    plt.title('Скорость ветра', fontsize=32)
    plt.scatter(x_data, y_data, label=label, c=color, marker=marker, s=32, linewidths=4)
    plt.legend(fontsize=28, loc='lower center', bbox_to_anchor=(0.5, -0.85), markerscale=4)
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.gcf().autofmt_xdate()  # For nice date display


def plotting_graph_for_error(data, text_information, chart_signature, linestyle):
    x_data = []
    y_data = []
    for i in range(0, len(data)):
        x_data.append(data[i][0])
        y_data.append(data[i][1])
    plt.subplots_adjust(left=0.07, right=0.76)
    plt.xlabel('Заблаговременность', fontsize=32)
    plt.ylabel('Оценка', fontsize=32)
    plt.xticks(x_data, fontsize=24)
    plt.yticks(fontsize=28)
    plt.title(chart_signature, fontsize=32)
    plt.scatter(x_data, y_data, linewidths=4)
    plt.plot(x_data, y_data, label=text_information, linestyle=linestyle, linewidth=4)
    plt.legend(fontsize=24, loc='center right', bbox_to_anchor=(1.35, 0.5))
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
