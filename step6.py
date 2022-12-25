# Import the pandas library
import pandas as pd
import matplotlib as plt

# # Save the data from data/acts_sections.csv to a variable
# df = pd.read_csv('data/acts_sections.csv')

# Read the data from data/custom/cases_2018_criminal.csv 
df = pd.read_csv('data/custom/cases_2018_criminal.csv')

# Save the data from data/custom/women_acts.csv to a variable
acts = pd.read_csv('data/custom/women_acts.csv')

# Save the data from data/custom/women_sections.csv to a variable
sections = pd.read_csv('data/custom/women_sections.csv')

# Count the number of cases for which the "act" column matches any value in "act" column of acts OR "section" column matches any value in "section" column of sections
m = df.act.isin(acts.act) | df.section.isin(sections.section)
df = df[m]

# Save the result to a csv file
df.to_csv('data/custom/women_cases.csv', index=False)






