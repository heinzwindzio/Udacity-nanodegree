import numpy as np
import pandas as pd
import os

# os.path.exists('C:\\Heinz\\python\\projects\\Udacity\\Course 6 - Neural Networks\\Unit 3 - Implementing Gradient Descent\\binary.csv')

admissions = pd.read_csv('C:\\Heinz\\python\\projects\\Udacity\\Course 6 - Neural Networks\\Unit 3 - Implementing Gradient Descent\\binary.csv')

# Make dummy variables for rank
data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)
data = data.drop('rank', axis=1)

#print(f'data:\n {data}')

# Standarize features
for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:, field] = (data[field] - mean) / std

#print(f'new data:\n {data}')
    
# Split off random 10% of the data for testing
np.random.seed(42)
sample = np.random.choice(data.index, size=int(len(data) * 0.9), replace=False)
#print('sample: \n', sample)

data, test_data = data.iloc[sample], data.drop(sample)
#print('data: \n', data)

# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']