from pyspark import SparkContext, SparkConf
import numpy as np
import time
#============
#Add any extra imports here
#============

with open("/root/spark-ec2/cluster-url", "r") as myfile:
	master=myfile.readline().strip()

def parseLine(line):
    fields = line.split(',')
    converted_field = map(float, fields[1:])
    converted_field.append(float(1))
    year = int(fields[0])
    result_vector = np.dot(year, converted_field)
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

times=[]
for i in range(1,9):

	conf = (SparkConf().set("spark.cores.max", i))

	sc = SparkContext(master, "ec2_run_me", conf=conf)
	sc.setLogLevel("ERROR")

	start=time.time()

	rdd_train = sc.textFile("/songs/train_data.txt")
	rdd_test = sc.textFile("/songs/test_data.txt")

	#==================================
	#Start of your linear regression code
	#==================================

	# Part 2: a
	rdd_2 = rdd_train.map(parseLine)
	print rdd_2.sum()

	# Part 2:b
	rdd_3 = rdd_train.map(transMatrix)
	print rdd_3.sum()

	# Part 2:c
	inverse = np.linalg.inv(rdd_3.sum())
	w = np.dot(inverse, rdd_2.sum())
	print type(w), "weight", w

	# Part 2:d
	x_test = rdd_test.map(prediction)
	y_pred = np.dot(x_test.collect(), w.T)
	print "y_pred = ", y_pred

	# Part 2:e
	y_real = rdd_test.map(lambda x: int(x.split(',')[0]))
	MSE = abs(np.subtract(y_real.collect(), y_pred)).sum() / y_real.count()
	print "MSE = ", MSE


	#==================================
    #End of your linear regression code 
    #==================================

	times.append([i,time.time()-start])

	print times

	sc.stop()






