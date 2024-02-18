# place your code to clean up the data file below.

import csv

processed_data = []

# open the raw data file in read mode
with open("data/raw_data.csv", 'r', newline = '') as f_raw:
    reader = csv.reader(f_raw)
    header = next(reader) # read the header
    header.pop(3)  # remove the fourth column from the header
    
    for row in reader:
        row[0] = row[0][:5]  # extract the first five characters of the ZIP code
        row.pop(3)  # delete the original fourth column 
        if row[2] != '':  # remove missing values
            processed_data.append(row)

# sort the processed data by building type(column 1) and utility(column 3)
sorted_data = sorted(processed_data, key = lambda x: (x[1], x[3]))

# store the cleaned and sorted data to the clean file
with open("data/clean_data.csv", 'w', newline = '') as f_clean:
    writer = csv.writer(f_clean)
    writer.writerow(header) 
    writer.writerows(sorted_data) 

