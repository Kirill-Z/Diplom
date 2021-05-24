x = 0.0+1.0+1.0+1.0+1.0+3.585786437626905+1.0+1.0+1.0+-1.0+1.0+2.0+3.0+0.5857864376269049+-0.41421356237309515+0.0+1.0+0.0+0.5857864376269049+-1.0+0.0+0.0+0.0+-0.41421356237309515+2.0+2.585786437626905+6.0+2.0+0.0+0.0+-1.0+3.0+1.0+2.0+0.0+5.0+4.585786437626905+0.7639320225002102+2.0+3.0+3.0+2.0+4.0+1.0+0.0+-1.0+-2.23606797749979+0.0+3.0+1.0+2.585786437626905+-1.0+1.0+1.5857864376269049+3.585786437626905+0.5857864376269049+1.0+2.0+6.0+3.0+-1.2360679774997898+0.0+3.0+-3.0990195135927845+1.0+2.0+1.0+1.0+1.0+0.0+-2.0+0.5857864376269049+3.0+7.0+2.0+1.0+3.6148351928654963+7.0+2.0+3.0+1.5857864376269049+6.0+0.0+-1.0+4.0+6.0+1.5857864376269049+-1.2360679774997898+1.5857864376269049+-2.0+-1.2360679774997898+-0.41421356237309515+-4.0+1.0+1.0+0.0+-1.2360679774997898+-2.23606797749979+2.585786437626905+0.0+3.0+5.0+1.0+-1.0+1.0+-2.8284271247461903+1.0+2.0+2.0+2.0+2.76393202250021+-4.4031242374328485+-1.2360679774997898+0.0+0.0+1.0+3.0+4.0+0.5857864376269049+0.0+-0.16227766016837952+2.0+1.7639320225002102+3.0+-1.4142135623730951+-0.8284271247461903+1.0+2.0+5.0+3.0+2.585786437626905+6.0+4.0+-2.3851648071345037+5.17157287525381+3.0+3.0+2.0+-2.0+-2.23606797749979+2.0+2.0+0.0+0.0+-1.8284271247461903+-3.1622776601683795+-5.0+5.0+-4.0+3.0+1.0+4.0+4.0+2.0+0.0+0.0+0.0+2.0+1.0+0.0+4.0+2.0+1.0+0.0+1.0+2.0+0.7639320225002102+0.0+0.0+2.0+1.5857864376269049+2.0+1.0+1.0+0.0+1.0+0.0+2.0+3.0+2.0+3.0+2.0+2.0+-1.0+1.0+0.0+0.0+1.0+2.0+1.0+-1.0+-1.4142135623730951+1.0+0.0+-1.4142135623730951+0.0+1.0+2.0+0.0+2.0+4.0+1.0+2.0+3.0+1.5857864376269049+1.0+2.0+3.0+4.0+1.0+1.0+1.0+0.0+1.0+1.0+0.0+1.0+0.0+2.0+0.0+3.0+-12.727922061357855+1.0+-4.0+-2.0+1.0+2.0+2.0+1.0+1.0+1.0+1.0+3.0+1.0+2.0+1.0+1.5857864376269049+2.0+1.0+1.0+4.0+3.0+4.0+1.0+1.0+0.0+0.0+2.0+0.0+-1.0+-1.0+1.0+3.0+2.0+4.0+4.0+2.0+0.0+0.0+1.0+1.0+-1.4142135623730951+0.0+0.0+0.0+2.0+1.0+1.0+2.0+1.0+1.0+0.0+-0.41421356237309515+1.0+1.7639320225002102+1.0+2.0+3.0+2.0+1.0+4.0+2.0+0.0+4.0+1.0+1.0+1.0+1.0+5.0+2.0+1.0+1.0+3.0+2.0+2.0+1.0+2.0+5.0+2.0+3.0+5.0+0.7639320225002102+1.0+0.0+2.0+3.0+4.585786437626905+4.0+2.0+5.0+1.5857864376269049+2.585786437626905+6.0+3.0+3.585786437626905+2.0+2.0+1.0+1.0+3.0+2.0+1.0+2.0+1.0+1.0+-1.0+4.0+4.585786437626905+4.0+9.0+8.585786437626904+5.0+7.0+3.0+5.0+2.76393202250021+2.0+2.0+4.0+7.585786437626905+3.0+4.585786437626905+2.585786437626905+4.0+5.0+5.0+5.0+12.0+7.0+3.585786437626905+3.0+2.0+1.0+3.0+6.0+9.0+1.0+3.0+-1.0+4.0+5.0+0.5857864376269049+3.585786437626905+4.0+6.0+7.0
print(x/365)
    # Summer
'''    lead_time = 0
    for i in range(0, 8):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i], b0_summer[i],
                          b1_summer[i], lead_time, 'Летний период')
        lead_time += 3
    for i in range(8, 10):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 8], b0_summer[i],
                          b1_summer[i], lead_time, 'Летний период')
        lead_time += 3
    for i in range(10, 18):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 10],
                          b0_summer[i - 10],
                          b1_summer[i - 10], lead_time, 'Летний период')
        lead_time += 3
    for i in range(18, 20):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 16],
                          b0_summer[i - 10], b1_summer[i - 10], lead_time, 'Летний период')
        lead_time += 3
    for i in range(20, 24):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 16],
                          b0_summer[i - 20], b1_summer[i - 20], lead_time, 'Летний период')
        lead_time += 3
    for i in range(24, 27):
        linear_regression(lead_time_forecast_summer_test[i], lead_time_observation_summer_test[i - 24],
                          b0_summer[i - 20], b1_summer[i - 20], lead_time, 'Летний период')
        lead_time += 3'''

    # Winter
    '''lead_time = 0
    for i in range(0, 8):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i], b0_winter[i], b1_winter[i], lead_time, 'Зимний период')
        lead_time += 3
    for i in range(8, 10):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-8], b0_winter[i], b1_winter[i], lead_time, 'Зимний период')
        lead_time += 3
    for i in range(10, 18):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-10], b0_winter[i-10],
                          b1_winter[i-10], lead_time, 'Зимний период')
        lead_time += 3
    for i in range(18, 20):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i-16], b0_winter[i-10], b1_winter[i-10], lead_time, 'Зимний период')
        lead_time += 3
    for i in range(20, 24):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i - 16],
                          b0_winter[i - 20], b1_winter[i - 20], lead_time, 'Зимний период')
        lead_time += 3
    for i in range(24, 27):
        linear_regression(lead_time_forecast_winter_test[i], lead_time_observation_winter_test[i - 24],
                          b0_winter[i - 20], b1_winter[i - 20], lead_time, 'Зимний период')
        lead_time += 3'''

    # Spring
'''    lead_time = 0
    for i in range(0, 8):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i], b0_spring[i],
                          b1_spring[i], lead_time, 'Весенний период')
        lead_time += 3
    for i in range(8, 10):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 8], b0_spring[i],
                          b1_spring[i], lead_time, 'Весенний период')
        lead_time += 3
    for i in range(10, 18):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 10],
                          b0_spring[i - 10],
                          b1_spring[i - 10], lead_time, 'Весенний период')
        lead_time += 3
    for i in range(18, 20):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 16],
                          b0_spring[i - 10], b1_spring[i - 10], lead_time, 'Весенний период')
        lead_time += 3
    for i in range(20, 24):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 16],
                          b0_spring[i - 20], b1_spring[i - 20], lead_time, 'Весенний период')
        lead_time += 3
    for i in range(24, 27):
        linear_regression(lead_time_forecast_spring_test[i], lead_time_observation_spring_test[i - 24],
                          b0_spring[i - 20], b1_spring[i - 20], lead_time, 'Весенний период')
        lead_time += 3'''

# Autumn

lead_time = 0
for i in range(0, 8):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i], b0_autumn[i],
                      b1_autumn[i], lead_time, 'Осенний период')
    lead_time += 3
for i in range(8, 10):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 8], b0_autumn[i],
                      b1_autumn[i], lead_time, 'Осенний период')
    lead_time += 3
for i in range(10, 18):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 10],
                      b0_autumn[i - 10],
                      b1_autumn[i - 10], lead_time, 'Осенний период')
    lead_time += 3
for i in range(18, 20):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 16],
                      b0_autumn[i - 10], b1_autumn[i - 10], lead_time, 'Осенний период')
    lead_time += 3
for i in range(20, 24):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 16],
                      b0_autumn[i - 20], b1_autumn[i - 20], lead_time, 'Осенний период')
    lead_time += 3
for i in range(24, 27):
    linear_regression(lead_time_forecast_autumn_test[i], lead_time_observation_autumn_test[i - 24],
                      b0_autumn[i - 20], b1_autumn[i - 20], lead_time, 'Осенний период')
    lead_time += 3
