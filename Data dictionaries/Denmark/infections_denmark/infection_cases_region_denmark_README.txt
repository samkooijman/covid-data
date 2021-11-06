This document describes the contents of the confirmed_cases_denmark_per_region file. The variable names described below refer to column names. Data is static and in time-series in .xlsx format. Data will be imported using the pandas library and then pass the source to the pd.read_xlsx(). There are no privacy restrictions, all data is public.

Data sources:
• The governmental Denmark Covid-19 dashboard
• The Danish Statens Serum Institut
• https://covid19.ssi.dk/overvagningsdata/download-fil-med-overvaagningdata


General description:
The dataset contains static data regarding the absolute numbers of postive Covid-19 infections, deaths and hospitalisations per region in Denmark per day. Additionaly, the hospitalisations, deaths and positive cases of the whole of denmark are also cumulatively included.
The data starts from the 01-03-2020 to 05-10-2021. 
There are 5512 instances and each instance makes a distinction between male or female. This might be interesting in analysing how the pandemic influences gender.
There seems to be no bias in the dataset as it is governmental data. 
Some of the Dato variable data seem to be of another data type. So we'll need to look into that.
The dataset and the number of infections and deaths will act as a dependent variable in the statisical analysis in combination with the independent variables discussed in the business understanding.


Variables:

Region | Region of residence (region of residence at the time of sampling) | DATA TYPE | STRING		
Dato | Date of sampling and actual day of admission | DATA TYPE | DATETYPE64
Køn | Men and women  | DATA TYPE | STRING
Bekræftede tilfælde | Number of confirmed cases | DATA TYPE | INT
Døde |Number of deaths | DATA TYPE | INT
Indlæggelser | Number of admissions | DATA TYPE | INT
Kumuleret antal døde | All deaths from the start of the pandemic to the current day | DATA TYPE | INT
Kumuleret antal bekræftede tilfæld| All confirmed cases from the start of the pandemic to the current day | DATA TYPE | INT
Kumuleret antal indlæggelser | All hospitalisations from the start of the pandemic to the current day | DATA TYPE | INT
