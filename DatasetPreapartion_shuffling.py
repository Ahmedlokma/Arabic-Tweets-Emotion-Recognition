import csv
import random

# Read the contents of the input CSV file into a list
with open('output.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Shuffle the rows of the list
random.shuffle(data)

# Write the shuffled rows to a new CSV file
with open('output2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
