# Import the pandas library
import pandas as pd
import matplotlib as plt

# Read the data from data/custom/cases_2018_criminal.csv 
df = pd.read_csv('data/custom/cases_2018_criminal.csv')

# Drop all rows where ddl_decision_judge_id is NaN
df = df.dropna(subset=['ddl_decision_judge_id'])

# Drop all rows where date_of_filing is NaN
df = df.dropna(subset=['date_of_filing'])

# Convert the date_of_filing column to datetime
df['date_of_filing'] = pd.to_datetime(df['date_of_filing'])

# For each unique value of ddl_decision_judge_id, find how many cases were filed
temp = df.groupby('ddl_decision_judge_id').apply(lambda x: x['date_of_filing'].count())

# Drop all rows where date_of_decision is NaN
df = df.dropna(subset=['date_of_decision'])

# Convert the date_of_decision column to datetime
df['date_of_decision'] = pd.to_datetime(df['date_of_decision'])

# Print the first 5 rows of the data
print(df.head())


# For each unique value of ddl_decision_judge_id, find how many cases were decided within 1 year of filing
judge_counts = df.groupby('ddl_decision_judge_id').apply(lambda x: (x['date_of_decision'] - x['date_of_filing']).dt.days.le(365).sum())

judge_counts = judge_counts / temp

# Sort the values in descending order
judge_counts = judge_counts.sort_values(ascending=False)

# Plot the cumulative distribution function, where the x-axis is the percentage of cases where decision was reached within 1 year of filing
# and the y-axis is the number of judges who have that percentage of cases where decision was reached within 1 year of filing
# Save the plot to data/custom/judge_counts.png and label the axes
judge_counts.plot(kind='hist', bins=10000, cumulative=True)
plt.pyplot.xlabel('Percentage of cases where date_of_decision was reached within 1 year of filing')
plt.pyplot.ylabel('Number of judges')
plt.pyplot.title('Judges by percentage of cases where decision was reached within 1 year of filing')

# Print the mean, median, and standard deviation of the judge_counts and show them in the plot
print('Mean: ', judge_counts.mean())
print('Median: ', judge_counts.median())
print('Standard Deviation: ', judge_counts.std())
plt.pyplot.axvline(judge_counts.mean(), color='r', linestyle='dashed', linewidth=2, label='Mean')
plt.pyplot.axvline(judge_counts.median(), color='g', linestyle='dashed', linewidth=2, label='Median')

# Save the plot to data/custom/judge_counts.png
plt.pyplot.savefig('data/custom/judge_counts.png')

# Save the results to data/custom/judge_counts.csv
judge_counts.to_csv('data/custom/judge_counts.csv')

