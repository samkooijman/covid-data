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


# -------------------------------------
# loading data 

density_usa = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\usa_density.csv", encoding= 'unicode_escape', delimiter=",")
infection_usa = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\usa_cases.csv",  encoding= 'unicode_escape', delimiter=",")
pop_usa= pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\pop_usa.csv",  encoding= 'unicode_escape', delimiter=",")
vacc_usa = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\vacc_usa.csv",  encoding= 'unicode_escape', delimiter=",")


income_usa = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\usa_income.xlsx")
income_usa = income_usa.iloc[2:-3]
new_header = income_usa.iloc[0]
income_usa = income_usa[1:]
income_usa.columns = new_header
income_usa['Median Household Income (2019)'] = income_usa['Median Household Income (2019)'].str[1:]
income_usa['Median Household Income (2019)'] = income_usa['Median Household Income (2019)'].str.replace(',', '')




# -------------------------------------


#Replace the statenames by the statecodes
pop_usa = pop_usa.replace({
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
})


infection_usa = infection_usa.iloc[: , [0, 1, 5]]
infection_usa = infection_usa.rename(columns={"submission_date" : "date"})

pop_usa = pop_usa.iloc[5 : , [4, 5]]
pop_usa = pop_usa.rename(columns={"NAME" : "state", "CENSUS2010POP" : "population"})

#Merge the population dataset with the infection dataset
infection_usa = pd.merge(pop_usa,infection_usa,on='state')

#Change the date
infection_usa['date'] = pd.to_datetime(infection_usa['date'])
infection_usa['date'] = pd.to_datetime(infection_usa['date'], format='%Y%m%d').dt.strftime('%d/%m/%Y')

#Grouping the states and dates together
infection_usa = infection_usa.groupby(['date', 'state', 'new_case'], as_index=False).sum();

#Calculate the infections per 100k
infection_usa['new_case'] = infection_usa['new_case'] / infection_usa['population'] * 100000;

infection_usa = infection_usa.rename(columns={"new_case" : "new_cases_per_100k"})


# -----------------------------------------
# Rewriting states

density_usa = density_usa.replace({
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
})

income_usa = income_usa.replace({
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
})

# ---------------------------------------
# Linear regression function

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

def onlysunday(table):
    table = table[table['date'].dt.day_name() == 'Sunday']
    return table

# ---------------------------------------


# linking rolling avarage of infections and density

density = []
for x in density_usa['density']:
    y = x * 0.386102159 
    density = density + [y]
density_usa['DensityKM'] = density

density_usa = density_usa.rename(columns={"State" : "state"})
density_usa = pd.merge(density_usa,infection_usa,on='state')

density_usa['date'] = pd.to_datetime(density_usa['date'])
density_usa = density_usa.sort_values(by=['state','date'])

density_usa['rolling_avg'] = density_usa.groupby('state')['new_cases_per_100k'].transform(lambda x: x.rolling(14, 1).mean())

# ------------------------------------------
# vaccination dataset prep

vacc_usa = vacc_usa.rename(columns=str.lower)

vacc_usa = vacc_usa.rename(columns={"location" : "state"})

vacc_usa = vacc_usa.iloc[: , [0, 2, 42]]

vacc_usa['date'] = pd.to_datetime(vacc_usa['date'])
vacc_usa['date'] = pd.to_datetime(vacc_usa['date'], format='%Y%m%d').dt.strftime('%d/%m/%Y')

vacc_usa = vacc_usa.groupby(['date', 'state'], as_index=False).sum();

# ----------------------------------------------------
# Linking income and vaccination coverage 
income_usa = income_usa.rename(columns={'Name' : 'state', 'Median Household Income (2019)' : 'income'})
income_usa = pd.merge(income_usa, vacc_usa, on='state')
income_usa['date'] = pd.to_datetime(income_usa['date'])
income_usa = income_usa.sort_values(by=['state','date'])
income_usa = income_usa.astype({'income': 'float64'})



# --------------------------------------------------- 
# Linear regression over income and vaccination coverage 

income_usa = onlysunday(income_usa)
density_usa = onlysunday(density_usa)

a, b, c, d = making_lists(income_usa, 'income', 'series_complete_pop_pct' )
income_usa['coef'] = a
income_usa['intersect'] = b
income_usa['error_rate'] = c 
income_usa['p_value'] = d 

graph = income_usa[income_usa['date'] == '2021-11-07']

x = graph['income']
y = graph['series_complete_pop_pct']
plt.plot(x, y, 'o')
plt.plot(x, ((graph['coef'] * x) + graph['intersect']))
plt.xlabel("average income")
plt.ylabel("vaccination coverage")
i = graph['error_rate'].max()
j = graph['p_value'].max()
plt.gcf().text(0.13, 0.95, "Mean absolute error: %1.3f" %i, fontsize=10)
plt.gcf().text(0.13, 0.90, "P-value: %1.3f" %j, fontsize=10)
plt.show()

# ----------------------------------

a, b, c, d = making_lists(density_usa, 'DensityKM', 'rolling_avg')
density_usa['coef'] = a 
density_usa['intersect'] = b
density_usa['error_rate'] = c 
density_usa['p_value'] = d 

graph = density_usa[density_usa['date'] == '2021-11-07']
graph = graph[graph['state'] != 'DC']

x = graph['DensityKM']
y = graph['rolling_avg']
plt.plot(x, y, 'o')
plt.plot(x, ((graph['coef'] * x) + graph['intersect']))
plt.xlabel("Population Density")
plt.ylabel("Average number of new cases")
i = graph['error_rate'].max()
j = graph['p_value'].max()
plt.gcf().text(0.13, 0.95, "Mean absolute error: %1.3f" %i, fontsize=10)
plt.gcf().text(0.13, 0.90, "P-value: %1.3f" %j, fontsize=10)
plt.show()


