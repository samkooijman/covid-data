import pandas as pd

# #Downloading data
# #Sentiment, is still a zip, needs to be unzipped
# Sentiment_DENMARK = pd.read_csv('https://www.openicpsr.org/openicpsr/project/120321/version/V10/view?path=/openicpsr/120321/fcr:versions/V10/Twitter-COVID-dataset---Sep2021/tweetid_userid_keyword_sentiments_emotions_Denmark.csv.zip&type=file')
# Sentiment_USA = pd.read_csv('https://www.openicpsr.org/openicpsr/project/120321/version/V10/view?path=/openicpsr/120321/fcr:versions/V10/Twitter-COVID-dataset---Sep2021/tweetid_userid_keyword_sentiments_emotions_United-States.csv.zip&type=file')
# Sentiment_UK = pd.read_csv('https://www.openicpsr.org/openicpsr/project/120321/version/V10/view?path=/openicpsr/120321/fcr:versions/V10/Twitter-COVID-dataset---Sep2021/tweetid_userid_keyword_sentiments_emotions_United-Kingdom.csv.zip&type=file')
#
# #Stringency index, needs to be stored locally or JSON
# #Stringency_Index = pd.read_csv('/src/stringency_index.csv', sep='\t', header=None)
# Stringency_Index = pd.read_csv(r'C:\Users\mickm\OneDrive\OneDrive - Universiteit Utrecht\Leerjaar 2\INFOMDSS Data Science and Society\Project Group\src\stringency_index.csv', sep=',', header=None)
#
# #Average income per region
# Average_income_region_denmark = pd.read_csv('https://www.statbank.dk/statbank5a/selectvarval/saveselections.asp')
# Average_income_region_uk = pd.read_csv('https://www.ons.gov.uk/download/table?format=csv&uri=/economy/regionalaccounts/grossdisposablehouseholdincome/bulletins/regionalgrossdisposablehouseholdincomegdhi/1997to2018/ef135495.json)
# Average_income_region_usa = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD&bom=true&format=true&delimiter=%3B')
#
# #Infections per region
# Infections_per_region_denmark = pd.read_csv('')
# Infections_per_region_UK = pd.read_csv("https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=capacityPillarFour&format=csv")
# Infections_per_region_USA = pd.read('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD')
#
# #Politcal preference per region
# Political_preference_per_region_denmark = pd.read_csv('://www.statbank.dk/statbank5a/selectvarval/saveselections.asp')
#Political_preference_per_region_UK = pd.read_excel("https://data.parliament.uk/resources/constituencystatistics/general-election-results-2019.xlsx")
# Political_preference_per_region_USA = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/955555/1790759/governors_county_candidate.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211102%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211102T112030Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=63097ad07fa6e46010e0de076ed1eef16bd44459ccd0f2e8375ce1e76a8ea133d1edc8bb4d7f9d9da5403b2f0a2cf7204652f0eb2e881ece2f7e9f0eb4434e565ced21397db7e2acc329a7497ffca7a501b5a8abf3353f0788ba7e281806c2616d4ad411b7784e62d375409f4edfdb09b59a0dcfb6ad05c486c5912b7544e1a5e2fd94b6e8f015f8aac445bbf6d5608c35b5ac5f5ee64739268564810f5534868a9507012895d39766f0d2bfb54e30eb1baf08b026a25e97895e461cf6558e0a8c085c0c77f428ea7a324e1745212914ddef1794f44494c4ca22fe5546f6b83744f062790845b9344d7a7728d84dad6cac9688dbc293f5fae3c47f0e1934cf2c')
#
# #Population density per region
# Population_density_per_region_denmark =  pd.read_csv('https://www.statbank.dk/0_1/Save/?format=excel&root=/statbank5a/&pxid=2021112111732350218028FOLK1A&dbl=0&sfn=2')
# Population_density_per_region_UK = pd.read_csv('')
# Population_density_per_region_USA = pd.read_csv('https://www.statbank.dk/0_1/Save/?format=excel&root=/statbank5a/&pxid=2021112122232350227348FOLK1A&dbl=0&sfn=2')
#
# #Vaccination coverage
# Vaccination_coverage_per_region_Denmark = pd.read_csv("https://files.ssi.dk/covid19/vaccinationsdata/zipfil/vaccinationsdata-dashboard-covid19-01112021-007u")
# Vaccination_coverage_per_region_UK = pd.read_csv('')
# Vaccination_coverage_per_region_USA = pd.read_csv('https://data.cdc.gov/api/views/unsk-b7fc/rows.csv?accessType=DOWNLOAD&bom=true&format=true&delimiter=%3B')
#
# #Weather per region
#
#
#
# #Cleaning data
#
#
#
#
#
#
