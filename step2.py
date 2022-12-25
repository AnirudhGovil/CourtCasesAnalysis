# Import the pandas library
import pandas as pd

# Read the data from data/custom/cases_2018_criminal.csv
df = pd.read_csv('data/custom/cases_2018_criminal.csv')

# Print the first 5 rows of the data
print(df.head())

# Read all rows of data/keys/judge_case_merge_key.csv
acts = pd.read_csv('data/keys/judge_case_merge_key.csv')

# For all rows of the data, use ddl_case_id to join the data with acts and save the result in a new variable

joined = df.merge(acts, left_on='ddl_case_id', right_on='ddl_case_id', how='left')

# Print the first 5 rows of the joined data
print(joined.head())

# Save the joined data to data/custom/cases_2018_criminal.csv
joined.to_csv('data/custom/cases_2018_criminal.csv')
