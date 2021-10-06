This document describes the contents of the political_preference_uk file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public.


Data sources:
• House of Commons Library analysis
(https://commonslibrary.parliament.uk/constituency-data-election-results/)

--------------------------------------------------
General description:
This file has data on results of the 2017 General Election for constituencies in the UK. 
Candidates’ gender is recorded based on information in the public domain in the run-up to the election. ‘Non-binary’ indicates candidates with a non-binary or gender neutral gender identity.
The change in each party’s vote share relative to 2017 is shown in percentage points (e.g. a party that received 40% of the vote in 2017 and 30% of the vote in 2019 will have a change of -10 percentage points). If this is the first time a party stood at the election, the change is the same as their total share of the votes. Change is not shown for independent candidates as they do not belong to a party.
Turnout is the number of valid votes cast as a proportion of the electorate (i.e. people who are eligible to vote) in a constituency.
Data is partly filled with empty values consisting null (0). No major concerns about compatibility with data types. 

--------------------------------------------------

Description of variables:		
	
ons_id	ONS code for the constituency	| DATA TYPE | STRING |		
ons_region_id	ONS code for the region	| DATA TYPE | STRING |		
constituency_name	Name of constituency	| DATA TYPE | STRING |		
county_name	Name of county the constituency is in | DATA TYPE | STRING |			
region_name	Name of region/nation the constituency is in | DATA TYPE | STRING |			
country_name	Name of nation the constituency is in | DATA TYPE | STRING |		
constituency_type	Whether the constituency is a borough or a county constituency | DATA TYPE | STRING |		
declaration_time	Time that the result was declared	| DATA TYPE | DATE |		
mp_firstname	First name of the winning candidate | DATA TYPE | STRING |			
mp_surname	Surname of the winning candidate	| DATA TYPE | STRING |		
mp_gender	Gender of the winning candidate	| DATA TYPE | STRING |		
result	Winning party, and if applicable the party the seat was gained from			
first_party	Short code for the party that came first	| DATA TYPE | STRING |		
second_party	Short code for the party that came second	| DATA TYPE | STRING |		
electorate	Number of people eligible to vote	| DATA TYPE | INT |		
valid_votes	Valid votes cast	| DATA TYPE | INT |	
invalid_votes	Invalid votes cast | DATA TYPE | INT |			
majority		Majority in votes | DATA TYPE | INT |			
mp_fullname	Full name of the winning candidate | DATA TYPE | STRING |				
majority_percent	Majority expressed as a percentage | DATA TYPE | FLOAT |			
majority_rank	Rank on size of majority expressed as a percentage (1 is the largest and 650 the smallest) | DATA TYPE | FLOAT |				
turnout_const	Turnout in the consitutency | DATA TYPE | FLOAT |				
turnout_reg	Turnout in the region	 | DATA TYPE | FLOAT |			
turnout_uk	Turnout in the UK	 | DATA TYPE | FLOAT |			
turnout_2017	Turnout in the constituency in 2017  | DATA TYPE | FLOAT |				

