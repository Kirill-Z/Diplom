import pandas as pd
import wind_forecast
import practical_wind_forecast
import difference_for_lead_time as difference
import abs_error_for_lead_time as abs
import root_mean_square_error_for_lead_time as rmse
import correl_coef_for_lead_time as correl

def write_in_speed_predictive(lead_time: str, speed_wind_predictive):
    local_speed_wind = []
    for i in range(0, len(speed_wind_predictive)):
        if speed_wind_predictive[i][0][11:13] == lead_time:
            local_speed_wind.append(speed_wind_predictive[i])
    return local_speed_wind


def get_forecat_data():
    tmp = input('Press 1 if you want to calculate values')
    if tmp == "1":
        value = input(
            "Forecast data: If you need to calculate a point, press 1, if you need to calculate an area, press 2: ")
        if value == '1':
            wind_forecast.main_for_difference_lead_time(value)
        elif value == '2':
            wind_forecast.main_for_difference_lead_time(value)

    current_file = "/home/kirill/Downloads/Data/gfs/list_data"  # Path to the predicted wind speed file
    file_reader = pd.read_csv(current_file, sep=';', header=None, engine='python')
    speed_wind_predictive_true = []
    speed_wind_predictive = file_reader.values.tolist()

    lead_time = (
        '00', '03', '06', '09', '12', '15', '18', '21', '24', '27', '30', '33', '36', '39', '42', '45', '48', '51',
        '54', '57', '60', '63', '66', '69', '72', '75', '78')

    for i in lead_time:
        speed_wind_predictive_true.append(write_in_speed_predictive(i, speed_wind_predictive))
    return speed_wind_predictive_true


def get_observation_data():
    speed_wind_practical = practical_wind_forecast.main('1')
    return speed_wind_practical


def main():
    speed_wind_predictive_true = get_forecat_data()
    speed_wind_practical = get_observation_data()

    diff_0_lead_time = []
    diff_3_lead_time = []
    diff_6_lead_time = []
    diff_9_lead_time = []
    diff_12_lead_time = []
    diff_15_lead_time = []
    diff_18_lead_time = []
    diff_21_lead_time = []
    diff_24_lead_time = []
    diff_27_lead_time = []
    diff_30_lead_time = []
    diff_33_lead_time = []
    diff_36_lead_time = []
    diff_39_lead_time = []
    diff_42_lead_time = []
    diff_45_lead_time = []
    diff_48_lead_time = []
    diff_51_lead_time = []
    diff_54_lead_time = []
    diff_57_lead_time = []
    diff_60_lead_time = []
    diff_63_lead_time = []
    diff_66_lead_time = []
    diff_69_lead_time = []
    diff_72_lead_time = []
    diff_75_lead_time = []
    diff_78_lead_time = []

    print("Select calculation number:")
    print(10 * " " + "1. Different")
    print(10 * " " + "2. Absolute")
    print(10 * " " + "3. RMSE")
    print(10 * " " + "4. Correl coef")
    estimate = int(input())
    if estimate == 1:
        for i in range(0, len(speed_wind_predictive_true)):
            for j in range(0, len(speed_wind_predictive_true[i])):
                diff_0_lead_time = difference.calc_diff('00', diff_0_lead_time, speed_wind_predictive_true,
                                                        speed_wind_practical,
                                                        i, j)
                diff_3_lead_time = difference.calc_diff('03', diff_3_lead_time, speed_wind_predictive_true,
                                                        speed_wind_practical,
                                                        i, j)
                diff_6_lead_time = difference.calc_diff('06', diff_6_lead_time, speed_wind_predictive_true,
                                                        speed_wind_practical,
                                                        i, j)
                diff_9_lead_time = difference.calc_diff('09', diff_9_lead_time, speed_wind_predictive_true,
                                                        speed_wind_practical,
                                                        i, j)
                diff_12_lead_time = difference.calc_diff('12', diff_12_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_15_lead_time = difference.calc_diff('15', diff_15_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_18_lead_time = difference.calc_diff('18', diff_18_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_21_lead_time = difference.calc_diff('21', diff_21_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_24_lead_time = difference.calc_diff('24', diff_24_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_27_lead_time = difference.calc_diff('27', diff_27_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_30_lead_time = difference.calc_diff('30', diff_30_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_33_lead_time = difference.calc_diff('33', diff_33_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_36_lead_time = difference.calc_diff('36', diff_36_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_39_lead_time = difference.calc_diff('39', diff_39_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_42_lead_time = difference.calc_diff('42', diff_42_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_45_lead_time = difference.calc_diff('45', diff_45_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_48_lead_time = difference.calc_diff('48', diff_48_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_51_lead_time = difference.calc_diff('51', diff_51_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_54_lead_time = difference.calc_diff('54', diff_54_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_57_lead_time = difference.calc_diff('57', diff_57_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_60_lead_time = difference.calc_diff('60', diff_60_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_63_lead_time = difference.calc_diff('63', diff_63_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_66_lead_time = difference.calc_diff('66', diff_66_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_69_lead_time = difference.calc_diff('69', diff_69_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_72_lead_time = difference.calc_diff('72', diff_72_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_75_lead_time = difference.calc_diff('75', diff_75_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)
                diff_78_lead_time = difference.calc_diff('78', diff_78_lead_time, speed_wind_predictive_true,
                                                         speed_wind_practical,
                                                         i, j)

        average_diff_0 = difference.calc_the_average_diff(diff_0_lead_time)
        average_diff_3 = difference.calc_the_average_diff(diff_3_lead_time)
        average_diff_6 = difference.calc_the_average_diff(diff_6_lead_time)
        average_diff_9 = difference.calc_the_average_diff(diff_9_lead_time)
        average_diff_12 = difference.calc_the_average_diff(diff_12_lead_time)
        average_diff_15 = difference.calc_the_average_diff(diff_15_lead_time)
        average_diff_18 = difference.calc_the_average_diff(diff_18_lead_time)
        average_diff_21 = difference.calc_the_average_diff(diff_21_lead_time)
        average_diff_24 = difference.calc_the_average_diff(diff_24_lead_time)
        average_diff_27 = difference.calc_the_average_diff(diff_27_lead_time)
        average_diff_30 = difference.calc_the_average_diff(diff_30_lead_time)
        average_diff_33 = difference.calc_the_average_diff(diff_33_lead_time)
        average_diff_36 = difference.calc_the_average_diff(diff_36_lead_time)
        average_diff_39 = difference.calc_the_average_diff(diff_39_lead_time)
        average_diff_42 = difference.calc_the_average_diff(diff_42_lead_time)
        average_diff_45 = difference.calc_the_average_diff(diff_45_lead_time)
        average_diff_48 = difference.calc_the_average_diff(diff_48_lead_time)
        average_diff_51 = difference.calc_the_average_diff(diff_51_lead_time)
        average_diff_54 = difference.calc_the_average_diff(diff_54_lead_time)
        average_diff_57 = difference.calc_the_average_diff(diff_57_lead_time)
        average_diff_60 = difference.calc_the_average_diff(diff_60_lead_time)
        average_diff_63 = difference.calc_the_average_diff(diff_63_lead_time)
        average_diff_66 = difference.calc_the_average_diff(diff_66_lead_time)
        average_diff_69 = difference.calc_the_average_diff(diff_69_lead_time)
        average_diff_72 = difference.calc_the_average_diff(diff_72_lead_time)
        average_diff_75 = difference.calc_the_average_diff(diff_75_lead_time)
        average_diff_78 = difference.calc_the_average_diff(diff_78_lead_time)

        difference.print_average_diff('0 часов', average_diff_0)
        difference.print_average_diff('3 часа', average_diff_3)
        difference.print_average_diff('6 часов', average_diff_6)
        difference.print_average_diff('9 часов', average_diff_9)
        difference.print_average_diff('12 часов', average_diff_12)
        difference.print_average_diff('15 часов', average_diff_15)
        difference.print_average_diff('18 часов', average_diff_18)
        difference.print_average_diff('21 час', average_diff_21)
        difference.print_average_diff('24 часа', average_diff_24)
        difference.print_average_diff('27 часов', average_diff_27)
        difference.print_average_diff('30 часов', average_diff_30)
        difference.print_average_diff('33 часа', average_diff_33)
        difference.print_average_diff('36 часов', average_diff_36)
        difference.print_average_diff('39 часов', average_diff_39)
        difference.print_average_diff('42 часа', average_diff_42)
        difference.print_average_diff('45 часов', average_diff_45)
        difference.print_average_diff('48 часов', average_diff_48)
        difference.print_average_diff('51 час', average_diff_51)
        difference.print_average_diff('54 часа', average_diff_54)
        difference.print_average_diff('57 часов', average_diff_57)
        difference.print_average_diff('60 часов', average_diff_60)
        difference.print_average_diff('63 часа', average_diff_63)
        difference.print_average_diff('66 часов', average_diff_66)
        difference.print_average_diff('69 часов', average_diff_69)
        difference.print_average_diff('72 часа', average_diff_72)
        difference.print_average_diff('75 часов', average_diff_75)
        difference.print_average_diff('78 часов', average_diff_78)
    if estimate == 2:
        for i in range(0, len(speed_wind_predictive_true)):
            for j in range(0, len(speed_wind_predictive_true[i])):
                diff_0_lead_time = abs.calc_abs_diff('00', diff_0_lead_time, speed_wind_predictive_true,
                                                     speed_wind_practical, i, j)
                diff_3_lead_time = abs.calc_abs_diff('03', diff_3_lead_time, speed_wind_predictive_true,
                                                     speed_wind_practical, i, j)
                diff_6_lead_time = abs.calc_abs_diff('06', diff_6_lead_time, speed_wind_predictive_true,
                                                     speed_wind_practical, i, j)
                diff_9_lead_time = abs.calc_abs_diff('09', diff_9_lead_time, speed_wind_predictive_true,
                                                     speed_wind_practical, i, j)
                diff_12_lead_time = abs.calc_abs_diff('12', diff_12_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_15_lead_time = abs.calc_abs_diff('15', diff_15_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_18_lead_time = abs.calc_abs_diff('18', diff_18_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_21_lead_time = abs.calc_abs_diff('21', diff_21_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_24_lead_time = abs.calc_abs_diff('24', diff_24_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_27_lead_time = abs.calc_abs_diff('27', diff_27_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_30_lead_time = abs.calc_abs_diff('30', diff_30_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_33_lead_time = abs.calc_abs_diff('33', diff_33_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_36_lead_time = abs.calc_abs_diff('36', diff_36_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_39_lead_time = abs.calc_abs_diff('39', diff_39_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_42_lead_time = abs.calc_abs_diff('42', diff_42_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_45_lead_time = abs.calc_abs_diff('45', diff_45_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_48_lead_time = abs.calc_abs_diff('48', diff_48_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_51_lead_time = abs.calc_abs_diff('51', diff_51_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_54_lead_time = abs.calc_abs_diff('54', diff_54_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_57_lead_time = abs.calc_abs_diff('57', diff_57_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_60_lead_time = abs.calc_abs_diff('60', diff_60_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_63_lead_time = abs.calc_abs_diff('63', diff_63_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_66_lead_time = abs.calc_abs_diff('66', diff_66_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_69_lead_time = abs.calc_abs_diff('69', diff_69_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_72_lead_time = abs.calc_abs_diff('72', diff_72_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_75_lead_time = abs.calc_abs_diff('75', diff_75_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)
                diff_78_lead_time = abs.calc_abs_diff('78', diff_78_lead_time, speed_wind_predictive_true,
                                                      speed_wind_practical, i, j)

        abs_0 = abs.calc_abs(diff_0_lead_time)
        abs_3 = abs.calc_abs(diff_3_lead_time)
        abs_6 = abs.calc_abs(diff_6_lead_time)
        abs_9 = abs.calc_abs(diff_9_lead_time)
        abs_12 = abs.calc_abs(diff_12_lead_time)
        abs_15 = abs.calc_abs(diff_15_lead_time)
        abs_18 = abs.calc_abs(diff_18_lead_time)
        abs_21 = abs.calc_abs(diff_21_lead_time)
        abs_24 = abs.calc_abs(diff_24_lead_time)
        abs_27 = abs.calc_abs(diff_27_lead_time)
        abs_30 = abs.calc_abs(diff_30_lead_time)
        abs_33 = abs.calc_abs(diff_33_lead_time)
        abs_36 = abs.calc_abs(diff_36_lead_time)
        abs_39 = abs.calc_abs(diff_39_lead_time)
        abs_42 = abs.calc_abs(diff_42_lead_time)
        abs_45 = abs.calc_abs(diff_45_lead_time)
        abs_48 = abs.calc_abs(diff_48_lead_time)
        abs_51 = abs.calc_abs(diff_51_lead_time)
        abs_54 = abs.calc_abs(diff_54_lead_time)
        abs_57 = abs.calc_abs(diff_57_lead_time)
        abs_60 = abs.calc_abs(diff_60_lead_time)
        abs_63 = abs.calc_abs(diff_63_lead_time)
        abs_66 = abs.calc_abs(diff_66_lead_time)
        abs_69 = abs.calc_abs(diff_69_lead_time)
        abs_72 = abs.calc_abs(diff_72_lead_time)
        abs_75 = abs.calc_abs(diff_75_lead_time)
        abs_78 = abs.calc_abs(diff_78_lead_time)

        abs.print_average_diff('0 часов', abs_0)
        abs.print_average_diff('3 часа', abs_3)
        abs.print_average_diff('6 часов', abs_6)
        abs.print_average_diff('9 часов', abs_9)
        abs.print_average_diff('12 часов', abs_12)
        abs.print_average_diff('15 часов', abs_15)
        abs.print_average_diff('18 часов', abs_18)
        abs.print_average_diff('21 час', abs_21)
        abs.print_average_diff('24 часа', abs_24)
        abs.print_average_diff('27 часов', abs_27)
        abs.print_average_diff('30 часов', abs_30)
        abs.print_average_diff('33 часа', abs_33)
        abs.print_average_diff('36 часов', abs_36)
        abs.print_average_diff('39 часов', abs_39)
        abs.print_average_diff('42 часа', abs_42)
        abs.print_average_diff('45 часов', abs_45)
        abs.print_average_diff('48 часов', abs_48)
        abs.print_average_diff('51 час', abs_51)
        abs.print_average_diff('54 часа', abs_54)
        abs.print_average_diff('57 часов', abs_57)
        abs.print_average_diff('60 часов', abs_60)
        abs.print_average_diff('63 часа', abs_63)
        abs.print_average_diff('66 часов', abs_66)
        abs.print_average_diff('69 часов', abs_69)
        abs.print_average_diff('72 часа', abs_72)
        abs.print_average_diff('75 часов', abs_75)
        abs.print_average_diff('78 часов', abs_78)
    if estimate == 3:
        for i in range(0, len(speed_wind_predictive_true)):
            for j in range(0, len(speed_wind_predictive_true[i])):
                diff_0_lead_time = rmse.calc_squared_difference('00', diff_0_lead_time, speed_wind_predictive_true,
                                                                speed_wind_practical, i, j)
                diff_3_lead_time = rmse.calc_squared_difference('03', diff_3_lead_time, speed_wind_predictive_true,
                                                                speed_wind_practical, i, j)
                diff_6_lead_time = rmse.calc_squared_difference('06', diff_6_lead_time, speed_wind_predictive_true,
                                                                speed_wind_practical, i, j)
                diff_9_lead_time = rmse.calc_squared_difference('09', diff_9_lead_time, speed_wind_predictive_true,
                                                                speed_wind_practical, i, j)
                diff_12_lead_time = rmse.calc_squared_difference('12', diff_12_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_15_lead_time = rmse.calc_squared_difference('15', diff_15_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_18_lead_time = rmse.calc_squared_difference('18', diff_18_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_21_lead_time = rmse.calc_squared_difference('21', diff_21_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_24_lead_time = rmse.calc_squared_difference('24', diff_24_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_27_lead_time = rmse.calc_squared_difference('27', diff_27_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_30_lead_time = rmse.calc_squared_difference('30', diff_30_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_33_lead_time = rmse.calc_squared_difference('33', diff_33_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_36_lead_time = rmse.calc_squared_difference('36', diff_36_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_39_lead_time = rmse.calc_squared_difference('39', diff_39_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_42_lead_time = rmse.calc_squared_difference('42', diff_42_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_45_lead_time = rmse.calc_squared_difference('45', diff_45_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_48_lead_time = rmse.calc_squared_difference('48', diff_48_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_51_lead_time = rmse.calc_squared_difference('51', diff_51_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_54_lead_time = rmse.calc_squared_difference('54', diff_54_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_57_lead_time = rmse.calc_squared_difference('57', diff_57_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_60_lead_time = rmse.calc_squared_difference('60', diff_60_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_63_lead_time = rmse.calc_squared_difference('63', diff_63_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_66_lead_time = rmse.calc_squared_difference('66', diff_66_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_69_lead_time = rmse.calc_squared_difference('69', diff_69_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_72_lead_time = rmse.calc_squared_difference('72', diff_72_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_75_lead_time = rmse.calc_squared_difference('75', diff_75_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)
                diff_78_lead_time = rmse.calc_squared_difference('78', diff_78_lead_time, speed_wind_predictive_true,
                                                                 speed_wind_practical, i, j)

            rmse_0 = rmse.calc_rmse(diff_0_lead_time)
            rmse_3 = rmse.calc_rmse(diff_3_lead_time)
            rmse_6 = rmse.calc_rmse(diff_6_lead_time)
            rmse_9 = rmse.calc_rmse(diff_9_lead_time)
            rmse_12 = rmse.calc_rmse(diff_12_lead_time)
            rmse_15 = rmse.calc_rmse(diff_15_lead_time)
            rmse_18 = rmse.calc_rmse(diff_18_lead_time)
            rmse_21 = rmse.calc_rmse(diff_21_lead_time)
            rmse_24 = rmse.calc_rmse(diff_24_lead_time)
            rmse_27 = rmse.calc_rmse(diff_27_lead_time)
            rmse_30 = rmse.calc_rmse(diff_30_lead_time)
            rmse_33 = rmse.calc_rmse(diff_33_lead_time)
            rmse_36 = rmse.calc_rmse(diff_36_lead_time)
            rmse_39 = rmse.calc_rmse(diff_39_lead_time)
            rmse_42 = rmse.calc_rmse(diff_42_lead_time)
            rmse_45 = rmse.calc_rmse(diff_45_lead_time)
            rmse_48 = rmse.calc_rmse(diff_48_lead_time)
            rmse_51 = rmse.calc_rmse(diff_51_lead_time)
            rmse_54 = rmse.calc_rmse(diff_54_lead_time)
            rmse_57 = rmse.calc_rmse(diff_57_lead_time)
            rmse_60 = rmse.calc_rmse(diff_60_lead_time)
            rmse_63 = rmse.calc_rmse(diff_63_lead_time)
            rmse_66 = rmse.calc_rmse(diff_66_lead_time)
            rmse_69 = rmse.calc_rmse(diff_69_lead_time)
            rmse_72 = rmse.calc_rmse(diff_72_lead_time)
            rmse_75 = rmse.calc_rmse(diff_75_lead_time)
            rmse_78 = rmse.calc_rmse(diff_78_lead_time)

            rmse.print_rmse('0 часов', rmse_0)
            rmse.print_rmse('3 часа', rmse_3)
            rmse.print_rmse('6 часов', rmse_6)
            rmse.print_rmse('9 часов', rmse_9)
            rmse.print_rmse('12 часов', rmse_12)
            rmse.print_rmse('15 часов', rmse_15)
            rmse.print_rmse('18 часов', rmse_18)
            rmse.print_rmse('21 час', rmse_21)
            rmse.print_rmse('24 часа', rmse_24)
            rmse.print_rmse('27 часов', rmse_27)
            rmse.print_rmse('30 часов', rmse_30)
            rmse.print_rmse('33 часа', rmse_33)
            rmse.print_rmse('36 часов', rmse_36)
            rmse.print_rmse('39 часов', rmse_39)
            rmse.print_rmse('42 часа', rmse_42)
            rmse.print_rmse('45 часов', rmse_45)
            rmse.print_rmse('48 часов', rmse_48)
            rmse.print_rmse('51 час', rmse_51)
            rmse.print_rmse('54 часа', rmse_54)
            rmse.print_rmse('57 часов', rmse_57)
            rmse.print_rmse('60 часов', rmse_60)
            rmse.print_rmse('63 часа', rmse_63)
            rmse.print_rmse('66 часов', rmse_66)
            rmse.print_rmse('69 часов', rmse_69)
            rmse.print_rmse('72 часа', rmse_72)
            rmse.print_rmse('75 часов', rmse_75)
            rmse.print_rmse('78 часов', rmse_78)
    if estimate == 4:
        lead_time_predictive = [
            lead_time_0_predictive, lead_time_3_predictive, lead_time_6_predictive, lead_time_9_predictive,
            lead_time_12_predictive, lead_time_15_predictive, lead_time_18_predictive, lead_time_21_predictive,
            lead_time_24_predictive, lead_time_27_predictive, lead_time_30_predictive, lead_time_33_predictive,
            lead_time_36_predictive, lead_time_39_predictive, lead_time_42_predictive, lead_time_45_predictive,
            lead_time_48_predictive, lead_time_51_predictive, lead_time_54_predictive, lead_time_57_predictive,
            lead_time_60_predictive, lead_time_63_predictive, lead_time_66_predictive, lead_time_69_predictive,
            lead_time_72_predictive, lead_time_75_predictive, lead_time_78_predictive] = correl.separation_data_by_lead_time(speed_wind_predictive_true)

        lead_time_practical = [
            lead_time_0_practical, lead_time_3_practical, lead_time_6_practical, lead_time_9_practical,
            lead_time_12_practical, lead_time_15_practical, lead_time_18_practical, lead_time_21_practical] = correl.separation_data_by_lead_time_practical(speed_wind_practical)

        #  0:8
        #  8:16
        #  16:24
        #  24:27
        a = 0
        b = 8
        for i, j in zip(lead_time_predictive[0:8], lead_time_practical):
            pass
        for i, j in zip(lead_time_predictive[8:16], lead_time_practical):
            pass
        for i, j in zip(lead_time_predictive[16:24], lead_time_practical):
            pass
        for i, j in zip(lead_time_predictive[24:27], lead_time_practical):
            pass
            #correl.calc_correl_coef(i, lead_time_0_practical)


        '''
        correl.calc_correl_coef(lead_time_0_predictive, lead_time_0_practical)
        correl.calc_correl_coef(lead_time_3_predictive, lead_time_3_practical)
        correl.calc_correl_coef(lead_time_6_predictive, lead_time_6_practical)
        correl.calc_correl_coef(lead_time_9_predictive, lead_time_9_practical)
        correl.calc_correl_coef(lead_time_12_predictive, lead_time_12_practical) 
        correl.calc_correl_coef(lead_time_15_predictive, lead_time_15_practical) 
        correl.calc_correl_coef(lead_time_18_predictive, lead_time_18_practical)
        correl.calc_correl_coef(lead_time_21_predictive, lead_time_21_practical)
        correl.calc_correl_coef(lead_time_24_predictive, lead_time_0_practical) 
        correl.calc_correl_coef(lead_time_27_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_30_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_33_predictive, lead_time__practical)
        correl.calc_correl_coef(lead_time_36_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_39_predictive, lead_time__practical)
        correl.calc_correl_coef(lead_time_42_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_45_predictive, lead_time__practical)
        correl.calc_correl_coef(lead_time_48_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_51_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_54_predictive, lead_time__practical) 
        correl.calc_correl_coef(lead_time_57_predictive, lead_time__practical)
        correl.calc_correl_coef(lead_time_60_predictive, lead_time_60_practical) 
        correl.calc_correl_coef(lead_time_63_predictive, lead_time_63_practical) 
        correl.calc_correl_coef(lead_time_66_predictive, lead_time_66_practical) 
        correl.calc_correl_coef(lead_time_69_predictive, lead_time_69_practical)
        correl.calc_correl_coef(lead_time_72_predictive, lead_time_72_practical) 
        correl.calc_correl_coef(lead_time_75_predictive, lead_time_75_practical) 
        correl.calc_correl_coef(lead_time_78_predictive, lead_time_78_practical)
        '''

main()
