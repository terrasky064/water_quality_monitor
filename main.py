import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir("C:\Projects\Water_Quality_Project\Data")
csv_file='water_quality_data.csv'

import csv
with open(csv_file, 'r') as file:
    reader = csv.reader(file,delimiter  = ';')
    for each_row in reader:
        print(each_row)


data = pd.read_csv(csv_file)
df = pd.DataFrame(data)
# Show the plot
plt.show()

'''date = data["Date"]
time = data["Time"]
ph = data["pH"]
chlorine = data["Chlorine"]
residual = data["Residual"]

x = []
y = []
a = []
b = []

x=list(date, time)
y=list(chlorine, residual)
a=list(chlorine)
b=list(residual)

plt.scatter(x,y)
plt.xlabel('Date/Time->')
plt.ylabel('Chlorine & Residual->')
plt.title('Data')
plt.show()'''

# Plot
plt.figure(figsize=(6.8, 4.2))
x = range(len(data['Date']))
plt.plot(x, data['pH'])
plt.xticks(x, data['Date'])
plt.xlabel('Date')
plt.ylabel('pH')
plt.show()