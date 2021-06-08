import matplotlib.pyplot as plt
import plotting
import get_data


def choice_speed_data_with_lead_time(speed_wind):
    """Sample forecast data up to 24 hours only."""
    speed_wind_with_lead_time_on_this_day = []
    for i in range(len(speed_wind)):
        file_name = speed_wind[i][0][11:]
        if int(file_name) < 24:
            speed_wind_with_lead_time_on_this_day.append(speed_wind[i])
    return speed_wind_with_lead_time_on_this_day


def main():
    speed_wind_predictive, choice_num = get_data.forecast_data()
    speed_wind_predictive = choice_speed_data_with_lead_time(speed_wind_predictive)
    if choice_num == '1':
        plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 'b', 'GFS, Прогноз для точки', 'o')
    elif choice_num == '2':
        plotting.plotting_wind_speed(speed_wind_predictive, '%Y-%m-%d-%H', 'b', 'GFS, Прогноз для 5 точек', 'o')

    speed_wind_practical, choice_num = get_data.observation_data()
    if choice_num == '1':
        plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r', 'АВ-6, Наблюдение', 's')
    elif choice_num == '2':
        plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r',
                                     'АВ-6, Наблюдение для диапазона времени (+-30 мин)', 's')
    elif choice_num == '3':
        plotting.plotting_wind_speed(speed_wind_practical, '%Y-%m-%d-%H:%M', 'r',
                                     'АВ-6, Наблюдение для диапазона времени (+-30 мин), учитывая каждую минуту', 's')

    plt.subplots_adjust(bottom=0.44, left=0.17, right=0.99, top=0.95)
    plt.show()


if __name__ == '__main__':
    main()
