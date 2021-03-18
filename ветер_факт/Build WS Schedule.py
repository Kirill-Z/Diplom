import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates
import datetime as dt

cwd = os.getcwd()

os.chdir("/home/ubuntu/Desktop/Diplom/ветер_факт")

file = 'USDD_2015_01 (1).xlsx'
x1 = pd.ExcelFile(file)
df1 = x1.parse('USDD_2015_01', usecols=[0, 1, 2, 3, 4, 7])

data = df1.values.tolist()

lengthData = len(data)

for i in range(lengthData):
    data[i][0] = str(data[i][0])+'-'+str(data[i][1])+'-'+str(data[i][2])+'-'+str(data[i][3])+':'+str(data[i][4])
    del data[i][4]
    del data[i][3]
    del data[i][2]
    del data[i][1]

fmt = dates.DateFormatter('%Y-%m-%d-%H:%M')

data_for_delete = []
x_data = []
y_data = []
for i in range(lengthData):
    data_for_delete.append(data[i][0])
    x_data.append(dt.datetime.strptime(data_for_delete[i], '%Y-%m-%d-%H:%M'))
    y_data.append(data[i][1])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d-%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xlabel('Date')
plt.ylabel('Wind speed (m/s)')
plt.title('Wind Speed (m/s)')
plt.scatter(x_data, y_data, label='data')
plt.gcf().autofmt_xdate()
plt.show()
