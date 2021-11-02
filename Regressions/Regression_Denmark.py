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
from sklearn.utils.extmath import density


import matplotlib.pyplot as plt
from fuzzywuzzy import process

# ------------------------------

denmark_cases = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\denmark_vac.csv", delimiter=',')
denmark_density = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\population_density_denmark_cleaned.xlsx")
denmark_income = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\denmark_income.csv", delimiter=';')
denmark_vac = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\denmark_vac1.csv", delimiter=',')


# -----------------------------

def linear_regression(x, y):
    x_ready = x.reshape((-1,1))

    X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.2, random_state=0) 

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    coef = regressor.coef_

    y_pred = regressor.predict(X_test)
    error = metrics.mean_absolute_error(y_test, y_pred)

    X_train = flatten_list(X_train)

    slope, intercept, r_value, p_value, std_err = stats.linregress(X_train, y_train)


    return coef[0], regressor.intercept_, error, p_value
     
def making_lists (a, b, c):
    coef = [] 
    intersect = []
    Mean_Absolute_Error = [] 
    p_value = [] 
    for d in a['date']:
       e = a[a['date'] == d ]
       f = e[b].values
       g = e[c].values 
       x, y, z, v = linear_regression(f, g)
       coef.append(x)
       intersect.append(y)
       Mean_Absolute_Error.append(z)
       p_value.append(v)
    return coef, intersect, Mean_Absolute_Error, p_value
       
def flatten_list (x):
    flat_list = []
    for sublist in x:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def dropdates(table):
    occurences = table['date'].value_counts()
    occurences = occurences.to_frame().reset_index()
    occurences = occurences[occurences['date'] < 5]
    for date in occurences['index']:
        table = table[table['date'] != date]
    return table


# -----------------------------
# density - infection rate

denmark_density = denmark_density.rename(columns={'Region' : 'region'})
denmark_density = pd.merge(denmark_density, denmark_cases, on='region')
denmark_density['date'] = pd.to_datetime(denmark_density['date'])
denmark_density = denmark_density.sort_values(by=['region', 'date'])

denmark_density['rolling_avg'] = denmark_density.groupby('region')['confirmed_cases_per_100k'].transform(lambda x: x.rolling(14, 1).mean())

denmark_density = dropdates(denmark_density)
a, b, c, d = making_lists(denmark_density, 'Population density', 'rolling_avg')
denmark_density['coef'] = a
denmark_density['intersect'] = b 
denmark_density['error_rate'] = c 
denmark_density['p_value'] = d

graph = denmark_density[denmark_density['date'] == '2021-06-06']

x = graph['Population density']
y = graph['rolling_avg']
plt.plot(x, y, 'o')
plt.plot(x, ((graph['coef'] * x) + graph['intersect']))
plt.xlabel("Population density")
plt.ylabel("Infection rate")
i = graph['error_rate'].iloc[0]
j = graph['p_value'].iloc[0]
plt.gcf().text(0.13, 0.95, "Mean absolute error: %1.3f" %i, fontsize=10)
plt.gcf().text(0.13, 0.90, "P-value: %1.3f" %j, fontsize=10)
plt.show()

# ------------------------------------
# income - vaccination coverage

denmark_vac = denmark_vac.rename(columns={'municipality' : 'region'})
denmark_income = denmark_income.iloc[4:-225].reset_index()
denmark_income = denmark_income.rename(columns={'level_3' : 'region', 'People by unit, time, sex, region and type of income' : 'income'})
denmark_income = denmark_income.astype({'income': 'float64'})
denmark_income = denmark_income.sort_values(by=['region'])

keys = {}
for region in denmark_vac['region']: 
  keys[region] = ((process.extract(region, denmark_income['region'], limit=1)))

labels = [] 
for key in keys:
    label = keys[key][0][0]
    labels = labels + [label]

denmark_vac['region'] = labels

denmark_income = pd.merge(denmark_income, denmark_vac, on='region')

#denmark_income = denmark_income[denmark_income['region'] != 'Province Byen København']
#denmark_income = denmark_income[denmark_income['region'] != 'Aarhus']

x = denmark_income['income'].values
y = denmark_income['vacc_pct_municipality'].values 

a, b, c, d = linear_regression(x, y)

denmark_income['coef'] = a 
denmark_income['intersect'] = b 
denmark_income['error_rate'] = c
denmark_income['p_value'] = d

print(denmark_income)

x = denmark_income['income']
y = denmark_income['vacc_pct_municipality']
plt.plot(x, y, 'o')
plt.plot(x, ((denmark_income['coef'] * x) + denmark_income['intersect']))
plt.xlabel("average income")
plt.ylabel("vaccination coverage")
i = denmark_income['error_rate'].iloc[0]
j = denmark_income['p_value'].iloc[0]
plt.gcf().text(0.13, 0.95, "Mean absolute error: %1.3f" %i, fontsize=10)
plt.gcf().text(0.13, 0.90, "P-value: %1.3f" %j, fontsize=10)
plt.show()












