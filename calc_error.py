import difference as df
import abs_error 
import root_mean_square_error as rmse
import correl_coef as correlation
import get_data
import plotting
import matplotlib.pyplot as plt
import separation_data as spdata


def test_for_emptiness(diff, calc_func):
    if len(diff) != 0:
        diff_season = calc_func
    return diff_season


def main():
    speed_wind_observation, choice_num = get_data.observation_data()
    speed_wind_forecast, choice_num = get_data.forecast_data()

    winter_forecast, spring_forecast, summer_forecast, autumn_forecast \
        = spdata.separation_of_data_by_seasons(speed_wind_forecast)
    winter_observation, spring_observation, summer_observation, autumn_observation \
        = spdata.separation_of_data_by_seasons(speed_wind_observation)

    lead_time_forecast_winter = spdata.separation_data_by_lead_time_forecast(winter_forecast)
    lead_time_forecast_spring = spdata.separation_data_by_lead_time_forecast(spring_forecast)
    lead_time_forecast_summer = spdata.separation_data_by_lead_time_forecast(summer_forecast)
    lead_time_forecast_autumn = spdata.separation_data_by_lead_time_forecast(autumn_forecast)

    lead_time_observation_winter = spdata.separation_data_by_lead_time_observation(winter_observation)
    lead_time_observation_spring = spdata.separation_data_by_lead_time_observation(spring_observation)
    lead_time_observation_summer = spdata.separation_data_by_lead_time_observation(summer_observation)
    lead_time_observation_autumn = spdata.separation_data_by_lead_time_observation(autumn_observation)
    print("Select calculation number:")
    print(10 * " " + "1. Different")
    print(10 * " " + "2. Absolute")
    print(10 * " " + "3. RMSE")
    print(10 * " " + "4. Correlation coefficient")
    estimate = int(input("Calculation number: "))
    choice_display = input('Do you need to display graphs by errors? Write yes  or no: ')
    if estimate == 1:
        average_diff_winter = df.get_diff_for_season_and_lead_time(lead_time_forecast_winter,
                                                                   lead_time_observation_winter)
        average_diff_spring = df.get_diff_for_season_and_lead_time(lead_time_forecast_spring,
                                                                   lead_time_observation_spring)
        average_diff_summer = df.get_diff_for_season_and_lead_time(lead_time_forecast_summer,
                                                                   lead_time_observation_summer)
        average_diff_autumn = df.get_diff_for_season_and_lead_time(lead_time_forecast_autumn,
                                                                   lead_time_observation_autumn)

        #df.print_average_diff('зимний', average_diff_winter)
        #df.print_average_diff('весенний', average_diff_spring)
        #df.print_average_diff('летний', average_diff_summer)
        #df.print_average_diff('осенний', average_diff_autumn)

        if choice_display in ('yes', 'y'):
            plotting.plotting_graph_for_error(average_diff_winter, 'Зимний период',
                                              'Средняя арифметическая погрешность', '-')
            plotting.plotting_graph_for_error(average_diff_spring, 'Весенний период',
                                              'Средняя арифметическая погрешность', '--')
            plotting.plotting_graph_for_error(average_diff_summer, 'Летний период',
                                              'Средняя арифметическая погрешность', '-.')
            plotting.plotting_graph_for_error(average_diff_autumn, 'Осенний период',
                                              'Средняя арифметическая погрешность', ':')
            plt.show()
        return average_diff_winter, average_diff_spring, average_diff_summer, average_diff_autumn

    if estimate == 2:
        abs_diff_winter = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_winter,
                                                                          lead_time_observation_winter)
        abs_diff_spring = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_spring,
                                                                          lead_time_observation_spring)
        abs_diff_summer = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_summer,
                                                                          lead_time_observation_summer)
        abs_diff_autumn = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_autumn,
                                                                          lead_time_observation_autumn)

        #abs_error.print_average_diff_abs('зимний',   abs_diff_winter)
        #abs_error.print_average_diff_abs('весенний', abs_diff_spring)
        #abs_error.print_average_diff_abs('летний',   abs_diff_summer)
        #abs_error.print_average_diff_abs('осенний',  abs_diff_autumn)

        if choice_display in ('yes', 'y'):
            plotting.plotting_graph_for_error(abs_diff_winter, 'Зимний период', 'Средняя абсолютная погрешность', '-')
            plotting.plotting_graph_for_error(abs_diff_spring, 'Весенний период', 'Средняя абсолютная погрешность', '--')
            plotting.plotting_graph_for_error(abs_diff_summer, 'Летний период', 'Средняя абсолютная погрешность', '-.')
            plotting.plotting_graph_for_error(abs_diff_autumn, 'Осенний период', 'Средняя абсолютная погрешность', ':')
            plt.show()

        return abs_diff_winter, abs_diff_spring, abs_diff_summer, abs_diff_autumn

    if estimate == 3:
        rmse_winter = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_winter, lead_time_observation_winter)
        rmse_spring = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_spring, lead_time_observation_spring)
        rmse_summer = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_summer, lead_time_observation_summer)
        rmse_autumn = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_autumn, lead_time_observation_autumn)

        #rmse.print_average_rmse('зимний',   rmse_winter)
        #rmse.print_average_rmse('весенний', rmse_spring)
        #rmse.print_average_rmse('летний',   rmse_summer)
        #rmse.print_average_rmse('осенний',  rmse_autumn)

        if choice_display in ('yes', 'y'):
            plotting.plotting_graph_for_error(rmse_winter, 'Зимний период', 'Средняя квадратическая погрешность', '-')
            plotting.plotting_graph_for_error(rmse_spring, 'Весенний период', 'Средняя квадратическая погрешность', '--')
            plotting.plotting_graph_for_error(rmse_summer, 'Летний период', 'Средняя квадратическая погрешность', '-.')
            plotting.plotting_graph_for_error(rmse_autumn, 'Осенний период', 'Средняя квадратическая погрешность', ':')
            plt.show()
        return rmse_winter, rmse_spring, rmse_summer, rmse_autumn

    if estimate == 4:
        correlation_coefficient_winter = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_winter, lead_time_observation_winter)
        correlation_coefficient_spring = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_spring, lead_time_observation_spring)
        correlation_coefficient_summer = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_summer, lead_time_observation_summer)
        correlation_coefficient_autumn = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_autumn, lead_time_observation_autumn)

        #correlation.print_correlation_coefficient('зимний', correlation_coefficient_winter)
        #correlation.print_correlation_coefficient('весенний', correlation_coefficient_spring)
        #correlation.print_correlation_coefficient('летний', correlation_coefficient_summer)
        #correlation.print_correlation_coefficient('осенний', correlation_coefficient_autumn)

        if choice_display in ('yes', 'y'):
            plotting.plotting_graph_for_error(correlation_coefficient_winter, 'Зимний период', 'Коэффициент корреляции', '-')
            plotting.plotting_graph_for_error(correlation_coefficient_spring, 'Весенний период',
                                              'Коэффициент корреляции', '--')
            plotting.plotting_graph_for_error(correlation_coefficient_summer, 'Летний период', 'Коэффициент корреляции', '-.')
            plotting.plotting_graph_for_error(correlation_coefficient_autumn, 'Осенний период',
                                              'Коэффициент корреляции', ':')
            plt.show()

        return correlation_coefficient_winter, correlation_coefficient_spring, correlation_coefficient_spring,\
               correlation_coefficient_autumn


if __name__ == '__main__':
    main()
