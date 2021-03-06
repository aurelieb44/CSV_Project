# changing the file to include all the data for the year of 2018 o
# change the title to Daily low and high temperatures - 2018
# extract low temps from the file and add to chart
# shade in the area between high and low

import csv
from datetime import datetime

open_file = open('death_valley_2018_simple.csv', 'r')
csv_file_dv = csv.reader(open_file, delimiter = ',')
open_file = open('sitka_weather_2018_simple.csv', 'r')
csv_file_s = csv.reader(open_file, delimiter = ',')
header_row_dv = next(csv_file_dv)
header_row_s = next(csv_file_s)

# SITKA

header_row_s_dict = {}
for index_s, column_header in enumerate(header_row_s): # can use enumerate on any kind of list object
    print(index_s, column_header)
    header_row_s_dict[column_header] = index_s
print(header_row_s)

highs_s = []
lows_s = []
dates_s = []

for row in csv_file_s: 

    try:
        high = int(row[header_row_s_dict['TMAX']])
        low = int(row[header_row_s_dict['TMIN']])
        current_date = datetime.strptime(row[header_row_s_dict['DATE']], '%Y-%m-%d')
        title_s = row[header_row_s_dict['NAME']]
    
    except ValueError:  # doesn’t break the program, it just skips a row
        print(f"Missing Data for {current_date}") # to print out if we get a value error

    else:
        highs_s.append(high)
        lows_s.append(low)
        dates_s.append(current_date)

# DEATH VALLEY

header_row_dv_dict = {}
for index_dv, column_header in enumerate(header_row_dv): # can use enumerate on any kind of list object
    print(index_dv, column_header)
    header_row_dv_dict[column_header] = index_dv
print(header_row_dv)

highs_dv = []
lows_dv = []
dates_dv = []

for row in csv_file_dv: 

    try:
        high = int(row[header_row_dv_dict['TMAX']])
        low = int(row[header_row_dv_dict['TMIN']])
        current_date = datetime.strptime(row[header_row_dv_dict['DATE']], '%Y-%m-%d')
        title_dv = row[header_row_dv_dict['NAME']]
    
    except ValueError:  # doesn’t break the program, it just skips a row
        print(f"Missing Data for {current_date}") # to print out if we get a value error

    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(current_date)

# GRAPH

import matplotlib.pyplot as plt
fig = plt.figure() 

plt.tick_params(axis="both", which="major", labelsize=16) # major tick

plt.subplot(2,1,1)
plt.plot(dates_s,highs_s, c='red')
plt.plot(dates_s,lows_s, c='blue')
plt.fill_between(dates_s, highs_s, lows_s, facecolor = 'blue', alpha = 0.1)
plt.title(title_s)

plt.subplot(2,1,2) # second subplot
plt.plot(dates_dv,highs_dv, c='red')
plt.plot(dates_dv,lows_dv, c='blue')
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor = 'blue', alpha = 0.1)
plt.title(title_dv)

plt.suptitle("Temperature Comparison between SITKA AIRPORT, AK US, AND DEATH VALLEY, CA US,2018")

fig.autofmt_xdate()  
plt.show()


