
This document describes the contents of the  Twitter_Sentiment file. The variable names described below refer to column names. Data is static in csv format. Data will be imported using the pandas library and then pass the source to the pd. read_csv(). There are no privacy restrictions, all data is public. 


Data sources: 

•  OPEN ICPSR, database for behavioral, health and social science. https://www.openicpsr.org/openicpsr/project/120321/version/V10/view?path=/openicpsr/120321/fcr:versions/V10/Twitter-COVID-dataset---Sep2021&type=folder 

 

-------------------------------------------------- 

General description: 

 

A static dataset is retrieved from an opensource database named ‘OPEN ICPSR’, in which an overview of calculated sentiment and emotion scores of tweets regarding the pandemic is presented. usage of Twitters’ standard API has limitations as it does not allow for exhaustive collection of tweets due to indexing. The acquired tweets from 28 January 2020 to 18 March 2021, merely contain the first 144 characters of the texts of tweets are collected. When making comparisons before and after this date, we expect to reprocess this part of the dataset. We additionally expect to cleanse data as there are some unexplainable deviations in the numerical values.  

 

-------------------------------------------------- 

Description of variables: 

 

User_id - unique identifier for the Twitter user | DATA TYPE | FLOAT | 

Tweet_id - a unique identifier for the associated tweet | DATA TYPE | FLOAT |	 

keywords - used words to retrieve the tweets- | DATA TYPE | STRING | 

time_stamp – time of the creation of the tweet | DATA TYPE | DATETIME64[NS] | 

Valence_intensity  - indicates intensity of expressed emotion | DATA TYPE | STRING | 

Fear_intensity - indicates intensity of expressed emotion | DATA TYPE | STRING | 

Anger_intensity - indicates intensity of expressed emotion | DATA TYPE | STRING | 

Happiness_intensity - indicates intensity of expressed emotion | DATA TYPE | STRING | 

Sadness_intensity - indicates intensity of expressed emotion | DATA TYPE | STRING | 

Sentiment- categorical value consisting of one in five classes | DATA TYPE | STRING| 

Emotion – categorical value describing one. of five emotion classes | DATA TYPE | STRING| 
