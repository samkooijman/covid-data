This document describes the contents of the infections_nation_uk file. The variable names described below refer to column names. Data is static and in time-series in csv format. Data will be imported using the pandas library and then pass the source to the pd.read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• The governmental UK Covid-19 dashboard
• https://coronavirus.data.gov.uk/details/download

--------------------------------------------------
General description:
The dataset contains the amount of Covid-19 positive tests on a specific date in a respective country in the UK.
There are 2358 instances.
There seems to be not biased as this is a governmental data and all data seems consistent.
The dataset is rather limited to only positive tests on a given date and a country in the UK. The countries are fairly big so that can be a struggle in the data preparation phase. Espcially England is pretty big, but another dataset is available to dinstinguish the regions of England. The number of postive tests will act as a dependent variable with regards to the other variables discussed in the business understanding.

Variables

areaCode | The areacode of the country in the UK.DATA TYPE | STRING |
areaName | The name of the respective region in UK. DATA TYPE | STRING |
areaType | The type of locatin, region, area in UK. DATA TYPE | STRING |
date | The publish date of the Covid-19 positive test. DATA TYPE | DATETIME64 |
newCasesByPublishData | The amount of Covid-19 positive test. DATA TYPE | INT |