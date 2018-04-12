#This is k-mean algoritm #
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Spark:K-Means Clustering")
sc = SparkContext(conf = conf)
rawData = sc.textFile("/path/Wholesale.csv")
rawData.persist()
rawData.count()
rawData.take(4)
parsedData = rawData.map (lambda 
line: array([int(x) for x in line.split(",")]))
dataWithIdex = parsedData.zipWithIndex().map(lambda (k,v):(v,k))
test= dataWithIdex.sample(False, 0.2, 42)
training = dataWithIdex.subtractByKey(test)
testData = test.values().cache()
trainingData = training.values().cache()
testData.count()
trainingData.count()
k = 8
maxIterations = 30 
clusters = KMeans.train(trainingData,k,maxIterations,initializationMode="k-means||", seed = 50) 
cluster = clusters.clusterCenters
cluster = array (clusters.clusterCenters, dtype = int)
print "Cluster Number: %d" %len(cluster)
print "Cluster Centers Information Overview:"
for i in range(len(cluster)):
    print "Center Point of Cluster " + str(i) +": "+ str(cluster[i]) 
for dataLine in testData.collect():
   index = clusters.predict(dataLine)
   print "The data "+ str (dataLine) + " belongs to cluster "+ str(index)
wcss_train = clusters.computeCost(trainingData)
wcss = clusters.computeCost(testData)
print "Clustering score for k=%d is %0.2f for training dataset, %0.2f for testing dataset" %(k, wcss_train, wcss)

# **choose the best k **#
# ks= [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for k in ks:
#  model = KMeans.train(trainingData, k, 30)
#  ssd = model.computeCost(trainingData)
#  print "Sum of squared distances of points to their nearest center when k=%d -> %0.2f"  %(k , ssd) 
