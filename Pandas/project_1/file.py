import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Читаем данные по рейсам
flights = pd.read_csv('flights.csv',
                     parse_dates=['time_hour'], # разобрать дату
                     dtype={'carrier' : 'str' # код перевозчика - текст
                           })  

#Читаем список авиакомпаний
airlines = pd.read_csv('airlines.csv', 
                      dtype={'carrier':'str'}) # код перевозчика - текст
airlines.rename({'name':'airline'}, axis='columns', inplace=True)

#Присоединяем авиакомпании:
flights = pd.merge(flights, airlines, on='carrier', how='left')

flights.head()
flights.info()



#TASK 1
col_list=["dep_time","dep_delay","air_time"]
df = pd.read_csv("flights.csv", usecols=col_list)
#saved_column = df.arr_time
print (df)
dp_time = df["dep_time"].between(000, 559, inclusive = True) 
ar_time=df["air_time"].between(50,1000000, inclusive = True) 
dp_delay=df["dep_delay"].between(-1000,60, inclusive = True) 
print (df[dp_time][ar_time][dp_delay]) #время вылета от 0 00 до 5 59 
# время задержки меньше 60 минут 
# время в полете больше 50 минут !


#TASK 2
dest=(flights['dest'].isin(['IAH', 'HOU']))
fligh=flights['airline'].isin(['Delta Air Lines Inc.', 'American Airlines Inc.', 'United Air Lines Inc.'])
dates=(flights['year'] == 2013) & (flights['month'].between(6, 8)) 
delays=(flights['dep_delay'] <= 0) & (flights['arr_delay'] > 60)

print (flights[dest][fligh][dates][delays])


#TASK 3
