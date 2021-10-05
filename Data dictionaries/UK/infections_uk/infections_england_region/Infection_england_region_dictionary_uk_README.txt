This document describes the contents of the infections_region_england file. The variable names described below refer to column names. Data is static and in time-series in csv format. Data will be imported using the pandas library and then pass the source to the pd.read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• The governmental UK Covid-19 dashboard
• https://coronavirus.data.gov.uk/details/download

--------------------------------------------------
General description:
The dataset contains the amount of Covid-19 positive tests on a specific date in a respective region in England.
There are 4824 instances.
There seems to no bias as this is a governmental dataset and all data seems consistent with each other.
The dataset is rather limited to only positive tests on a given date and a region. The region is fairly big so that can be a struggle in the data preparation phase. However, the number of postive tests will act as a dependent variable with regards to the other variables discussed in the business understanding.

Variables

areaCode | The areacode of the region in England. DATA TYPE | STRING |
areaName | The name of the respective region in England. DATA TYPE | STRING |
areaType | The type of locatin, region, area in England. DATA TYPE | STRING |
date | The publish date of the Covid-19 positive test. DATA TYPE | DATETIME64 |
newCasesByPublishData | The amount of Covid-19 positive test. DATA TYPE | INT |
