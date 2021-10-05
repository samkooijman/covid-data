This document describes the contents of the population_denmark file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• Statistics Denmark 
(https://www.statbank.dk/statbank5a/selectvarval/saveselections.asp)

--------------------------------------------------
General description:
The income statistics are based on a full-population register. It contains information on annual incomes at both the personal- and family level as well as data on the distribution of income. The income is available both pre- and post taxes and can be split into subcategories such as primary income, transfers, property income and taxes. In the income statistics the population is divided into groups by age, socio-economic status, gender, municipalities (NUTS-3), type of family and into income intervals.
Data is fully filled. No major concerns about compatibility with data types. 

--------------------------------------------------

Description of variables:
Region - region in Denmark | DATA TYPE | STRING |
Pre-tax Income, total - also known as earnings before tax, is the net income earned by a business before taxes are subtracted/accounted for | DATA TYPE | FLOAT |	
Primary income - he primary income account is made up of compensation of employees, investment income and other primary income. | DATA TYPE | FLOAT |