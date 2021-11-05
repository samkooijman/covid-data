import pandas as pd

df_wea_den = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/weather/denmark/combined.csv')
infec_den = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/infec_denmark.csv')

df_wea_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/weather/unitedkingdom/merged_folder/combined.csv')
infec_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_uk_infec.csv')

df_wea_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/weather/usa/combined.csv')
infec_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/usa_cases.csv')



df_wea_den = df_wea_den.rename(columns={'date_time' : 'date'})
df_wea_uk = df_wea_uk.rename(columns={'date_time' : 'date'})
df_wea_usa = df_wea_usa.rename(columns={'date_time' : 'date'})
df_wea_usa = df_wea_usa.rename(columns={'location' : 'state'})
df_wea_den = df_wea_den.rename(columns={'location' : 'region'})


infec_den['date'] = pd.to_datetime(infec_den['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
df_wea_den['date'] = pd.to_datetime(df_wea_den['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')

infec_uk['date'] = pd.to_datetime(infec_uk['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
df_wea_uk['date'] = pd.to_datetime(df_wea_uk['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')

infec_usa['date'] = pd.to_datetime(infec_usa['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
df_wea_usa['date'] = pd.to_datetime(df_wea_usa['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')


df_wea_usa = df_wea_usa.replace({
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


new_df = pd.merge(df_wea_den, infec_den, on=['date', 'region'])
new_df2 = pd.merge(df_wea_uk, infec_uk, on='date')
new_df3 = pd.merge(df_wea_usa, infec_usa, on=['date', 'state'])

new_df.drop('Unnamed: 0', inplace=True, axis=1)
new_df3.drop('Unnamed: 0', inplace=True, axis=1)

print(new_df.keys())

new_df = new_df.drop_duplicates()
new_df3 = new_df3.drop_duplicates()

new_df = new_df.sort_values(by='date', ascending=True)
new_df3 = new_df3.sort_values(by='date', ascending=True)


#print(new_df.iloc[1:10, 1: 8])
#print(new_df)
#print(new_df2)
print(new_df3)
