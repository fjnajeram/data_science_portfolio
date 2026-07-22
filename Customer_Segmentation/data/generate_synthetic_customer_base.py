'''
create synthetic data for a dictionary where:
# Sample data format for sample_customers.csv:
data = {
    'CustomerID': [1, 2, 3, 4, 5, ...],
    'SpendScore': [75.5, 62.3, 88.9, 45.2, 91.0, ...],
    'EngagementScore': [82.1, 65.4, 95.2, 38.7, 88.5, ...],
    'Age': [28, 45, 52, 23, 67, ...],
    'Gender': ['M', 'F', 'M', 'F', 'M', ...],
    'Location': ['East', 'West', 'North', 'South', 'East', ...]
}
df = pd.DataFrame(data)
df.to_csv('data/sample_customers.csv', index=False)


'''

import pandas as pd
import random

num_samples = 10000
random.seed(31)
data = {'CustomerID':[],
    'SpendScore':[],
    'EngagementScore':[],
    'Age':[],
    'Gender':[],
    'Location':[]}

for i in range(num_samples):
    data['CustomerID'].append(i+1)
    data['SpendScore'].append(random.uniform(50, 100))
    data['EngagementScore'].append(random.uniform(50, 100))
    # Generate random age and gender but giving the population a normal distribution where the median is around 40, cropping the distribution to 18 years
    data['Age'].append(max(18, random.normalvariate(40, 10)))
    data['Gender'].append(  random.choice(['Male', 'Female']))
    data['Location'].append(random.choice(['East', 'West', 'North', 'South']))

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('sample_customers.csv', index=True)

print("Data generation complete.")

