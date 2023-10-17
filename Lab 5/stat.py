import statistics
import time

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = []

for grade in data.split(','):
    grades.append(int(grade))

minimum = min(grades)
print("Minimum grade:", minimum)
maximum = max(grades)
time.sleep(0.5)
print("Maximum grade:", maximum)

average = sum(grades) / len(grades)
average = round(average, 2)
time.sleep(0.5)
print("Average grade: ", average)

mean = round(statistics.mean(grades), 2)
time.sleep(0.5)
print("Mean grade: {}".format(mean))

median = statistics.median(grades)
time.sleep(0.5)
print("Median grade: {}".format(median))


minimum = min(grades)
maximum = max(grades)
average = sum(grades) / len(grades)
mean = statistics.mean(grades)
median = statistics.median(grades)

output = "Minimum grade: {}\nMaximum grade: {}\nAverage grade: {}\nMean grade: {}\nMedian grade: {}"
time.sleep(0.5)
print(output.format(minimum, maximum, average, mean, median))