import calc_error
import linear_regression
import matplotlib.pyplot as plt


def diff_error_for_season(error_model, error_recovery):
    diff = []
    print(len(error_model))
    print(len(error_recovery))
    for i in range(0, len(error_model)):
        diff_with_lead_time = [error_model[i][0]]
        diff_with_lead_time.append(error_model[i][1] - error_recovery[i][1])
        diff.append(diff_with_lead_time)
    return diff


def plot_error(error_data_season_model, error_data_season_recovery, label_model, label_recovery):
    x_data_model = []
    y_data_model = []
    for i in range(0, len(error_data_season_model)):
        x_data_model.append(error_data_season_model[i][0])
        y_data_model.append(error_data_season_model[i][1])
    plt.xticks(x_data_model, fontsize=28)
    plt.yticks(fontsize=28)
    plt.scatter(x_data_model, y_data_model)
    plt.plot(x_data_model, y_data_model, label=label_model)

    x_data_recovery = []
    y_data_recovery = []
    for i in range(0, len(error_data_season_recovery)):
        x_data_recovery.append(error_data_season_recovery[i][0])
        y_data_recovery.append(error_data_season_recovery[i][1])
    plt.xlabel('Заблаговременность', fontsize=32)
    plt.ylabel('Оценка', fontsize=32)
    plt.title('Коэффициент корреляции', fontsize=32)
    plt.scatter(x_data_recovery, y_data_recovery, c='red')
    plt.plot(x_data_recovery, y_data_recovery, label=label_recovery, linestyle='-.', c='red')
    plt.legend(fontsize=28, loc='lower center', bbox_to_anchor=(0.5, -0.35))
    plt.show()


def main():
    error_model_data_winter, error_model_data_spring, error_model_data_summer, error_model_data_autumn = calc_error.main()
    error_recovery_data_winter, error_recovery_data_spring, error_recovery_data_summer, error_recovery_data_autumn = \
        linear_regression.main()

    plot_error(error_model_data_winter, error_recovery_data_winter,
               'Зимний период для модельных данных',
               'Зимний период для восстановленных данных')
    plot_error(error_model_data_spring, error_recovery_data_spring,
               'Весенний период для модельных данных',
               'Весенний период для восстановленных данных')
    plot_error(error_model_data_summer, error_recovery_data_summer,
               'Летний период для модельных данных',
               'Летний период для восстановленных данных')
    plot_error(error_model_data_autumn, error_recovery_data_autumn,
               'Осенний период для модельных данных',
               'Осенний период для восстановленных данных')


    diff_winter = diff_error_for_season(error_model_data_winter, error_recovery_data_winter)
    diff_spring = diff_error_for_season(error_model_data_spring, error_recovery_data_spring)
    diff_summer = diff_error_for_season(error_model_data_summer, error_recovery_data_summer)
    diff_autumn = diff_error_for_season(error_model_data_autumn, error_recovery_data_autumn)

    print(diff_winter)
    print(diff_spring)
    print(diff_summer)
    print(diff_autumn)


main()

