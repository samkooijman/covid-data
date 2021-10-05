This document describes the contents of the vaccination_covarage_usa file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• Centers for Disease Control and Prevention 
(https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc)

--------------------------------------------------
General description:
Overall US COVID-19 Vaccine deliveries and administration data at national and jurisdiction level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities. 

There is not sufficient data -  missing data is filled with null values or string "no value"(therefore in some columns numeric data is depicted as a string -  this can cause conflicts in compatibility with data type). 

--------------------------------------------------

Description of variables:

Date: Date. DATA TYPE | DATE |
MMWR_week: The Morbidity and Mortality Weekly Report. DATA TYPE | INT | 
Location: State/Territory/Federal Entity.  DATA TYPE | STRING | 
Distributed: Total number of distributed doses.  DATA TYPE | INT | 
Distributed_Janssen: Total number of J&J/Janssen doses delivered DATA TYPE | INT | 
Distributed_Moderna: Total number of Moderna doses delivered  DATA TYPE | INT | 
Distributed_Pfizer: Total number of Pfizer-BioNTech doses delivered DATA TYPE | INT | 
Distributed_Unk_Manuf: Total number of doses from unknown manufacturer delivered  DATA TYPE | INT | 
Dist_Per_100K Delivered doses per 100,000 census population  DATA TYPE | INT | 
Distributed_Per_100k_12Plus: Total number of delivered doses per 100,000 12+ population  DATA TYPE | INT | 
Distributed_Per_100k_18Plus: Total number of delivered doses per 100,000 18+ population  DATA TYPE | INT | 
Distributed_Per_100k_65Plus: Total number of delivered doses per 100,000 65+ population  DATA TYPE | INT | 
Administered: Total number of administered vaccines based on state where administered  DATA TYPE | INT | 
Administered_12Plus: Total number of doses administered to people 12+ based on the jurisdiction where recipient lives  DATA TYPE | INT | 
Administered_18Plus: Total number of doses administered to people 18+ based on the jurisdiction where recipient lives  DATA TYPE | INT | 
Administered_65Plus: Total number of doses administered to people 65+ based on the jurisdiction where recipient lives  DATA TYPE | INT | 
Administered_Janssen: Total number of J&J/Janssen doses administered  DATA TYPE | INT | 
Administered_Dose1_Pop_Pct:  Percent of population with at lease one dose based on the jurisdiction where recipient lives DATA TYPE | FLOAT | 
Administered_Dose1_Recip_12Plus: Total number of people 12+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_12PlusPop_Pct: Percent of 12+ population with at least one dose based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Administered_Dose1_Recip_18Plus: Total number of people 18+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_18PlusPop: Pct Percent of 18+ population with at least one dose based on the jurisdiction where recipient lives DATA TYPE | FLOAT | 
Administered_Dose1_Recip_65Plus: Total number of people 65+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_65PlusPop_Pct: Percent of 65+ population with at lease one dose based on the jurisdiction where recipient lives DATA TYPE | FLOAT | 
Series_Complete_Yes: Total number of people who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives DATA TYPE | INT | 
Series_Complete_Pop_Pct: Percent of people who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_12Plus: Total number of people 12+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives: DATA TYPE | INT | 
Series_Complete_12PlusPop_Pct: Percent of people 12+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives DATA TYPE | FLOAT | 
Series_Complete_18Plus:  Total number of people 18+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | INT | 
Series_Complete_18PlusPop_Pct: Percent of people 18+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Administered_Dose1_Pop_Pct: Percent of population with at lease one dose based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Administered_Dose1_Recip_12Plus: Total number of people 12+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_12PlusPop_Pct: Percent of 12+ population with at least one dose based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Administered_Dose1_Recip_18Plus: Total number of people 18+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_18PlusPop_Pct: Percent of 18+ population with at least one dose based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Administered_Dose1_Recip_65Plus: Total number of people 65+ with at least one dose based on the jurisdiction where recipient lives DATA TYPE | INT | 
Administered_Dose1_Recip_65PlusPop_Pct: Percent of 65+ population with at lease one dose based on the jurisdiction where recipient lives DATA TYPE | FLOAT | 
Series_Complete_Yes: Total number of people who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives DATA TYPE | INT | 
Series_Complete_Pop_Pct Percent: of people who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_12Plus: Total number of people 12+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives DATA TYPE | INT | 
Series_Complete_12PlusPop_Pct: Percent of people 12+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_18Plus: Total number of people 18+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives DATA TYPE | INT | 
Series_Complete_18PlusPop_Pct: Percent of people 18+ who are fully vaccinated (have second dose of a two-dose vaccine or one dose of a single-dose vaccine) based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_Pfizer_18Plus: Total number of people 18+ who are fully vaccinated with the Pfizer vaccine based on the jurisdiction where recipient lives Number  DATA TYPE | FLOAT | 
Series_Complete_Unk_Manuf_18Plus: Total number of people 18+ who are fully vaccinated with two doses from an uknown two-dose vaccine manufacturer based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_Janssen_65Plus: Total number of people 65+ who are fully vaccinated with the J&J/Janssen vaccine based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_Moderna_65Plus: Total number of people 65+ who are fully vaccinated with the Moderna vaccine based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_Pfizer_65Plus: Total number of people 65+ who are fully vaccinated with the Pfizer vaccine based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_Unk_Manuf_65Plus: Total number of people 65+ who are fully vaccinated with two doses from an uknown two-dose vaccine manufacturer based on the jurisdiction where recipient lives  DATA TYPE | FLOAT | 
Series_Complete_FedLTC: Total number of doses administed to long-term care facilities  DATA TYPE | FLOAT | 
Series_Complete_FedLTC_Residents: Total number of doses administed to long-term care facility residents  DATA TYPE | FLOAT | 
Series_Complete_FedLTC_Staff: Total number of doses administed to long-term care facility staff  DATA TYPE | FLOAT | 
Series_Complete_FedLTC_Unknown: Total number of doses administed to other people in long-term care facility  DATA TYPE | FLOAT | 
Additional_Doses: Total number of people who are fully vaccinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_Vax_Pct: Percent of people who are fully vaccinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_18Plus: Total number of people 18+ that are fully vaccinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_18Plus_Vax_Pct: Percent of people 18+ who are fully vaccinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_50Plus: Total number of people 50+ that are fully vaccinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_50Plus_Vax_Pct: Percent of people 50+ who are fully vaccinated and have received a booster (or additiuonal) dose. DATA TYPE | STRING | 
Additional_Doses_65Plus: Total number of people 65+ that are fully vacinated and have received a booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_65Plus_Vax_Pct: Percent of people 65+ who are fully vaccinated and have received a booster (or additional) dose.  DATA TYPE | STRING | 
Additional_Doses_Moderna: Total number of fully vaccinated people who have received a Moderna booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_Pfizer: Total number of fully vaccinated people who have received a Pfizer booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_Janssen: Total number of fully vaccinated people who have received a Janssen booster (or additional) dose. DATA TYPE | STRING | 
Additional_Doses_Unk_Manuf: Total number of fully vaccinated people who have received an other or unknown booster (or additional) dose.  DATA TYPE | STRING | 


-------------------------------------------------- 
