import csv
import random
import math
import operator

##########======KNN=======#####################################################
"""
    load dataset from csv file, randomly split into training and test set
"""
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
"""
    calculate Euclidean Distance to:
        locate the k most similar data instances in the training dataset
        for a given member of the test dataset
    
""" 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

"""
    get Neighbors:
        returns k most similar neighbors from the training set for a given test instance 
        (using the already defined euclideanDistance function)
"""  
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

"""
    get Response:
        Once we have located the most similar neighbors for a test instance,
        then we need to devise a predicted response based on those neighbors.
        This function is to get the majority voted response from a number of neighbors
"""  
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

"""
    getAccuracy:
        sums the total correct predictions and 
        returns the accuracy as a percentage of correct classifications
"""
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

#############========IMPLEMENTATION========#######################################

filename = '/Users/lilyle/Desktop/dataKNN.csv'
trainingSet=[]
testSet=[]
# Set split rate (0< split rate < 1)
split = 0.85
loadDataset(filename, split, trainingSet, testSet)
print ('Train set: ' + repr(len(trainingSet)))
print ('Test set: ' + repr(len(testSet)))

# generate predictions
predictions=[]
k = 3
for x in range(len(testSet)):
	neighbors = getNeighbors(trainingSet, testSet[x], k)
	result = getResponse(neighbors)
	predictions.append(result)
	print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')

