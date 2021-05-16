import math


def calc_correl_coef(speed_wind_predictive, speed_wind_practical):
    x_avg = 0
    y_avg = 0

    if len(speed_wind_predictive) < len(speed_wind_practical):
        lenght = int(len(speed_wind_predictive))
    elif len(speed_wind_practical) < len(speed_wind_predictive):
        lenght = int(len(speed_wind_practical))
    else:
        lenght = int(len(speed_wind_predictive))


    for i in range(0, lenght):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            x_avg += speed_wind_practical[i][1]
            y_avg += speed_wind_predictive[i][1]
    x_avg /= len(speed_wind_predictive)
    y_avg /= len(speed_wind_predictive)

    numerator = 0
    x = 0
    y = 0
    for i in range(0, lenght):
        if float(speed_wind_predictive[i][1]) >= 9999 or math.isnan(float(speed_wind_practical[i][1])):
            continue
        else:
            numerator += (speed_wind_practical[i][1] - x_avg)*(speed_wind_predictive[i][1] - y_avg)
            x += (speed_wind_practical[i][1] - x_avg)**2
            y += (speed_wind_predictive[i][1] - y_avg)**2
    denominator = math.sqrt(x*y)
    correl_coef = numerator / denominator

    return correl_coef
