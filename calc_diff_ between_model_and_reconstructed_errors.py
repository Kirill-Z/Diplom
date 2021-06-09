import calc_error
import linear_regression
import matplotlib.pyplot as plt


def diff_error_for_season(error_model, error_recovery):
    diff = []
    for i in range(0, len(error_model)):
        diff_with_lead_time = [error_model[i][0], error_model[i][1] - error_recovery[i][1]]
        diff.append(diff_with_lead_time)
    return diff


def plot_error(error_data_season_model, error_data_season_recovery, label_model, label_recovery):
    x_data_model = []
    y_data_model = []
    for i in range(0, len(error_data_season_model)):
        x_data_model.append(error_data_season_model[i][0])
        y_data_model.append(error_data_season_model[i][1])
    plt.subplots_adjust(bottom=0.24, top=0.95)
    plt.xticks(x_data_model, fontsize=28)
    plt.yticks(fontsize=28)
    plt.scatter(x_data_model, y_data_model, linewidths=8)
    plt.plot(x_data_model, y_data_model, label=label_model, linewidth=6)

    x_data_recovery = []
    y_data_recovery = []
    for i in range(0, len(error_data_season_recovery)):
        x_data_recovery.append(error_data_season_recovery[i][0])
        y_data_recovery.append(error_data_season_recovery[i][1])
    plt.xlabel('Заблаговременность', fontsize=32)
    plt.ylabel('Оценка', fontsize=32)
    plt.title('', fontsize=32)
    plt.scatter(x_data_recovery, y_data_recovery, c='red', linewidths=4)
    plt.plot(x_data_recovery, y_data_recovery, label=label_recovery, linestyle='-.', linewidth=4, c='red')
    plt.legend(fontsize=28, loc='lower center', bbox_to_anchor=(0.5, -0.35))

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
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


main()

