from pyspark import SparkContext
import numpy as np

#============
#Add any extra imports here
#============
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from math import *
#==================================
#Start of your code
#==================================

def parseLine(line):
    fields = line.split(',')
    converted_field = map(float, fields[1:])
    converted_field.append(float(1))
    transposed_vector = np.array(converted_field)
    year = int(fields[0])
    result_vector = np.dot(transposed_vector.T, year)
    return result_vector

def transMatrix(line):
    fields = line.split(',')
    converted_field = map(float, fields[1:])
    converted_field.append(float(1))
    transposed_vector = np.array(converted_field)
    result_multiplier = np.outer(transposed_vector.T, transposed_vector)
    return result_multiplier

def prediction(line):
    fields = line.split(',')
    converted_field = map(float, fields[1:])
    converted_field.append(float(1))
    transposed_vector = np.array(converted_field)
    return transposed_vector

sc = SparkContext("local", "local_run_me")
sc.setLogLevel("ERROR")

rdd_train = sc.textFile("/home/ravi/Documents/Machine_Learning_Lectures/Homework/Hw3/Data/Songs/train_data.txt")
rdd_test = sc.textFile("/home/ravi/Documents/Machine_Learning_Lectures/Homework/Hw3/Data/Songs/test_data.txt")

rdd = rdd_train.map(lambda x: int(x.split(',')[0]))

#Part 1: a
count = rdd.count()
print("Part 1(a): number of data cases in train dataset", count)

#Part 1: b
mean = rdd_train.map(lambda x: float(x.split(',')[0])).reduce(lambda x, y: x + y)/rdd.count()
print("Part 1(b): average_year = ", mean)

stdev = sqrt(rdd_train.map(lambda x: (int(x.split(',')[0]) - mean)*(int(x.split(',')[0]) - mean)).reduce(lambda x, y: x+y)/count)
print("Part 1(c): stdev = ", stdev)

result = rdd.countByValue()
year_distribution = rdd.map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y).sortByKey().collect()

num_songs_per_year = []
years = []

for key, value in year_distribution:
    num_songs_per_year.append(value)
    years.append(key) 
    print("%s %i" % (key, value))

print("years", len(years))

y_pos = np.arange(len(years))

#Part 1: d
plt.bar(y_pos, num_songs_per_year, align='edge', alpha=0.1)
plt.xticks(y_pos, years, rotation = 'vertical', size = 8)
plt.ylabel('Number of Songs in Year')
plt.title('Song Yearwise Distribution')
plt.savefig("Song_Distribution.pdf")

#Part 1: e
inner_product = rdd_train.map(lambda x: float(x.split(',')[1]) * float(x.split(',')[2])).reduce(lambda x, y: x+y)
print "Part 1(e): inner product", inner_product

#Part 2: a
rdd_2 = rdd_train.map(parseLine).reduce(lambda x, y: x + y)
print "Part 2(a): ", rdd_2

#Part 2:b
rdd_3 = rdd_train.map(transMatrix).reduce(lambda x, y: x + y)
print "Part 2(b): ", rdd_3

#Part 2:c
inverse = np.linalg.inv(rdd_3)
w = np.dot(inverse, rdd_2)
print "Part 2(c): weight", w

#Part 2:d
x_test = rdd_test.map(prediction).collect()
y_pred = np.dot(x_test, w.T)
print "Part 2(d): y_pred = ", y_pred

#Part 2:e
y_real = rdd_test.map(lambda x: int(x.split(',')[0]))
MAE = abs(np.subtract(y_real.collect(), y_pred)).sum()/y_real.count()
print "Part 2(e): MAE = ", MAE

#Part 3(b):
time_to_execute = [190.16260886192322, 99.202215909957886, 70.583625078201294, 57.576313972473145,
                   56.298246145248413, 45.088545083999634, 44.452743053436279, 43.938822984695435]

plt.plot(np.arange(1, 9), time_to_execute)
plt.axis([0, 10, 0, 200])
plt.xticks(np.arange(1,9), np.arange(1, 9))
plt.xlabel('Number of workers')
plt.ylabel("Execution Time (in seconds)")
plt.title('Number of Worker vs Execution Time')
plt.savefig("Time_Distribution.pdf")
