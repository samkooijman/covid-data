poliThis document describes the contents of the political_pref_denmark file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• Statistics Denmark 
(https://www.statbank.dk/statbank5a/selectvarval/saveselections.asp)

--------------------------------------------------
General description:
In Danish elections votes are counted manually. The municipalities use an IT-system developed by KMD afterwards. It is only a few very obvious mistakes that Statistics Denmark has any possibility of discovering. E.g. when a result in one area differs significantly from other results within the same constituency. Controls are in place in order to find situations like these.
Data is fully filled. No major concerns about compatibility with data types. 

--------------------------------------------------

Description of variables:
Political party	- name of political party | DATA TYPE | STRING |
Region - region in Denmark | DATA TYPE | STRING |
Number of people	- number of people that are voting for particular political party | DATA TYPE | INT|