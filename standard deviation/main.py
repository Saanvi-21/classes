import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

sum = 0
all_elements = []

for data in file_data:
    elements = len(data)
    for i in data:
        all_elements.append(i)
        sum += float(i)

mean = sum / elements

squared_sum = 0
for element in all_elements:
    squared_sum = squared_sum + \
        ((float(mean) - float(element)) * (float(mean) - float(element)))

squared_sum = squared_sum / len(all_elements)
final_result = math.sqrt(float(squared_sum))
print(final_result)
