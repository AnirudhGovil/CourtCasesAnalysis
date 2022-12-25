# Import the pandas library
import pandas as pd
import matplotlib as plt

# Read the data from data/custom/cases_2018_criminal.csv where date_of_filing is no more than 1 year before date_of_decision
df = pd.read_csv('data/custom/cases_2018_criminal.csv', parse_dates=['date_of_filing', 'date_of_decision'])

# Merge the data with the data from data/keys/cases_court_key.csv using a joint key of state_code,dist_code and court_no
df = df.merge(pd.read_csv('data/keys/cases_court_key.csv'), left_on=['state_code', 'dist_code', 'court_no'], right_on=['state_code', 'dist_code', 'court_no'])

# Print the first 5 rows of the data
print(df.head())

# For each unique value of the combination of state_code,dist_code and court_no, calculate the number of cases filed
temp = df.groupby(['state_code', 'dist_code', 'court_no']).size()

# For each unique value of the combination of state_code,dist_code and court_no, calculate the number of cases where decision was reached within 1 year of filing
court_counts = df[df['date_of_decision'] - df['date_of_filing'] <= pd.Timedelta('365 days')].groupby(['state_code', 'dist_code', 'court_no']).size()

court_counts = court_counts / temp

# Sort the values in descending order
court_counts = court_counts.sort_values(ascending=False)

# Plot the cumulative distribution function, where the x-axis is the percentage of cases where decision was reached within 1 year of filing
# and the y-axis is the number of judges who have that percentage of cases where decision was reached within 1 year of filing
# Save the plot to data/custom/judge_counts.png and label the axes
court_counts.plot(kind='hist', bins=10000, cumulative=True)
plt.pyplot.xlabel('Percentage of cases where date_of_decision was reached within 1 year of filing')
plt.pyplot.ylabel('Number of Courts')
plt.pyplot.title('Courts by percentage of cases where decision was reached within 1 year of filing')

# Print the mean, median, and standard deviation of the judge_counts and show them in the plot
print('Mean: ', court_counts.mean())
print('Median: ', court_counts.median())
print('Standard Deviation: ', court_counts.std())
plt.pyplot.axvline(court_counts.mean(), color='r', linestyle='dashed', linewidth=2, label='Mean')
plt.pyplot.axvline(court_counts.median(), color='g', linestyle='dashed', linewidth=2, label='Median')


# Save the plot to data/custom/court_counts.png
plt.pyplot.savefig('data/custom/court_counts.png')

# Save the results to data/custom/court_counts.csv
court_counts.to_csv('data/custom/court_counts.csv')


