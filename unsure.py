import csv
import matplotlib
import datetime as dt


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


dates = []
highs = []
lows = []


for row in csv_file:
    try:
        high = int(row[header_row.index("TMAX")])
        low = int(row[header_row.index("TMIN")])
        date = dt.datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")

    except ValueError:
        print(f"Missing data for {row[0]}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

name = str(row[header_row.index("NAME")])
print(highs[:10])
print(name)

##############################################################
##############################################################
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)

dates2 = []
highs2 = []
lows2 = []

for row in csv_file2:
    try:
        high2 = int(row[header_row2.index("TMAX")])
        low2 = int(row[header_row2.index("TMIN")])
        date2 = dt.datetime.strptime(row[header_row2.index("DATE")], "%Y-%m-%d")

    except ValueError:
        print(f"Missing data for {row[0]}")

    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(date)

name2 = str(row[header_row2.index("NAME")])
print(highs2[:10])
print(name2)



import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c="red")  # plt is the actual graph object
plt.plot(dates, lows, c="blue")

plt.title(name, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)

plt.tick_params(axis="both", labelsize=12)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()
# Draws labels daigonnaly to prevent overlapping

plt.show()



fig2 = plt.figure()


plt.plot(dates, highs, c="red")  # plt is the actual graph object
plt.plot(dates, lows, c="blue")

plt.title(name, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)

plt.tick_params(axis="both", labelsize=12)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()
# Draws labels daigonnaly to prevent overlapping

plt.show()

fig = plt.figure()






fig, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")
a[1].plot(dates2, highs2, c="red")
a[1].plot(dates2, lows2, c="blue")

plt.show()
"""