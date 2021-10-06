This document describes the contents of the gross_disposable_houseincome_uk file. The variable names described below refer to column names. Data is static and in xlsx format. Data will be imported using the pandas library and then pass the source to the pd.read_xlsx(). There are no privacy restrictions, all data is public.


Data sources:
• The UK Office for National Statistics
• https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/bulletins/regionalgrossdisposablehouseholdincomegdhi/1997to2018

--------------------------------------------------
General description:

The dataset contains data about the disposable income of different regions in the UK in 2018. The gross disposable household income (GDHI) is the relative income a household receives each year relative to inflation and what they can spend.
There are 13 instances.
There seems to be not biased as this is a governmental data and all data seems consistent which each other. The dataset is an easy to read xlsx file so basically everyone can read and understand it. 
The dataset is rather small and only relates to the bigger regions of the UK. Therefore, the GDHI is just an average over the entire region. There can still be a lot of differences in the regionby themselves. However, it is nice to compare regions and the local regulations.
The dataset will be used as an independent variable to see if there are any differences to the regions and how they respond to regulation. Additionaly, these effects will be analysed regarding the infections, vaccinations and other demographic data.
There seem to be no data problems as the dataset is pretty small.

Variables:

Countries and regions of the UK | DATA TYPE
Population | DATA TYPE
GDHI per head (£) | Gross disposable household income per head in British Pounds | DATA TYPE | STRING
GDHI per head growth on 2017 (percentage) Growth of gross disposable household income per head in percentage | DATA TYPE | FLOAT
Total GDHI (£ million) | Total gross disposable household income in the UK in British Pounds | DATA TYPE | FLOAT
Total GDHI growth on 2017 (percentage) | Total growth of the total UK gross disposable income | DATA TYPE | FLOAT
Share of the UK population (percentage) | Share of the UK region population in percentage of the total UK population| DATA TYPE | FLOAT
Share of UK total GDHI (percentage) | Share of the UK region population gross disposable income of the total UK population | DATA TYPE | FLOAT


