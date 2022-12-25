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

# Convert the strings into integers using LabelEncoder fit_transform on the first row of the training data
le = preprocessing.LabelEncoder()
train['act'] = le.fit_transform(train['act'])
train['section'] = le.fit_transform(train['section'])
train['judge_position'] = le.fit_transform(train['judge_position'])
train['criminal'] = le.fit_transform(train['criminal'])
train['state_code'] = le.fit_transform(train['state_code'])
train['dist_code'] = le.fit_transform(train['dist_code'])
train['court_no'] = le.fit_transform(train['court_no'])
train['female_defendant'] = le.fit_transform(train['female_defendant'])
train['female_petitioner'] = le.fit_transform(train['female_petitioner'])
train['type_name'] = le.fit_transform(train['type_name'])
train['purpose_name'] = le.fit_transform(train['purpose_name'])


# Train the classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=1000, max_depth=3, random_state=42)


# Fit the classifier to different combinations of features
clf.fit(train[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']], train['disp_name'])

# Test the classifier
# Convert the strings into integers
test['act'] = le.fit_transform(test['act'])
test['section'] = le.fit_transform(test['section'])
test['judge_position'] = le.fit_transform(test['judge_position'])
test['criminal'] = le.fit_transform(test['criminal'])
test['state_code'] = le.fit_transform(test['state_code'])
test['dist_code'] = le.fit_transform(test['dist_code'])
test['court_no'] = le.fit_transform(test['court_no'])
test['female_defendant'] = le.fit_transform(test['female_defendant'])
test['female_petitioner'] = le.fit_transform(test['female_petitioner'])
test['type_name'] = le.fit_transform(test['type_name'])
test['purpose_name'] = le.fit_transform(test['purpose_name'])

# Predict the disp_name for the test data
pred = clf.predict(test[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']])

# Test the classifier using different combinations of features and print the accuracy
print(clf.score(test[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']], test['disp_name']))

# Confusion Matrix as a way to visualize the accuracy of the classifier
from sklearn.metrics import confusion_matrix
print(confusion_matrix(test['disp_name'], pred))

# Visualise which features are most important
import matplotlib.pyplot as plt
importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_],
                axis=0)
indices = np.argsort(importances)[::-1]
# Map the feature indices to the feature names
dict = {0: 'act', 1: 'section', 2: 'judge_position', 3: 'criminal', 4: 'state_code', 5: 'dist_code', 6: 'court_no', 7: 'female_defendant', \
8:'female_petitioner', 9: 'type_name', 10: 'purpose_name'}


# Print the feature ranking by importance and mention the feature name
print("Feature ranking:")
for f in range(train[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']].shape[1]):
    print("%d. feature %s (%f)" % (f + 1, dict[indices[f]], importances[indices[f]]))
# Plot the feature importances of the forest
plt.figure(figsize=(20,10))
plt.title("Feature importances")
plt.bar(range(train[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']].shape[1]), importances[indices], color="r", yerr=std[indices], align="center")  
plt.xticks(range(train[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']].shape[1]), [dict[i] for i in indices])
plt.xlim(-1, train[['act', 'section', 'judge_position','criminal','state_code','dist_code','court_no','female_defendant','female_petitioner','type_name','purpose_name']].shape[1])
plt.show()




