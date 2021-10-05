This document describes the contents of the  income_usa file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
•  Bureau of Labor Statistics, Local Area Unemployment Statistics (LAUS) data. Average annual unemployment data are unavailable for Puerto Rico in 2020 because of missing monthly observations for March and April 2020.
(hhttps://data.ers.usda.gov/reports.aspx?ID=17828)

--------------------------------------------------
General description:
Socioeconomic indicators like poverty rates, population change, unemployment rates, and education levels vary geographically across U.S. States and counties. ERS compiles the latest data on these measures and provides data download for States and counties.
Data is partly filled - Puerto Rico has empty values. No major concerns about compatibility with data types. 

--------------------------------------------------

Description of variables:
Name - name of state in USA | DATA TYPE | STRING |
Unemployment Rate (percent) by yer (percent) - | DATA TYPE | FLOAT |	
Median Household Income (2019)- Median Household Income (2019) in $ | DATA TYPE | FLOAT |