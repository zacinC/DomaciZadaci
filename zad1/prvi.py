import csv
import numpy as np
from itertools import combinations

passenger_ids = []
data = []
sum = 0

with open('test/zad1/test.xls', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        data.append(row)
        passenger_id = row[0]
        passenger_ids.append(int(passenger_id))
        sum += int(passenger_id)
    csvfile.close()
minId = min(passenger_ids)
maxId = max(passenger_ids)
average_value = sum/len(passenger_ids)
percentage_difference = (maxId - average_value)/100
normalised_ids = [(id - minId) / (maxId - minId) for id in passenger_ids]
print(minId, maxId, average_value, percentage_difference)
print(normalised_ids)

# Read data from CSV file
data = []
with open('test/zad1/test.xls', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
