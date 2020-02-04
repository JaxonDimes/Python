# Imports
import pyodbc
import matplotlib.pyplot as plt
from plotly.graph_objects import Bar, Layout
from plotly import offline

# Lists/Variables
item_total = []
total = []
frequencies = []
total_sold = 0
b = 0

# Connecting to the Driver
conn = pyodbc.connect\
    (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=N:\Fruit Sale Project\2019AnthisFruit.accdb;')
cursor = conn.cursor()
cursor.execute('select * from FruitSale')

# This simply justs gets the required index you provide and appends it to item_total
for rows in cursor.fetchall():
    item_total.append(rows[4])

# This now, this is the stuff. This ciphers out the Nones and ignores them, by placing the float/integers into a list.
for item in item_total:
    if item is not None:
        total.append(item)

# This adds up all the items in the index for the column. (amount sold)
for thing in total:
    total_sold = total_sold + thing

# Natural born print statements
print(item_total)
print(total)
print(total_sold)

# This finds the largest amount sold in one sitting. This becomes our x or y highest coordinate.
for i in total:
    if i > b:
        b = i
    elif i < b:
        b = b
max_result = b

for value in list(range(1, int(b))):
    frequency = total.count(value)
    frequencies.append(value)
    frequencies.append(frequency)

print(frequencies)

# Visualization
x_values = total
data = [Bar(x=frequencies.sort(), y=x_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of how many Clementines were sold in one sitting.',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='Fruit_Sale_Vis')
