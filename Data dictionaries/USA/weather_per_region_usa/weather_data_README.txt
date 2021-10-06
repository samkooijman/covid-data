This document describes the contents of the weather per region in USA. The variable names described below refer to column names. The data is fetched by using an API of WorldWeatherOnline. This API is free for 60 days and limited to 500 calls per day. 


Data sources:
• WorldWeatherOnline
(https://www.worldweatheronline.com/developer/)
--------------------------------------------------
General description:
The CSV files retrieved through the API can be used for the KPIs related to this.
In the API, the developer can specify from which date the desired data must be retrieved.
The data can therefore be retrieved historically for the countries that have been selected.
At this moment we have chosen to save the retrieved data in CSV files. 
The column "season" is missing from the API.
It will be created manually during the transformation of the data.

--------------------------------------------------

Description of variables:
(https://www.worldweatheronline.com/developer/api/docs/local-city-town-weather-api.aspx)
date_time: The selected dates. DATA TYPE | DATE
maxtempC: Maximum temperature of the day in degree Celcius. DATA TYPE | INT
mintempC: Minimum temperature of the day in degree Celcius. DATA TYPE | INT
totalSnow_cm: Snow in cm. DATA TYPE | Float
sunHour: Sun hour. DATA TYPE | INT
uvIndex: UV index. DATA TYPE | INT
moon_illumination: Moon illumination. DATA TYPE | DECIMAL
moonrise: Local moonrise time. DATA TYPE | dateTime
moonset: Local moonset time. DATA TYPE | dateTime
sunrise: Local sunrise time. DATA TYPE | dateTime
sunset: Local sunset time. DATA TYPE | dateTime
DewPointC: Dew point temperature in degrees Celsius.   DATA TYPE | INR
FeelsLikeC: Feels like temperature in degree Celcius.  DATA TYPE | INT
HeatIndexC: Heat index temperature in degrees Celsius. DATA TYPE | INT
WindChillC: Wind chill temperature in degrees Celsius. DATA TYPE | INT
WindGustKmph: Wind gust in kilometers per hour. DATA TYPE | INT
cloudcover: Cloud cover amount in percentage(%). DATA TYPE | INT
humidity: Humidity in percentage. DATA TYPE | FLOAT
precipMM: Precipitation in millimeters. DATA TYPE | FLOAT
pressure: Atmospheric pressure in millibars (mb). DATA TYPE | INT
tempC: Temperature in degrees Celsius. DATA TYPE | INT
visibility: Visibility in kilometers. DATA TYPE | INT
winddirDegree: Wind direction in degrees. DATA TYPE | INT
windspeedKmph: Wind speed in kilometers per hour. DATA TYPE | INT
location: Name of the location in the database from where the weather data is being taken. DATA TYPE | String
-------------------------------------------------- 