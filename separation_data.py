def separation_of_data_by_seasons(diff):
    winter = []
    spring = []
    summer = []
    autumn = []

    for i in range(0, len(diff)):
        month = str(diff[i][0][4:6])
        if month in ('11', '12', '01', '02', '03'):
            winter.append(diff[i])

        if month in ('04', '05'):
            spring.append(diff[i])

        if month in ('06', '07', '08'):
            summer.append(diff[i])

        if month in ('09', '10'):
            autumn.append(diff[i])
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