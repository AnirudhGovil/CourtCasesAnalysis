# Import the pandas library
import pandas as pd
import matplotlib as plt

# Save the data from women_cases.csv to a variable
df = pd.read_csv('data/custom/women_cases.csv')

# Save the act_key.csv to a variable
acts = pd.read_csv('data/keys/act_key.csv')

# Save the section_key.csv to a variable
sections = pd.read_csv('data/keys/section_key.csv')

# Find the top 10 most common entries in "act" of the df
top_acts = df.act.value_counts().head(10)
for i in top_acts.index:
    print(acts[acts.act == i].act_s.values[0]," - ",int(top_acts[i]))

# Find the top 10 most common entries in "section" of the df
top_sections = df.section.value_counts().head(10)
for i in top_sections.index:
    print(sections[sections.section == i].section_s.values[0]," - ",int(top_sections[i]))









