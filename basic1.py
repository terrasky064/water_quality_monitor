import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("C:\Users\cyberkitsune096\Documents\Water_Quality_Project")
csv_file='testdata_1.csv'


# Load data
data = pd.read_csv('csv_file')
'''
# Plot
plt.figure(figsize=(6.8, 4.2))
x = range(len(data['month']))
plt.plot(x, data['sales'])
plt.xticks(x, data['month'])
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
'''
df =pd.read_csv('filename.csv', sep=',')

months = {'jan':1,
          'feb':2,
          'mar':3,
          'apr':4,
          'may':5,
          'jun':6,
          'jul':7,
          'aug':8,
          'sep':9,
          'oct':10,
          'nov':11,
          'dec':12
         }

plt.plot(df['month'].replace(months), df['sales'], label='sales')
plt.plot(df['month'].replace(months), df['expenditure'], label='expenditure')

plt.gca().set_xticks(list(months.values()))
plt.gca().set_xticklabels(list(months.keys()))
plt.legend()