import csv
from datetime import datetime

from matplotlib import pyplot as plt


filename = 'death_valley-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)  # Store this as CSV reader object
    header_row = next(reader)  # Call next once, to get list of headers

    # FIXME: Why can't I use multiple list comprehensions? Only the first returns
    # highs = [int(row[1]) for row in reader]
    # dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in reader]
    highs, dates, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            highs.append(int(row[1]))
            dates.append(current_date)
            lows.append(int(row[3]))
        except ValueError:
            print(current_date, 'missing data')


    # Plot data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot:
    # Title
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    # X axis label
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    # Y axis label
    plt.ylabel("Temperature (F)", fontsize=16)
    # Place ticks on both axes
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Show the graph
    plt.show()
