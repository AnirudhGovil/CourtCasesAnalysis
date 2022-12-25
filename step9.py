# Import the pandas library
import pandas as pd
import matplotlib as plt

# Save the data from women_cases_judges.csv to a variable
df = pd.read_csv('data/custom/women_cases.csv')

# Save the "state_code", "dist_code" and "court_no" columns to a new dataframe
df = df[['state_code', 'dist_code', 'court_no']]

# Count the number of cases for each combination of "state_code" and "dist_code" and save it to a column named "count"
count = df.groupby(['state_code', 'dist_code']).size().reset_index(name='count')

# Save the data from data/keys/cases_district_key.csv to a variable
districts = pd.read_csv('data/keys/cases_district_key.csv')

# Merge count and districts based on the "state_code" and "dist_code" columns
count = pd.merge(count, districts, left_on=['state_code', 'dist_code'], right_on=['state_code', 'dist_code'], how='left')

# Save the result to a csv file
count.to_csv('data/custom/district_data.csv', index=False)














