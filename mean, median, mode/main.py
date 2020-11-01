import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)


def calcMean(file_data):
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

    length = len(new_data)
    sum = 0
    for x in new_data:
        sum += x
    mean = sum / length
    return mean


def calcMedian(file_data):
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(n_num)

    n = len(new_data)

    new_data.sort()

    if n % 2 == 0:
        med_1 = float(new_data[n//2])
        med_2 = float(new_data[n//2 + 1])
        median = (med_1 + med_2) / 2

    else:
        median = new_data[n//2]

    return median


def calcMode(file_data):
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(n_num)

    data = Counter(new_data)

    mode_data_for_range = {
        "50-60": 0,
        "60-70": 0,
        "70-80": 0,
    }

    for height, occurence in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"] += occurence
        elif 60 < float(height) < 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 < float(height) < 80:
            mode_data_for_range["70-80"] += occurence

    mode_range, mode_occurance = 0, 0

    for range_data, occurence in mode_data_for_range.items():
        if occurence > mode_occurance:
            mode_range, mode_occurance = [
                int(range_data.split("-")[0]), int(range_data.split("-")[1])], occurence

    mode = float((mode_range[0] + mode_range[1]) / 2)
    return mode


mean = calcMean(file_data)
median = calcMedian(file_data)
mode = calcMode(file_data)

print("The mean is: " + str(mean))
print("The median is: " + str(median))
print("The mode is: " + str(mode))
