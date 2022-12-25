# Import the pandas library
import pandas as pd
import matplotlib as plt

# Save the data from women_cases.csv to a variable
df = pd.read_csv('data/cases/cases_2018.csv')

# Save the act_key.csv to a variable
judges = pd.read_csv('data/keys/judge_case_merge_key.csv')

# Merge df and judges based on the "ddl_case_id" column
df = pd.merge(df, judges, left_on='ddl_case_id', right_on='ddl_case_id', how='left')

# Save the result to a csv file
df.to_csv('data/custom/women_cases_judges.csv', index=False)










