This document describes the contents of the United_States_COVID-19_Cases_and_Deaths_by_State_over_Time file. The variable names described below refer to column names. Data is static and in time-series in csv format. Data will be imported using the pandas library and then pass the source to the pd.read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• The Centers for Disease Control and Prevention (CDC) database of the USA
• https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36

--------------------------------------------------
General description:
This dataset reports the confirmed postive Covid-19 cases, probable cases and deaths over time per state.
Probable cases and deaths with regards to Covid-19 are also considered in the dataset. This may be used for some extra analysis how independent variables may influence probably cases and due to what reason that thought is made.
No age groups have been exluded in the dataset.
There seems to be not biased as this is a governmental data. The structure of the data is not consistent. It is quite the mess and needs to be filtered accordingly.
There are 37.3k instances.
There are also for some states no probable cases or deaths. We may analyse why so and how this may be influenced to external factors
The dataset may contain negative values since it sometimes is adjusted by time-wise changes. Cases or deaths may be designated to other dates and therefore sometimes negative values may occur.
The dataset provides dependent variables (deaths and infections) which will get analysed with respect to the independent variables given in the business understanding section.

Variables

submission_date | Date of counts | DATA TYPE | DATETIME64
state | Jurisdiction | DATA TYPE| STRING
tot_cases | Total number of cases | DATA TYPE| INT
conf_cases | Total confirmed cases| DATA TYPE| INT
prob_cases | Total probable cases | DATA TYPE| INT
new_case | 	Number of new cases | DATA TYPE| INT
pnew_case | 	Number of new probable cases | DATA TYPE| INT
tot_death | 	Total number of deaths | DATA TYPE| INT
conf_death | 	Total number of confirmed deaths | DATA TYPE| INT
prob_death | Total number of probable deaths | DATA TYPE| INT
new_death | Number of new deaths | DATA TYPE| INT
pnew_death | 	Number of new probable deaths | DATA TYPE| INT
created_at | 	Date and time record was created | DATA TYPE| DATETIME64
consent_cases | If Agree, then confirmed and probable cases are included. If Not Agree, then only total cases are included. | DATA TYPE| STRING
consent_deaths | If Agree, then confirmed and probable deaths are included. If Not Agree, then only total deaths are included. | DATA TYPE| STRING
