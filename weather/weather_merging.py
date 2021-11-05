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


infec_den['date'] = pd.to_datetime(infec_den['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
df_wea_den['date'] = pd.to_datetime(df_wea_den['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')

infec_uk['date'] = pd.to_datetime(infec_uk['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
df_wea_uk['date'] = pd.to_datetime(df_wea_uk['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')

infec_usa['date'] = pd.to_datetime(infec_usa['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
df_wea_usa['date'] = pd.to_datetime(df_wea_usa['date'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')



new_df = pd.merge(df_wea_den, infec_den, on='date')
new_df2 = pd.merge(df_wea_uk, infec_uk, on='date')
new_df3 = pd.merge(df_wea_usa, infec_usa, on='date')

#print(new_df)
#print(new_df2)
print(new_df3)