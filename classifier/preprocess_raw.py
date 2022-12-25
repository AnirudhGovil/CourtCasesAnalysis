import pandas as pd

# Read in the data
df = pd.read_csv('classifier/raw_data.csv')

# Only keep rows where disp_name = [8,9,10,11]
df = df[df['disp_name'].isin([8,9,10,11])]
df = df.reset_index(drop=True)

# Drop all columns except for "act", "section", "judge_position","criminal","type_name","purpose_name","disp_name".
df = df[["act", "section", "judge_position","criminal","type_name","purpose_name","disp_name"]]

# Drop all rows with NaN values.
df = df.dropna()

# Save the data to a new csv file.
df.to_csv('classifier/preprocessed_data.csv')