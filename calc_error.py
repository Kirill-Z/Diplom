import difference as df
import abs_error 
import root_mean_square_error as rmse
import correl_coef as correlation
import get_data
import plotting
import matplotlib.pyplot as plt


def separation_of_data_by_seasons(diff):
    winter = []
    spring = []
    summer = []
    autumn = []
    for i in range(0, len(diff)):
        month = str(diff[i][0][4:6])
        diff_value = diff[i]
        if month in ('11', '12', '01', '02', '03'):
            winter.append(diff_value)

        if month in ('04', '05'):
            spring.append(diff_value)

        if month in ('06', '07', '08'):
            summer.append(diff_value)

        if month in ('09', '10'):
            autumn.append(diff_value)

    return winter, spring, summer, autumn


def separation_data_by_lead_time_forecast(data):
    lead_time_0 = []
    lead_time_3 = []
    lead_time_6 = []
    lead_time_9 = []
    lead_time_12 = []
    lead_time_15 = []
    lead_time_18 = []
    lead_time_21 = []
    lead_time_24 = []
    lead_time_27 = []
    lead_time_30 = []
    lead_time_33 = []
    lead_time_36 = []
    lead_time_39 = []
    lead_time_42 = []
    lead_time_45 = []
    lead_time_48 = []
    lead_time_51 = []
    lead_time_54 = []
    lead_time_57 = []
    lead_time_60 = []
    lead_time_63 = []
    lead_time_66 = []
    lead_time_69 = []
    lead_time_72 = []
    lead_time_75 = []
    lead_time_78 = []
    for i in range(0, len(data)):
        lead_time = data[i][0][11:13]
        if lead_time == '00':
            lead_time_0.append(data[i][5])
        if lead_time == '03':
            lead_time_3.append(data[i][5])
        if lead_time == '06':
            lead_time_6.append(data[i][5])
        if lead_time == '09':
            lead_time_9.append(data[i][5])
        if lead_time == '12':
            lead_time_12.append(data[i][5])
        if lead_time == '15':
            lead_time_15.append(data[i][5])
        if lead_time == '18':
            lead_time_18.append(data[i][5])
        if lead_time == '21':
            lead_time_21.append(data[i][5])
        if lead_time == '24':
            lead_time_24.append(data[i][5])
        if lead_time == '27':
            lead_time_27.append(data[i][5])
        if lead_time == '30':
            lead_time_30.append(data[i][5])
        if lead_time == '33':
            lead_time_33.append(data[i][5])
        if lead_time == '36':
            lead_time_36.append(data[i][5])
        if lead_time == '39':
            lead_time_39.append(data[i][5])
        if lead_time == '42':
            lead_time_42.append(data[i][5])
        if lead_time == '45':
            lead_time_45.append(data[i][5])
        if lead_time == '48':
            lead_time_48.append(data[i][5])
        if lead_time == '51':
            lead_time_51.append(data[i][5])
        if lead_time == '54':
            lead_time_54.append(data[i][5])
        if lead_time == '57':
            lead_time_57.append(data[i][5])
        if lead_time == '60':
            lead_time_60.append(data[i][5])
        if lead_time == '63':
            lead_time_63.append(data[i][5])
        if lead_time == '66':
            lead_time_66.append(data[i][5])
        if lead_time == '69':
            lead_time_69.append(data[i][5])
        if lead_time == '72':
            lead_time_72.append(data[i][5])
        if lead_time == '75':
            lead_time_75.append(data[i][5])
        if lead_time == '78':
            lead_time_78.append(data[i][5])
            
    lead_time_data = [lead_time_0, lead_time_3, lead_time_6, lead_time_9, lead_time_12, lead_time_15, lead_time_18,
                      lead_time_21, lead_time_24, lead_time_27, lead_time_30, lead_time_33, lead_time_36, lead_time_39,
                      lead_time_42, lead_time_45, lead_time_48, lead_time_51, lead_time_54, lead_time_57, lead_time_60,
                      lead_time_63, lead_time_66, lead_time_69, lead_time_72, lead_time_75, lead_time_78]
    return lead_time_data


def separation_data_by_lead_time_observation(data):
    lead_time_0 = []
    lead_time_3 = []
    lead_time_6 = []
    lead_time_9 = []
    lead_time_12 = []
    lead_time_15 = []
    lead_time_18 = []
    lead_time_21 = []

    for i in range(0, len(data)):
        lead_time = data[i][4][0:2]
        if lead_time == '00':
            lead_time_0.append(data[i][5])
        if lead_time == '03':
            lead_time_3.append(data[i][5])
        if lead_time == '06':
            lead_time_6.append(data[i][5])
        if lead_time == '09':
            lead_time_9.append(data[i][5])
        if lead_time == '12':
            lead_time_12.append(data[i][5])
        if lead_time == '15':
            lead_time_15.append(data[i][5])
        if lead_time == '18':
            lead_time_18.append(data[i][5])
        if lead_time == '21':
            lead_time_21.append(data[i][5])
    lead_time_data = [lead_time_0, lead_time_3, lead_time_6, lead_time_9,
                      lead_time_12, lead_time_15, lead_time_18, lead_time_21]
    return lead_time_data


def test_for_emptiness(diff, calc_func):
    if len(diff) != 0:
        diff_season = calc_func
    return diff_season


def main():
    speed_wind_forecast = get_data.forecast_data()
    speed_wind_observation = get_data.observation_data()

    winter_forecast, spring_forecast, summer_forecast, autumn_forecast \
        = separation_of_data_by_seasons(speed_wind_forecast)

    lead_time_forecast_winter = separation_data_by_lead_time_forecast(winter_forecast)
    lead_time_forecast_spring = separation_data_by_lead_time_forecast(spring_forecast)
    lead_time_forecast_summer = separation_data_by_lead_time_forecast(summer_forecast)
    lead_time_forecast_autumn = separation_data_by_lead_time_forecast(autumn_forecast)

    winter_observation, spring_observation, summer_observation, autumn_observation \
        = separation_of_data_by_seasons(speed_wind_observation)
    
    lead_time_observation_winter = separation_data_by_lead_time_observation(winter_observation)
    lead_time_observation_spring = separation_data_by_lead_time_observation(spring_observation)
    lead_time_observation_summer = separation_data_by_lead_time_observation(summer_observation)
    lead_time_observation_autumn = separation_data_by_lead_time_observation(autumn_observation)
    print("Select calculation number:")
    print(10 * " " + "1. Different")
    print(10 * " " + "2. Absolute")
    print(10 * " " + "3. RMSE")
    print(10 * " " + "4. correlation coefficient")
    estimate = int(input("Calculation number: "))
    if estimate == 1:
        average_diff_winter = df.get_diff_for_season_and_lead_time(lead_time_forecast_winter,
                                                                   lead_time_observation_winter)
        average_diff_spring = df.get_diff_for_season_and_lead_time(lead_time_forecast_spring,
                                                                   lead_time_observation_spring)
        average_diff_summer = df.get_diff_for_season_and_lead_time(lead_time_forecast_summer,
                                                                   lead_time_observation_summer)
        average_diff_autumn = df.get_diff_for_season_and_lead_time(lead_time_forecast_autumn,
                                                                   lead_time_observation_autumn)

        df.print_average_diff('зимний', average_diff_winter)
        df.print_average_diff('весенний', average_diff_spring)
        df.print_average_diff('летний', average_diff_summer)
        df.print_average_diff('осенний', average_diff_autumn)

        plotting.plotting_graph_for_error(average_diff_winter, 'Зимний период', 'Средняя арифметическая погрешность')
        plotting.plotting_graph_for_error(average_diff_spring, 'Весенний период', 'Средняя арифметическая погрешность')
        plotting.plotting_graph_for_error(average_diff_summer, 'Летний период', 'Средняя арифметическая погрешность')
        plotting.plotting_graph_for_error(average_diff_autumn, 'Осенний период', 'Средняя арифметическая погрешность')
        plt.show()

    if estimate == 2:
        abs_diff_winter = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_winter,
                                                                          lead_time_observation_winter)
        abs_diff_spring = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_spring,
                                                                          lead_time_observation_spring)
        abs_diff_summer = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_summer,
                                                                          lead_time_observation_summer)
        abs_diff_autumn = abs_error.get_diff_abs_for_season_and_lead_time(lead_time_forecast_autumn,
                                                                          lead_time_observation_autumn)

        abs_error.print_average_diff_abs('зимний',   abs_diff_winter)
        abs_error.print_average_diff_abs('весенний', abs_diff_spring)
        abs_error.print_average_diff_abs('летний',   abs_diff_summer)
        abs_error.print_average_diff_abs('осенний',  abs_diff_autumn)

        plotting.plotting_graph_for_error(abs_diff_winter, 'Зимний период', 'Абсолютная погрешность')
        plotting.plotting_graph_for_error(abs_diff_spring, 'Весенний период', 'Абсолютная погрешность')
        plotting.plotting_graph_for_error(abs_diff_summer, 'Летний период', 'Абсолютная погрешность')
        plotting.plotting_graph_for_error(abs_diff_autumn, 'Осенний период', 'Абсолютная погрешность')
        plt.show()

    if estimate == 3:
        rmse_winter = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_winter, lead_time_observation_winter)
        rmse_spring = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_spring, lead_time_observation_spring)
        rmse_summer = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_summer, lead_time_observation_summer)
        rmse_autumn = rmse.get_rmse_for_season_and_lead_time(lead_time_forecast_autumn, lead_time_observation_autumn)

        rmse.print_average_rmse('зимний',   rmse_winter)
        rmse.print_average_rmse('весенний', rmse_spring)
        rmse.print_average_rmse('летний',   rmse_summer)
        rmse.print_average_rmse('осенний',  rmse_autumn)

        plotting.plotting_graph_for_error(rmse_winter, 'Зимний период', 'Среднеквадратичная погрешность')
        plotting.plotting_graph_for_error(rmse_spring, 'Весенний период', 'Среднеквадратичная погрешность')
        plotting.plotting_graph_for_error(rmse_summer, 'Летний период', 'Среднеквадратичная погрешность')
        plotting.plotting_graph_for_error(rmse_autumn, 'Осенний период', 'Среднеквадратичная погрешность')
        plt.show()

    if estimate == 4:
        correlation_coefficient_winter = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_winter, lead_time_observation_winter)
        correlation_coefficient_spring = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_spring, lead_time_observation_spring)
        correlation_coefficient_summer = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_summer, lead_time_observation_summer)
        correlation_coefficient_autumn = correlation.get_correlation_coefficient_for_season_and_lead_time(
            lead_time_forecast_autumn, lead_time_observation_autumn)

        correlation.print_correlation_coefficient('зимний', correlation_coefficient_winter)
        correlation.print_correlation_coefficient('весенний', correlation_coefficient_spring)
        correlation.print_correlation_coefficient('летний', correlation_coefficient_summer)
        correlation.print_correlation_coefficient('осенний', correlation_coefficient_autumn)

        plotting.plotting_graph_for_error(correlation_coefficient_winter, 'Зимний период', 'Коэффициент корреляции')
        plotting.plotting_graph_for_error(correlation_coefficient_spring, 'Весенний период', 'Коэффициент корреляции')
        plotting.plotting_graph_for_error(correlation_coefficient_summer, 'Летний период', 'Коэффициент корреляции')
        plotting.plotting_graph_for_error(correlation_coefficient_autumn, 'Осенний период', 'Коэффициент корреляции')
        plt.show()


if __name__ == '__main__':
    main()
