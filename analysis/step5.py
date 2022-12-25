# Import the pandas library
import pandas as pd
import matplotlib as plt
import re

# For case insensitive keywords "woman" and "women", return the "act" column from data/keys/act_key.csv
acts = pd.read_csv('data/keys/act_key.csv')
ids = acts.act_s.str.contains('woman|women|mahila', flags = re.IGNORECASE, regex = True, na = False)
acts = acts[ids]

# For case insensitive keywords "woman" and "women", return the "section" ccolumn from data/keys/section_key.csv
sections = pd.read_csv('data/keys/section_key.csv')
ids = sections.section_s.str.contains('woman|women|mahila', flags = re.IGNORECASE, regex = True, na = False)
sections = sections[ids]

# Save the above results to a csv file
acts.to_csv('data/custom/women_acts.csv', index=False)
sections.to_csv('data/custom/women_sections.csv', index=False)





