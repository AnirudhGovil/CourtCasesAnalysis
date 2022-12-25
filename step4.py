# Import the pandas library
import pandas as pd
import matplotlib as plt

# Read the data from data/custom/cases_2018_criminal.csv 
df = pd.read_csv('data/custom/cases_2018_criminal.csv')

# Drop all rows where ddl_decision_judge_id is NaN
df = df.dropna(subset=['ddl_decision_judge_id'])

# Drop all rows where 'state_code', 'dist_code' or 'court_no' is NaN
df = df.dropna(subset=['state_code', 'dist_code', 'court_no'])

# Drop all rows where date_of_filing is NaN
df = df.dropna(subset=['date_of_filing'])

# Convert the date_of_filing column to datetime
df['date_of_filing'] = pd.to_datetime(df['date_of_filing'], errors='coerce')

# For each unique value of ddl_decision_court_id, find how many cases were filed
temp = df.groupby(['state_code', 'dist_code', 'court_no']).apply(lambda x: x['date_of_filing'].count())

# Drop all rows where date_of_decision is NaN
df = df.dropna(subset=['date_of_decision'])

# Convert the date_of_decision column to datetime
df['date_of_decision'] = pd.to_datetime(df['date_of_decision'])

# Print the first 5 rows of the data
print(df.head())


# For each unique value of ddl_decision_court_id, find how many cases were decided within 1 year of filing
court_counts = df.groupby(['state_code', 'dist_code', 'court_no']).apply(lambda x: (x['date_of_decision'] - x['date_of_filing']).dt.days.le(365).sum())

court_counts = court_counts / temp

# Sort the values in descending order
court_counts = court_counts.sort_values(ascending=False)

# Plot the cumulative distribution function, where the x-axis is the percentage of cases where decision was reached within 1 year of filing
# and the y-axis is the number of courts who have that percentage of cases where decision was reached within 1 year of filing
# Save the plot to data/custom/court_counts.png and label the axes
court_counts.plot(kind='hist', bins=10000, cumulative=True)
plt.pyplot.xlabel('Percentage of cases where date_of_decision was reached within 1 year of filing')
plt.pyplot.ylabel('Number of Courts')
plt.pyplot.title('Courts by percentage of cases where decision was reached within 1 year of filing')

# Print the mean, median, and standard deviation of the court_counts and show them in the plot
print('Mean: ', court_counts.mean())
print('Median: ', court_counts.median())
print('Standard Deviation: ', court_counts.std())
plt.pyplot.axvline(court_counts.mean(), color='r', linestyle='dashed', linewidth=2, label='Mean')
plt.pyplot.axvline(court_counts.median(), color='g', linestyle='dashed', linewidth=2, label='Median')

# Save the plot to data/custom/court_counts.png
plt.pyplot.savefig('data/custom/court_counts.png')

# Save the results to data/custom/court_counts.csv
court_counts.to_csv('data/custom/court_counts.csv')

