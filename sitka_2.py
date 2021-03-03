import csv
import datetime as dt

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# Looking at index value as well as column header; what index value is associte with what record

# The Enumerate() function returns both index of each item adn the value of each item as you loop through a list

for index, header in enumerate(header_row):
    print("Index:", index, "Column Header:", header)

# output is  a tuple!

highs = []
dates = []

"""
Version 1 (functional!)

for row in csv_file:
    highs.append(int(row[5]))
    dates.append(row[2])  
"""

# Version 2 (in class):
somedate = "2010-02-18"
converted_date = dt.datetime.strptime(somedate, "%Y-%m-%d")

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = dt.datetime.strptime(somedate, "%Y-%m-%d")
    dates.append(converted_date)


# print(highs)

# Let's extract the date to print on the graph with the highs


import matplotlib.pyplot as plt

fig = plt.figure()

fig.autofmt_xdate()

plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=12)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()

"""
Example: 
somedate = "2-10-07-01"
converted_date = dt.datetime.strptime(somedate, "%Y-%m-%d")  # this line doesn't work
# This could hypothetically strip a time

print(converted_date)

# Says no attribute strptime
"""