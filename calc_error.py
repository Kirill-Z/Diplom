import difference as different
import abs_error_by_season as abs
import root_mean_square_error_by_season as rmse
import correl_coef_by_season as correl
import get_data_from_file


def get_need_data(data):
    for i in range(len(data)):
        data[i][0] = str(data[i][1]) + '-' + str(data[i][2]) + '-' + str(data[i][3]) + '-' + str(data[i][4])
        del data[i][4]
        del data[i][3]
        del data[i][2]
        del data[i][1]
    return data


def division_of_data_by_seasons(diff):
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


def separation_data_by_lead_time(data):
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
            lead_time_0.append(data[i])
        if lead_time == '03':
            lead_time_3.append(data[i])
        if lead_time == '06':
            lead_time_6.append(data[i])
        if lead_time == '09':
            lead_time_9.append(data[i])
        if lead_time == '12':
            lead_time_12.append(data[i])
        if lead_time == '15':
            lead_time_15.append(data[i])
        if lead_time == '18':
            lead_time_18.append(data[i])
        if lead_time == '21':
            lead_time_21.append(data[i])
        if lead_time == '24':
            lead_time_24.append(data[i])
        if lead_time == '27':
            lead_time_27.append(data[i])
        if lead_time == '30':
            lead_time_30.append(data[i])
        if lead_time == '33':
            lead_time_33.append(data[i])
        if lead_time == '36':
            lead_time_36.append(data[i])
        if lead_time == '39':
            lead_time_39.append(data[i])
        if lead_time == '42':
            lead_time_42.append(data[i])
        if lead_time == '45':
            lead_time_45.append(data[i])
        if lead_time == '48':
            lead_time_48.append(data[i])
        if lead_time == '51':
            lead_time_51.append(data[i])
        if lead_time == '54':
            lead_time_54.append(data[i])
        if lead_time == '57':
            lead_time_57.append(data[i])
        if lead_time == '60':
            lead_time_60.append(data[i])
        if lead_time == '63':
            lead_time_63.append(data[i])
        if lead_time == '66':
            lead_time_66.append(data[i])
        if lead_time == '69':
            lead_time_69.append(data[i])
        if lead_time == '72':
            lead_time_72.append(data[i])
        if lead_time == '75':
            lead_time_75.append(data[i])
        if lead_time == '78':
            lead_time_78.append(data[i])

    return lead_time_0, lead_time_3, lead_time_6, lead_time_9, lead_time_12, lead_time_15, lead_time_18, lead_time_21, \
           lead_time_24, lead_time_27, lead_time_30, lead_time_33, lead_time_36, lead_time_39, lead_time_42, \
           lead_time_45, lead_time_48, lead_time_51, lead_time_54, lead_time_57, lead_time_60, lead_time_63, \
           lead_time_66, lead_time_69, lead_time_72, lead_time_75, lead_time_78


def test_for_emptiness(diff, calc_func):
    if len(diff) != 0:
        diff_season = calc_func
    return diff_season


def separation_data_by_lead_time_practical(data):
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
            lead_time_0.append(data[i])
        if lead_time == '03':
            lead_time_3.append(data[i])
        if lead_time == '06':
            lead_time_6.append(data[i])
        if lead_time == '09':
            lead_time_9.append(data[i])
        if lead_time == '12':
            lead_time_12.append(data[i])
        if lead_time == '15':
            lead_time_15.append(data[i])
        if lead_time == '18':
            lead_time_18.append(data[i])
        if lead_time == '21':
            lead_time_21.append(data[i])

    return lead_time_0, lead_time_3, lead_time_6, lead_time_9, lead_time_12, lead_time_15, lead_time_18, lead_time_21


def get_diff_for_season_and_lead_time(lead_time_forecast, lead_time_practical):
    average_diff = []
    lead_time = 0
    for predictive, practical in zip(lead_time_forecast[0: 8], lead_time_practical):
        average_diff.append(
            [lead_time, different.calc_the_average_diff(get_need_data(predictive), get_need_data(practical))])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[8: 16], lead_time_practical):
        average_diff.append([lead_time, different.calc_the_average_diff(get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[16: 24], lead_time_practical):
        average_diff.append([lead_time, different.calc_the_average_diff(get_need_data(predictive), practical)])
        lead_time += 3

    for predictive, practical in zip(lead_time_forecast[24:27], lead_time_practical[0:3]):
        average_diff.append([lead_time, different.calc_the_average_diff(get_need_data(predictive), practical)])
        lead_time += 3

    return average_diff


def print_average_diff(season, average_diff):
    for i in range(0, len(average_diff)):
        print(f'Средняя разность {season} за период и заблаговременность {average_diff[i][0]}: {average_diff[i][1]}')
    print('\n')


def main():
    speed_wind_predictive = get_data_from_file.forecast_data()
    speed_wind_practical = get_data_from_file.observation_data()

    #get_need_data(speed_wind_predictive)
    #get_need_data(speed_wind_practical)

    winter_forecast, spring_forecast, \
    summer_forecast, autumn_forecast = division_of_data_by_seasons(speed_wind_predictive)


    lead_time_forecast_winter = [
        lead_time_0_forecast_winter, lead_time_3_forecast_winter, lead_time_6_forecast_winter, 
        lead_time_9_forecast_winter, lead_time_12_forecast_winter, lead_time_15_forecast_winter, 
        lead_time_18_forecast_winter, lead_time_21_forecast_winter, lead_time_24_forecast_winter, 
        lead_time_27_forecast_winter, lead_time_30_forecast_winter, lead_time_33_forecast_winter,
        lead_time_36_forecast_winter, lead_time_39_forecast_winter, lead_time_42_forecast_winter, 
        lead_time_45_forecast_winter, lead_time_48_forecast_winter, lead_time_51_forecast_winter, 
        lead_time_54_forecast_winter, lead_time_57_forecast_winter, lead_time_60_forecast_winter, 
        lead_time_63_forecast_winter, lead_time_66_forecast_winter, lead_time_69_forecast_winter,
        lead_time_72_forecast_winter, lead_time_75_forecast_winter, lead_time_78_forecast_winter] \
        = separation_data_by_lead_time(winter_forecast)

    lead_time_forecast_spring = [
        lead_time_0_forecast_spring, lead_time_3_forecast_spring, lead_time_6_forecast_spring,
        lead_time_9_forecast_spring, lead_time_12_forecast_spring, lead_time_15_forecast_spring,
        lead_time_18_forecast_spring, lead_time_21_forecast_spring, lead_time_24_forecast_spring,
        lead_time_27_forecast_spring, lead_time_30_forecast_spring, lead_time_33_forecast_spring,
        lead_time_36_forecast_spring, lead_time_39_forecast_spring, lead_time_42_forecast_spring,
        lead_time_45_forecast_spring, lead_time_48_forecast_spring, lead_time_51_forecast_spring,
        lead_time_54_forecast_spring, lead_time_57_forecast_spring, lead_time_60_forecast_spring,
        lead_time_63_forecast_spring, lead_time_66_forecast_spring, lead_time_69_forecast_spring,
        lead_time_72_forecast_spring, lead_time_75_forecast_spring, lead_time_78_forecast_spring] \
        = separation_data_by_lead_time(spring_forecast)

    lead_time_forecast_summer = [
        lead_time_0_forecast_summer, lead_time_3_forecast_summer, lead_time_6_forecast_summer,
        lead_time_9_forecast_summer, lead_time_12_forecast_summer, lead_time_15_forecast_summer,
        lead_time_18_forecast_summer, lead_time_21_forecast_summer, lead_time_24_forecast_summer,
        lead_time_27_forecast_summer, lead_time_30_forecast_summer, lead_time_33_forecast_summer,
        lead_time_36_forecast_summer, lead_time_39_forecast_summer, lead_time_42_forecast_summer,
        lead_time_45_forecast_summer, lead_time_48_forecast_summer, lead_time_51_forecast_summer,
        lead_time_54_forecast_summer, lead_time_57_forecast_summer, lead_time_60_forecast_summer,
        lead_time_63_forecast_summer, lead_time_66_forecast_summer, lead_time_69_forecast_summer,
        lead_time_72_forecast_summer, lead_time_75_forecast_summer, lead_time_78_forecast_summer] \
        = separation_data_by_lead_time(summer_forecast)

    lead_time_forecast_autumn = [
        lead_time_0_forecast_autumn, lead_time_3_forecast_autumn, lead_time_6_forecast_autumn,
        lead_time_9_forecast_autumn, lead_time_12_forecast_autumn, lead_time_15_forecast_autumn,
        lead_time_18_forecast_autumn, lead_time_21_forecast_autumn, lead_time_24_forecast_autumn,
        lead_time_27_forecast_autumn, lead_time_30_forecast_autumn, lead_time_33_forecast_autumn,
        lead_time_36_forecast_autumn, lead_time_39_forecast_autumn, lead_time_42_forecast_autumn,
        lead_time_45_forecast_autumn, lead_time_48_forecast_autumn, lead_time_51_forecast_autumn,
        lead_time_54_forecast_autumn, lead_time_57_forecast_autumn, lead_time_60_forecast_autumn,
        lead_time_63_forecast_autumn, lead_time_66_forecast_autumn, lead_time_69_forecast_autumn,
        lead_time_72_forecast_autumn, lead_time_75_forecast_autumn, lead_time_78_forecast_autumn] \
        = separation_data_by_lead_time(autumn_forecast)


    winter_practical, spring_practical, \
    summer_practical, autumn_practical = division_of_data_by_seasons(speed_wind_practical)
    
    lead_time_practical_winter = [
        lead_time_0_practical_winter, lead_time_3_practical_winter, lead_time_6_practical_winter, 
        lead_time_9_practical_winter, lead_time_12_practical_winter, lead_time_15_practical_winter, 
        lead_time_18_practical_winter, lead_time_21_practical_winter] \
        = separation_data_by_lead_time_practical(winter_practical)
    lead_time_practical_spring = [
        lead_time_0_practical_spring, lead_time_3_practical_spring, lead_time_6_practical_spring,
        lead_time_9_practical_spring, lead_time_12_practical_spring, lead_time_15_practical_spring,
        lead_time_18_practical_spring, lead_time_21_practical_spring
    ] = separation_data_by_lead_time_practical(spring_practical)
    lead_time_practical_summer = [
        lead_time_0_practical_summer, lead_time_3_practical_summer, lead_time_6_practical_summer,
        lead_time_9_practical_summer, lead_time_12_practical_summer, lead_time_15_practical_summer,
        lead_time_18_practical_summer, lead_time_21_practical_summer
    ] = separation_data_by_lead_time_practical(summer_practical)
    lead_time_practical_autumn = [
        lead_time_0_practical_autumn, lead_time_3_practical_autumn, lead_time_6_practical_autumn,
        lead_time_9_practical_autumn, lead_time_12_practical_autumn, lead_time_15_practical_autumn,
        lead_time_18_practical_autumn, lead_time_21_practical_autumn
    ] = separation_data_by_lead_time_practical(autumn_practical)

    print("Select calculation number:")
    print(10 * " " + "1. Different")
    print(10 * " " + "2. Absolute")
    print(10 * " " + "3. RMSE")
    print(10 * " " + "4. Correl coef")
    estimate = int(input("Calculation number: "))
    if estimate == 1:
        average_diff_winter = get_diff_for_season_and_lead_time(lead_time_forecast_winter, lead_time_practical_winter)
        average_diff_spring = get_diff_for_season_and_lead_time(lead_time_forecast_spring, lead_time_practical_spring)
        average_diff_summer = get_diff_for_season_and_lead_time(lead_time_forecast_summer, lead_time_practical_summer)
        average_diff_autumn = get_diff_for_season_and_lead_time(lead_time_forecast_autumn, lead_time_practical_autumn)
        print_average_diff('зимний', average_diff_winter)
        print_average_diff('весенний', average_diff_spring)
        print_average_diff('летний', average_diff_summer)
        print_average_diff('осенний', average_diff_autumn)
    if estimate == 2:
        diff = abs.cacl_abs_diff(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        abs_diff_winter = test_for_emptiness(diff_winter, abs.calc_abs(diff_winter))
        abs_diff_spring = test_for_emptiness(diff_spring, abs.calc_abs(diff_spring))
        abs_diff_summer = test_for_emptiness(diff_summer, abs.calc_abs(diff_summer))
        abs_diff_autumn = test_for_emptiness(diff_autumn, abs.calc_abs(diff_autumn))

        print(f'Абсолютная погрешность за зимний период:   {abs_diff_winter}')
        print(f'Абсолютная погрешность за весенний период: {abs_diff_spring}')
        print(f'Абсолютная погрешность за летний период:   {abs_diff_summer}')
        print(f'Абсолютная погрешность за осениий период:  {abs_diff_autumn}')
    if estimate == 3:
        diff = rmse.calc_squared_difference(speed_wind_predictive, speed_wind_practical)

        diff_winter, diff_spring, diff_summer, diff_autumn = division_of_data_by_seasons(diff)

        rmse_winter = test_for_emptiness(diff_winter, rmse.calc_rmse(diff_winter))
        rmse_spring = test_for_emptiness(diff_spring, rmse.calc_rmse(diff_spring))
        rmse_summer = test_for_emptiness(diff_summer, rmse.calc_rmse(diff_summer))
        rmse_autumn = test_for_emptiness(diff_autumn, rmse.calc_rmse(diff_autumn))

        print(f'Среднеквадратичная ошибка за зимний период:   {rmse_winter}')
        print(f'Среднеквадратичная ошибка за весенний период: {rmse_spring}')
        print(f'Среднеквадратичная ошибка за летний период:   {rmse_summer}')
        print(f'Среднеквадратичная ошибка за осениий период:  {rmse_autumn}')
    if estimate == 4:
        diff_winter_predictive, \
        diff_spring_predictive, \
        diff_summer_predictive, \
        diff_autumn_predictive = division_of_data_by_seasons(speed_wind_predictive)

        diff_winter_practical, \
        diff_spring_practical, \
        diff_summer_practical, \
        diff_autumn_practical = division_of_data_by_seasons(speed_wind_practical)

        if (len(diff_winter_predictive) and len(diff_winter_practical)) != 0:
            correl_coef_winter = correl.calc_correl_coef(diff_winter_predictive, diff_winter_practical)
        if (len(diff_spring_predictive) and len(diff_spring_practical)) != 0:
            correl_coef_spring = correl.calc_correl_coef(diff_spring_predictive, diff_spring_practical)
        if (len(diff_summer_predictive) and len(diff_summer_practical)) != 0:
            correl_coef_summer = correl.calc_correl_coef(diff_summer_predictive, diff_summer_practical)
        if (len(diff_autumn_predictive) and len(diff_autumn_practical)) != 0:
            correl_coef_autumn = correl.calc_correl_coef(diff_autumn_predictive, diff_autumn_practical)

        print(f'Коэффициент корреляции за зимний период:   {correl_coef_winter}')
        print(f'Коэффициент корреляции за весенний период: {correl_coef_spring}')
        print(f'Коэффициент корреляции за летний период:   {correl_coef_summer}')
        print(f'Коэффициент корреляции за осениий период:  {correl_coef_autumn}')


main()
