import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
sum = 0


def calcMean(data):
    length = len(data)
    total = 0
    for e in data:
        total += float(e)

    mean = total / length
    return mean


squared_list = []
for i in data:
    a = int(i) - calcMean(data)
    a = a**2
    squared_list.append(a)

for i in squared_list:
    sum += i

result = sum / (len(data)-1)

std_dev = math.sqrt(result)
print(f"The standard deviation is {std_dev}")
