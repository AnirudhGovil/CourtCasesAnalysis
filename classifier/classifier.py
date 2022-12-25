import numpy as np
import pandas as pd
import os


# Train a random forest classifier to predict the disp_name given a set of strings

# Read in the preprocessed data
df = pd.read_csv('classifier/preprocessed_data.csv')

# Split the data into training and testing data
# 80% of the data will be used for training
# 20% of the data will be used for testing
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

# Train the classifier to preditc an integer i.e. disp_name, given a set of strings i.e. act, section, judge_position, criminal, type_name, purpose_name
# Use One Hot Encoding to convert the strings into integers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing

# Convert the strings into integers
le = preprocessing.LabelEncoder()
train['act'] = le.fit_transform(train['act'])
train['section'] = le.fit_transform(train['section'])
train['judge_position'] = le.fit_transform(train['judge_position'])
train['criminal'] = le.fit_transform(train['criminal'])
train['type_name'] = le.fit_transform(train['type_name'])
train['purpose_name'] = le.fit_transform(train['purpose_name'])

# Train the classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=42)


# Fit the classifier to different combinations of features
clf.fit(train[['act', 'section', 'judge_position','criminal','type_name','purpose_name']], train['disp_name'])

# Test the classifier
# Convert the strings into integers
test['act'] = le.fit_transform(test['act'])
test['section'] = le.fit_transform(test['section'])
test['judge_position'] = le.fit_transform(test['judge_position'])
test['criminal'] = le.fit_transform(test['criminal'])
test['type_name'] = le.fit_transform(test['type_name'])
test['purpose_name'] = le.fit_transform(test['purpose_name'])

# Predict the disp_name for the test data
pred = clf.predict(test[['act', 'section', 'judge_position','criminal','type_name','purpose_name']])

# Test the classifier using different combinations of features and print the accuracy
print(clf.score(test[['act', 'section', 'judge_position','criminal','type_name','purpose_name']], test['disp_name']))

# Confusion Matrix as a way to visualize the accuracy of the classifier
from sklearn.metrics import confusion_matrix
print(confusion_matrix(test['disp_name'], pred))




