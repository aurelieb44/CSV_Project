import csv

open_file = open('sitka_weather_07-2018_simple.csv', 'r')
csv_file = csv.reader(open_file, delimiter = ',')
header_row = next(csv_file)

print(type(header_row))
# every row is considered a list

for index, column_header in enumerate(header_row): # can use enumerate on any kind of list object
    print(index, column_header)

highs = []

for row in csv_file: 
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

# create a plot
plt.plot(highs, c="red")
plt.title("Daily high temperature, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16) # major tick

plt.show() # to show the plot







