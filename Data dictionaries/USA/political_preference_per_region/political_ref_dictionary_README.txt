poliThis document describes the contents of the political_preference_usa file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• Thomson Reuters
(https://www.kaggle.com/unanimad/us-election-2020?select=governors_county_candidate.csv)

--------------------------------------------------
General description:
This dataset contains county-level data from 2020 US Election.
Data is fully filled. No major concerns about compatibility with data types. 


--------------------------------------------------

Description of variables:
state - name of USA state | DATA TYPE | STRING |
county -   geographical region of a country used for administrative or other purposes in certain modern nations | DATA TYPE | STRING |
candidate - name and surname of the candidate | DATA TYPE | STRING |
party -  3 letter abbreviation  of a party | DATA TYPE | STRING |
votes - number of votes for a party | DATA TYPE | INT |
won - if party won election| DATA TYPE | BOOLEAN |
