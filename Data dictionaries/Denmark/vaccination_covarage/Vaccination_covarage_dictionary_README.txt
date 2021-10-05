This document describes the contents of the vaccination_covarage_denmark file. The variable names described below refer to column names. Data is staic in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• CPR register
• The Danish Vaccination Register
• Booking data
(https://covid19.ssi.dk/overvagningsdata/download-fil-med-vaccinationsdata)
--------------------------------------------------
General description:
The inventory includes people who were invited to be vaccinated against COVID-19 at least 7 days ago. This means that people invited within the last 7 days are not included.
The inventory is based on the various steps in the vaccination process.
The statement is made so that people can only appear at one of these stages, and they are placed at the highest possible stage achieved in the vaccination process, where started vaccination is a higher stage.
then invited to and booked time for vaccination. Therefore, the shares on the four steps add up to 100 per cent.
People who are vaccinated with the Johnson & Johnson vaccine will be included under the fully vaccinated.
There is not sufficient data - missing municipality values that will need to be filtered.  Data format is not the same in Number_invited_not_booked column - if there are less than 10 people, data type is presented as a string with value <10.

--------------------------------------------------

Description of variables:

municipality: Municipality of residence at the time of the inventory. DATA TYPE | STRING |
parish: Parish of residence at the time of the inventory. Some parishes are geographically distributed over several municipalities and will therefore appear several times. Persons who do not have an address cannot be placed in a parish. They will appear under the municipality, but without a parish (see also under discretion). DATA TYPE | STRING | 
ppl_inventory: The total number of people on which the inventory is based.  DATA TYPE | INT | 
Number_invited_not_booked: Number of people who have been invited but have not yet booked an appointment, have started or have completed vaccination.  DATA TYPE | INT | 
Proportion_invited_not_booked: Proportion of persons who have been invited but have not yet booked an appointment, have started or have completed vaccination. DATA TYPE | INT | 
Proportion_booked: Proportion of persons who have booked time, but who have not started or have completed vaccination. DATA TYPE | FLOAT | 
Proportion_started: Proportion of persons who have started vaccination but have not completed vaccination. DATA TYPE | FLOAT | 
Proportion_completed vaccinated: Proportion of persons who have completed vaccination. DATA TYPE | FLOAT | 
-------------------------------------------------- 
