import pandas as pd
import numpy as np 

# UK cleaning

# Extracting and selecting data concerning density
uk_density = pd.ExcelFile('C:\\Users\\FKvan\\Desktop\\MBI\\uk_density.xls')
uk_density = pd.read_excel(uk_density, 'MYE 5')
uk_density = uk_density[6:]

# Creating new column headers
new_header = uk_density.iloc[0]
uk_density = uk_density[1:]
uk_density.columns = new_header

# Selecting relevant data and correctly naming them
uk_density = uk_density.loc[(uk_density['Geography'] == 'Region')| (uk_density['Geography'] == 'Country')] 
uk_density = uk_density[['Name', '2020 people per sq. km']]
uk_density = uk_density.rename(columns={'Name' : 'region', '2020 people per sq. km' : 'density'})

# renaming items in region column
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
    "YORKSHIRE AND THE HUMBER" : "Yorkshire and The Humber",
    "UNITED KINGDOM" : "United Kingdom",
    "GREAT BRITAIN" : "Great Britain",
    "ENGLAND AND WALES" : "England and Wales",
    "ENGLAND" : "England"
})

# to CSV
uk_density.to_csv('uk_density_cleaned.csv')

# Extracting and selecting data concerning income 
uk_income = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\uk_income1.csv")
uk_income = uk_income.reset_index()
uk_income = uk_income[['level_0','level_2']]
uk_income = uk_income.iloc[:-5]

# Creating new column headers and renaming them
new_header = uk_income.iloc[0]
uk_income = uk_income[1:]
uk_income.columns = new_header
uk_income = uk_income.rename(columns={"Countries and\nregions of the \nUK" : "region", "GDHI per \nhead (£)¹" : "income"})

# Creating floats
uk_income['income'] = uk_income['income'].str.replace(',', '')
uk_income['income'] = uk_income['income'].astype({'income': 'float64'})

# To dollar
dollars = []
for pound in uk_income['income']:
    dollar = pound * 1.3635794
    dollars = dollars + [dollar]
uk_income['income'] = dollars
     
# renaming items in region
uk_income = uk_income.replace({
    "UK" : "United Kingdom"
})

# To CSV
uk_income.to_csv('uk_income_cleaned.csv')

# USA cleaning

# Extracting and selecting data concerting income
usa_income = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\usa_income.xlsx")
usa_income = usa_income.iloc[2:-3].reset_index()

# creating new headers and renaming them
new_header = usa_income.iloc[0]
usa_income = usa_income[1:]
usa_income.columns = new_header
usa_income = usa_income.rename(columns={'Name' : 'region', 'Median Household Income (2019)' : 'income'})

# Selecting relevant columns
usa_income = usa_income[['region', 'income']]

# Creating floats 
usa_income['income'] = usa_income['income'].str[1:]
usa_income['income'] = usa_income['income'].str.replace(',', '')
usa_income['income'] = usa_income['income'].str.replace('$', '')
usa_income['income'] = usa_income['income'].astype({'income': 'float64'})

# Renaming items in region
usa_income = usa_income.replace({
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

# To CSV
usa_income.to_csv('usa_income_cleaned.csv')

# Extracting and selecting data concerning density
usa_density = pd.read_csv("C:\\Users\\FKvan\\Desktop\\MBI\\usa_density.csv", encoding= 'unicode_escape', delimiter=",")
usa_density = usa_density[['State', 'density']]

# Renaming columns
usa_density = usa_density.rename(columns={'State' : 'region'})

# density in sq KM
densityKM = []
for mile in usa_density['density']:
    km = mile * 0.386102159 
    densityKM = densityKM + [km]
usa_density['density'] = densityKM

# renaming items in region
usa_density = usa_density.replace({
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

# To CSV
usa_density.to_csv('usa_density_cleaned.csv')

# Denmark cleaning

# Extracting and selecting data concerning income
denmark_income = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\Denmark_income.xlsx")
denmark_income = denmark_income[['Unnamed: 7', 'Unnamed: 8']]
denmark_income = denmark_income[2:]

# renaming columns 
denmark_income = denmark_income.rename(columns={'Unnamed: 7': 'region', 'Unnamed: 8' : 'income' })

# to dollar 
dollars = []
for krone in denmark_income['income']:
    dollar = krone * 0.15582071
    dollars = dollars + [dollar]
denmark_income['income'] = dollars

# To CSV
denmark_income.to_csv('denmark_income_cleaned.csv')

# Extracting and selecting data concerning density
denmark_density = pd.read_excel("C:\\Users\\FKvan\\Desktop\\MBI\\denmark_density.xlsx")
denmark_density = denmark_density[['Region', 'Population density']]

# Renaming columns
denmark_density = denmark_density.rename(columns={'Region': 'region', 'Population density' : 'density'})

# To CSV
denmark_density.to_csv('denmark_density_cleaned.csv')


