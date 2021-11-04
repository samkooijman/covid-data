# Friso packages
from numpy.core.fromnumeric import std
from numpy.core.numeric import roll
import pandas as pd
import numpy as np 

import datetime
import openpyxl
from scipy import stats
from pandas.core.window import rolling

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  
from sklearn import metrics

import matplotlib.pyplot as plt
import itertools

# Functions
def flatten_list (x):
    flat_list = []
    for sublist in x:
        for item in sublist:
            flat_list.append(item)
    return flat_list
     
def onlysunday(x):
    x = x[x['date'].dt.day_name() == 'Sunday']
    return x

def transpose(x):
    new = np.zeros(shape=(3,3))
    for date in x['date']:
        temp = x[x['date'] == date].T.iloc[2:].reset_index()
        temp['date'] = date
        temp = temp.to_numpy()
        new = np.append(new, temp, axis=0)
    df = pd.DataFrame(data=new, columns=['region', 'vaccination_coverage', 'date'])
    return df.iloc[3:]

# Importing stringency index
stringency_index = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/stringencyindex/covid-stringency-index.csv", delimiter=',')

# Dividing stringency index
usa_stringency_index = stringency_index[stringency_index['Entity'] == 'United States']
uk_stringency_index = stringency_index[stringency_index['Entity'] == 'United Kingdom']

# renaming columns
usa_stringency_index = usa_stringency_index.rename(columns={'Day' : 'date'})
uk_stringency_index = uk_stringency_index.rename(columns={'Day' : 'date'})

# Changing types
usa_stringency_index['date'] = pd.to_datetime(usa_stringency_index['date'])
uk_stringency_index['date'] = pd.to_datetime(uk_stringency_index['date'])

# Importing vaccination coverage 
usa_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/vacc_usa.csv",  encoding= 'unicode_escape', delimiter=",")
uk_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_uk_vacc.csv")


# Prepping usa_vac
usa_vac = usa_vac.rename(columns=str.lower)
usa_vac = usa_vac.rename(columns={"location" : "state"})
usa_vac = usa_vac.iloc[: , [0, 2, 42]]
usa_vac['date'] = pd.to_datetime(usa_vac['date'])
usa_vac = usa_vac.groupby(['date', 'state'], as_index=False).sum();

# prepping uk_vac
uk_vac = uk_vac.rename(columns={'weekly_period_end' : 'date'})
uk_vac['date'] = pd.to_datetime(uk_vac['date'], format='%d-%m-%Y')
uk_vac = transpose(uk_vac)
uk_vac['vaccination_coverage'] = pd.to_numeric(uk_vac['vaccination_coverage'])
uk_vac = uk_vac.sort_values(by=['date'])

# calculating average vaccination coverage via regional vaccination coverage, per day
uk_average_vaccination_coverage = []
for date in uk_vac['date']:
    dataframe = uk_vac[uk_vac['date'] == date]
    avg = dataframe['vaccination_coverage'].mean()
    uk_average_vaccination_coverage = uk_average_vaccination_coverage + [avg]
uk_vac['average_vaccination_coverage'] = uk_average_vaccination_coverage
uk_temp = uk_vac[['date', 'average_vaccination_coverage']]

usa_average_vaccination_coverage = []
for date in usa_vac['date']:
    dataframe = usa_vac[usa_vac['date'] == date]
    avg = dataframe['series_complete_pop_pct'].mean()
    usa_average_vaccination_coverage = usa_average_vaccination_coverage + [avg]
usa_vac['average_vaccination_coverage'] = usa_average_vaccination_coverage
usa_temp = usa_vac[['date', 'average_vaccination_coverage']]

# changing type 
uk_temp['date'] = pd.to_datetime(uk_temp['date'])

# Merging
uk_stringency_index = pd.merge(uk_stringency_index, uk_temp, on='date')
usa_stringency_index = pd.merge(usa_stringency_index, usa_temp, on='date')

# Dropping duplicates
uk_stringency_index = uk_stringency_index.drop_duplicates(subset = ["date"])
usa_stringency_index = usa_stringency_index.drop_duplicates(subset = ["date"])

# # Calculated growth in vaccin rate per day
uk_stringency_index['rate_of_change'] = uk_stringency_index['average_vaccination_coverage'].diff().fillna(0)
usa_stringency_index['rate_of_change'] = usa_stringency_index['average_vaccination_coverage'].diff().fillna(0)

# Only take sundays into account
uk_stringency_index = onlysunday(uk_stringency_index)
usa_stringency_index = onlysunday(usa_stringency_index)

# Drop dates before 01-12-2020
uk_stringency_index = uk_stringency_index[uk_stringency_index['date'] > '2020-12-01']
usa_stringency_index = usa_stringency_index[usa_stringency_index['date'] > '2020-12-01']

# Linear regrssion UK
x = uk_stringency_index['stringency_index'].values
y = uk_stringency_index['rate_of_change'].values

x_ready = x.reshape((-1,1))
X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.2, random_state=0) 
regressor = LinearRegression()
regressor.fit(X_train, y_train)
coef = regressor.coef_
y_pred = regressor.predict(X_test)
error = metrics.mean_absolute_error(y_test, y_pred)
X_train = flatten_list(X_train)
slope, intercept, r_value, p_value, std_err = stats.linregress(X_train, y_train)

uk_stringency_index['coef'] = [coef[0]] * len(uk_stringency_index['date'])
uk_stringency_index['intersect'] = [regressor.intercept_] * len(uk_stringency_index['date'])
uk_stringency_index['error_rate'] = [error] * len(uk_stringency_index['date'])
uk_stringency_index['p_value'] = [p_value] * len(uk_stringency_index['date'])

# Linear regrssion USA
x = usa_stringency_index['stringency_index'].values
y = usa_stringency_index['rate_of_change'].values

x_ready = x.reshape((-1,1))
X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.2, random_state=0) 
regressor = LinearRegression()
regressor.fit(X_train, y_train)
coef = regressor.coef_
y_pred = regressor.predict(X_test)
error = metrics.mean_absolute_error(y_test, y_pred)
X_train = flatten_list(X_train)
slope, intercept, r_value, p_value, std_err = stats.linregress(X_train, y_train)

usa_stringency_index['coef'] = [coef[0]] * len(usa_stringency_index['date'])
usa_stringency_index['intersect'] = [regressor.intercept_] * len(usa_stringency_index['date'])
usa_stringency_index['error_rate'] = [error] * len(usa_stringency_index['date'])
usa_stringency_index['p_value'] = [p_value] * len(usa_stringency_index['date'])

print(uk_stringency_index)
print(usa_stringency_index)

# Dashboard





