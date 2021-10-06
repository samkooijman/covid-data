This document describes the contents of the vaccination_covarage_uk file. The variable names described below refer to column names. Data is static and in time-series in xlsx format. Data will be imported using the pandas library and then pass the source to the pd.read_xlsx(). There are no privacy restrictions, all data is public.


Data sources:
• Office for National Statistics UK

--------------------------------------------------
General description:
The dataset contains cumulative data regarding the percentage of antibodies and vaccinations across the entire UK population.A regional and country distinction is made in the dataset. 
The dataset regards adults (16+) who have received 1 dose or more as vaccinated.
Sample groups were taken in blood tests which represents the regional population in the UK. Standard population weighting is used to properly assign conclusions to the population.
Bayesian analysis is used so that credible intervals can tell the dataset is reliable. So there seems to be no bias. Additionaly, it is governmental dat, so a bias would be highly unlikely.
The dataset records the data in a time-series week by week, starting 07 December 2020. The last update of the dataset is on 29 August 2021. Therefore, there are 37 instances (weeks).
The people within the population of the dataset are 16 years and over.
Different age groups are analysed per country in the dataset.
The instances of the dataset end on the last week of August, which make the data possible incomplete to the datasets of the other countries.
The dataset and the number of vaccinations will act as a dependent variable to combine with all the other independent variables discussed in the business understanding.


--------------------------------------------------

Description of variables:

All tables in the dataset:

Antibody and vaccination estimates for England
Table 1a - Antibodies
Table 1b - Antibodies per region
Table 1c - Antibodies by age group
Table 1d - Antibodies by single year of age
Table 1e - Vaccinations
Table 1f - Vaccinations per region
Table 1g - Vaccinations by age group 

Antibody and vaccination estimates for Wales
Table 2a - Antibodies
Table 2b - Antibodies per age group
Table 2c - Antibodies by single year of age
Table 2d - Antibodies by vaccinations
Table 2e - Vaccinations by age group

Antibody and vaccination estimates for Northern Ireland
Table 3a - Antibodies
Table 3b - Antibodies per age group
Table 3c - Antibodies by single year of age
Table 3d - Antibodies by vaccinations
Table 3e - Vaccinations by age group

Antibody and vaccination estimates for Scotland
Table 4a - Antibodies
Table 4b - Antibodies per age group
Table 4c - Antibodies by single year of age
Table 4d - Antibodies by vaccinations
Table 4e - Vaccinations by age group

Description of variables:

The same variables count for every table:

Weekly period. DATA TYPE | STRING |
95% Lower credible interval. DATA TYPE | FLOAT |
95% Upper credible interval. DATA TYPE | FLOAT |
Number of people in sample. DATA TYPE | FLOAT |

The datasets contain the following other variables:

Antibodies:

Modelled % testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |
Number of people testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |

Antibodies per region:

Region. DATA TYPE | STRING |
Modelled % testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |
Number of people testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |

Antibodies by age group

Age group
Modelled % testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |
Number of people testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |

Antibodies by single year of age:

Age. DATA TYPE | INT | 
Modelled % testing positive for COVID-19 antibodies. DATA TYPE | FLOAT |


Antibodies by vaccinations:

Modelled % of adults who have received 1 or more vaccination dose. DATA TYPE | FLOAT |
Number of adults who have reported receiving 1 or more vaccination dose. DATA TYPE | FLOAT |

Vaccinations per region:

Modelled % of adults who have received 1 or more vaccination dose. DATA TYPE | FLOAT |
Number of adults who have reported receiving 1 or more vaccination dose. DATA TYPE | FLOAT |

Vaccination by age group:

Age group
Modelled % of adults who have received 1 or more vaccination dose. DATA TYPE | FLOAT |
Number of adults who have reported receiving 1 or more vaccination dose. DATA TYPE | FLOAT |

