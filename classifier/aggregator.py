import pandas as pd
import os

# Merge cases with acts_sections.csv

df = pd.read_csv('data/acts_sections.csv')
df = df.drop_duplicates()

df2 = pd.read_csv('data/cases/cases_2018.csv')
df2 = df2.drop_duplicates()

df3 = pd.merge(df, df2, left_on='ddl_case_id', right_on='ddl_case_id')

df3.to_csv('raw_data.csv')