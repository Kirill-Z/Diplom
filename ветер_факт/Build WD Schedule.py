import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt

cwd = os.getcwd()

os.chdir("/home/ubuntu/Desktop/Diplom/ветер_факт")  # Прописываем путь до директории с файлом Excel

file = 'USDD_2015_01 (1).xlsx'
x1 = pd.ExcelFile(file)  # Чтение Excel таблицы в DataFrame
df1 = x1.parse('USDD_2015_01', usecols=[0, 1, 2, 3, 4, 6])  # Выбирем sheet с которым будем работать

data = df1.values.tolist()  # Переводим DateFrame в список

lengthData = len(data)  # Получаем длину списка

for i in range(lengthData):  # Объединяем строки даты и времени в в один элемент списка
    data[i][0] = str(data[i][0])+'-'+str(data[i][1])+'-'+str(data[i][2])+'-'+str(data[i][3])+':'+str(data[i][4])
    del data[i][4]
    del data[i][3]
    del data[i][2]
    del data[i][1]

fmt = dates.DateFormatter('%Y-%m-%d-%H:%M')

data_for_delete = []
x_data = []
y_data = []
for i in range(lengthData):  # Получившийся список с датой и временем в одной ячейке переводим в datetime,
    data_for_delete.append(data[i][0])  # для дальнейшей работы с форматом дата-время
    x_data.append(dt.datetime.strptime(data_for_delete[i], '%Y-%m-%d-%H:%M'))
    y_data.append(data[i][1])

plt.gca().xaxis.set_major_formatter(fmt)
plt.gca().xaxis.set_major_locator(dates.DayLocator())
plt.xlabel('Date')
plt.ylabel('Wind direction (degrees)')
plt.title('Wind Direction (degrees)')
plt.scatter(x_data, y_data, label='data')
plt.gcf().autofmt_xdate()  # Для красивой подписи даты и времени на графике
plt.show()
