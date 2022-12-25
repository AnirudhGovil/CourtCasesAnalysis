# Import the pandas library
import pandas as pd
import matplotlib.pyplot as plt

# Save the data from data/custom/district_data.csv to a variable
df = pd.read_csv('data/custom/district_data.csv')

# Group the data by "state_id" and "state_name" and sum the "count" column
df = df.groupby(['state_code', 'state_name']).sum().reset_index()

# Plot a bar chart of the data
df.plot.bar(x='state_name', y='count', rot=90, figsize=(20,10))
plt.title("Number of cases regarding women's safety in each state in 2018")
plt.show()















