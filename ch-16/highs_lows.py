import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)  # Store this as CSV reader object
    header_row = next(reader)  # Call next once, to get list of headers
    # print(header_row)  # Print the headers

    # Note: Use enumerate to acces the index
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    # Get high temperature: Store the first value of each row
    highs = [int(row[1]) for row in reader]

    print(highs)
