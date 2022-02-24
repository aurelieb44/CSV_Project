# changing the file to include all the data for the year of 2018 o
# change the title to Daily low and high temperatures - 2018
# extract low temps from the file and add to chart
# shade in the area between high and low

import csv
from datetime import datetime

open_file = open('death_valley_2018_simple.csv', 'r')
csv_file = csv.reader(open_file, delimiter = ',')
header_row = next(csv_file)

#print(header_row)
# every row is considered a list



for index, column_header in enumerate(header_row): # can use enumerate on any kind of list object
    print(index, column_header)

highs = []
lows = []
dates = []
for row in csv_file: 

    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    
    except ValueError:  # doesn’t break the program, it just skips a row
        print(f"Missing Data for {current_date}") # to print out if we get a value error

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
#print(highs)
#print(dates)
#print(lows)

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)

import matplotlib.pyplot as plt
fig = plt.figure()

# create a plot
plt.plot(dates,highs,c='red')
plt.plot(dates,lows, c='blue')

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
# give x axis location # give two y axis locations # alpha closer to 0 is more transparent

plt.title("Daily low and high temperature, 2018", fontsize=16)
plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16) # major tick

fig.autofmt_xdate()

plt.show() # so it only shows the second graph/subplot

