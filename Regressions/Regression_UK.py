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


# --------------------------------------------------

uk_infection = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\uk_infection.csv")
uk_vaccination = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\uk_vaccination.csv")
uk_density = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\population_density_uk_cleaned.xlsx")
uk_income = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\uk_income.xlsx")
vacc_usa = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\vacc_usa.csv",  encoding= 'unicode_escape', delimiter=",")

# --------------------------------------------------

uk_density = uk_density.loc[(uk_density['Geography'] == 'Region')| (uk_density['Geography'] == 'Country')] 

uk_density = uk_density.replace({
    "SOUTH WEST": "South West",
    "NORTH EAST": "North East",
    "WALES": "Wales",
    "LONDON": "London",
    "SCOTLAND": "Scotland",
    "WEST MIDLANDS": "West Midlands",
    "NORTH WEST": "North West",
    "EAST MIDLANDS": "East Midlands",
    "SCOTLAND": "Scotland",
    "WEST MIDLANDS": "West Midlands",
    "SOUTH EAST": "South East",
    "NORTHERN IRELAND": "Northern Ireland",
    "EAST": "East of England",
    "NORTHERN IRELAND": "Northern Ireland",
})

uk_density = uk_density.rename(columns={"Name" : "areaname"})
uk_density = pd.merge(uk_infection, uk_density , on='areaname')

uk_density['date'] = pd.to_datetime(uk_density['date'])
uk_density = uk_density.sort_values(by=['areaname', 'date'])

rolling_avg = uk_density.groupby('areaname')['cases_per_100k'].rolling(14, min_periods=1).mean().reset_index()
uk_density['rolling_avg'] = rolling_avg['cases_per_100k']

uk_density_temp = uk_density[uk_density['date'] == '2020-05-08']

x = uk_density_temp['2020 people per sq. km'].values
y = uk_density_temp['rolling_avg'].values

x_ready = x.reshape((-1,1))

X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.2, random_state=0) 

regressor = LinearRegression()
regressor.fit(X_train, y_train)

#print(regressor.intercept_)
#print(regressor.coef_)

y_pred = regressor.predict(X_test)
accuracy = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

#print(accuracy)

#print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
#print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
#print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#print(p_value)

# --------------------------------------

uk_vaccination = uk_vaccination.rename(columns={
    "full_vacc_south_west": "South West",
    "full_vacc_north_east": "North East",
    "full_vacc_wales": "Wales",
    "full_vacc_london": "London",
    "full_vacc_west_midlands": "West Midlands",
    "full_vacc_north_west": "North West",
    "full_vacc_east_midlands": "East Midlands",
    "full_vacc_scotland": "Scotland",
    "full_vacc_south_east": "South East",
    "full_vacc_north_ireland": "Northern Ireland",
    "full_vacc_east_of_england": "East of England",
    "full_vacc_yorkshire_and_the_humber": "Yorkshire and The Humber"
})

uk_income = uk_income.rename(columns={"GDHI per\nhead (£)¹" : "gdhi_per_head", "Countries and\nregions of the\nUK" : "region"})
uk_income = uk_income[uk_income['region'] != 'UK']
uk_income = uk_income[uk_income['region'] != 'England']
uk_income = uk_income.sort_values(by='region')

uk_vaccination_temp = uk_vaccination[uk_vaccination['weekly_period_end'] == '25-04-2021'].T.iloc[2:]
uk_vaccination_temp = uk_vaccination_temp.reset_index()
uk_vaccination_temp = uk_vaccination_temp.sort_values(by='index')
uk_vaccination_temp.rename(columns={uk_vaccination_temp.columns[1]: "vaccin_percentage" }, inplace = True)

x = uk_income['gdhi_per_head'].values
y = uk_vaccination_temp['vaccin_percentage'].values

x_ready = x.reshape((-1,1))

X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.1, random_state=0) 

egressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(X_test)
accuracy = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print(accuracy)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# --------------------------------------------------

vacc_usa = vacc_usa.rename(columns=str.lower)

vacc_usa = vacc_usa.rename(columns={"location" : "state"})

vacc_usa = vacc_usa.iloc[: , [0, 2, 42]]

vacc_usa['date'] =  pd.to_datetime(vacc_usa['date'])
vacc_usa['date'] = pd.to_datetime(vacc_usa['date'], format='%Y%m%d').dt.strftime('%d/%m/%Y')

vacc_usa = vacc_usa.groupby(['date', 'state'], as_index=False).sum();

# ----------------------------------------------------

print(vacc_usa)



