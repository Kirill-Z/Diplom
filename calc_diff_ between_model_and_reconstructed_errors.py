import calc_error
import linear_regression


def diff_error_for_season(error_model, error_recovery):
    diff = []
    print(len(error_model))
    print(len(error_recovery))
    for i in range(0, len(error_model)):
        diff_with_lead_time = [error_model[i][0]]
        diff_with_lead_time.append(error_model[i][1] - error_recovery[i][1])
        diff.append(diff_with_lead_time)
    return diff


def main():
    error_model_data_winter, error_model_data_spring, error_model_data_summer, error_model_data_autumn = calc_error.main()
    error_recovery_data_winter, error_recovery_data_spring, error_recovery_data_summer, error_recovery_data_autumn = \
        linear_regression.main()

    diff_winter = diff_error_for_season(error_model_data_winter, error_recovery_data_winter)
    diff_spring = diff_error_for_season(error_model_data_spring, error_recovery_data_spring)
    diff_summer = diff_error_for_season(error_model_data_summer, error_recovery_data_summer)
    diff_autumn = diff_error_for_season(error_model_data_autumn, error_recovery_data_autumn)

    print(diff_winter)
    print(diff_spring)
    print(diff_summer)
    print(diff_autumn)


main()

