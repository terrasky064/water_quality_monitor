import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
os.chdir(r"C:\Users\cyberkitsune096\Documents\Projects\water_quality_monitor-main\water_quality_monitor-main")
csv_file='water_quality_data.csv'

import csv
with open(csv_file, 'r') as file:
    reader = csv.reader(file,delimiter  = ';')
    for each_row in reader:
        print(each_row)

data = pd.read_csv(csv_file)

usr_input = input("Input: ")
while (usr_input != '1') and (usr_input != '2'):
    usr_input = input("Input: ")

if usr_input == '1':
    fig1 = px.line(data, x = 'Date', y = 'pH', title='pH Date graph')
    fig1.show()
elif usr_input == '2':
    fig2 = px.line(data, x = 'Date', y = 'Chlorine_Residual', title='Chlorine Residual Date graph')
    fig2.show()


df1 = pd.DataFrame(data)
# Show the plot
plt.show()

#Unnamed 0 = date; Unnamed 3 = pH

'''fig1 = px.line(data, x = 'Date', y = 'pH', title='pH Date graph')
fig1.show()

fig2 = px.line(data, x = 'Date', y = 'Chlorine_Residual', title='Chlorine Residual Date graph')
fig2.show()'''

'''#date = data['Date']
#time = data["Time"]
ph = data["pH"]
chlorine = data["Chlorine Residual"]

x = []
y = []
a = []

x=list(date)
y=list(ph)
a=list(chlorine)

plt.scatter(x,y)
plt.xlabel('Date->')
plt.ylabel('pH->')
plt.title('Data')
plt.show()

plt.scatter(x,y)
plt.xlabel('Date->')
plt.ylabel('Chlorine Residual->')
plt.title('Data')
plt.show()

# Plot
plt.figure(figsize=(6.8, 4.2))
x = range(len(data['Date']))
plt.plot(x, data['pH'])
plt.xticks(x, data['Date'])
plt.xlabel('Date')
plt.ylabel('pH')
plt.show()'''