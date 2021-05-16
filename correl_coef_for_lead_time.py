import math


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
        for j in range(0, len(data[i])):
            lead_time = data[i][j][0][11:13]
            if lead_time == '00':
                lead_time_0.append(data[i][j])
            if lead_time == '03':
                lead_time_3.append(data[i][j])
            if lead_time == '06':
                lead_time_6.append(data[i][j])
            if lead_time == '09':
                lead_time_9.append(data[i][j])
            if lead_time == '12':
                lead_time_12.append(data[i][j])
            if lead_time == '15':
                lead_time_15.append(data[i][j])
            if lead_time == '18':
                lead_time_18.append(data[i][j])
            if lead_time == '21':
                lead_time_21.append(data[i][j])
            if lead_time == '24':
                lead_time_24.append(data[i][j])
            if lead_time == '27':
                lead_time_27.append(data[i][j])
            if lead_time == '30':
                lead_time_30.append(data[i][j])
            if lead_time == '33':
                lead_time_33.append(data[i][j])
            if lead_time == '36':
                lead_time_36.append(data[i][j])
            if lead_time == '39':
                lead_time_39.append(data[i][j])
            if lead_time == '42':
                lead_time_42.append(data[i][j])
            if lead_time == '45':
                lead_time_45.append(data[i][j])
            if lead_time == '48':
                lead_time_48.append(data[i][j])
            if lead_time == '51':
                lead_time_51.append(data[i][j])
            if lead_time == '54':
                lead_time_54.append(data[i][j])
            if lead_time == '57':
                lead_time_57.append(data[i][j])
            if lead_time == '60':
                lead_time_60.append(data[i][j])
            if lead_time == '63':
                lead_time_63.append(data[i][j])
            if lead_time == '66':
                lead_time_66.append(data[i][j])
            if lead_time == '69':
                lead_time_69.append(data[i][j])
            if lead_time == '72':
                lead_time_72.append(data[i][j])
            if lead_time == '75':
                lead_time_75.append(data[i][j])
            if lead_time == '78':
                lead_time_78.append(data[i][j])

    return lead_time_0, lead_time_3, lead_time_6, lead_time_9, lead_time_12, lead_time_15, lead_time_18, lead_time_21, \
           lead_time_24, lead_time_27, lead_time_30, lead_time_33, lead_time_36, lead_time_39, lead_time_42, \
           lead_time_45, lead_time_48, lead_time_51, lead_time_54, lead_time_57, lead_time_60, lead_time_63, \
           lead_time_66, lead_time_69, lead_time_72, lead_time_75, lead_time_78


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
