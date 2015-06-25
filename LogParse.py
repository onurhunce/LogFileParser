import sys
from sys import argv
import operator
from itertools import islice
import os

#read file, split into datas, return desired outputs
def log_parser(file):

	urlDict = {}
	with open(file) as f:
		temp_time = None
		temp_url = None
		size = os.path.getsize(file)	
		for element in islice(f,size):	
			temp = (element.split(" "))	
			if temp[-1:] > temp_time:
				temp_time = temp[-1:]
				time = ''.join(temp[-1:])[:-1]
				temp_url = temp[6]	

			if temp[6] in urlDict:	
				urlDict[temp[6]] +=1 
			else:
				urlDict[temp[6]] = 1	

	mostRequest = max(urlDict.iteritems(), key = operator.itemgetter(1))[0]		

	return len(urlDict.keys()), mostRequest, temp_url, time		


script,filename=argv
filename=sys.argv[1]
distinct, mostRequestUrl, biggestUrl, biggestTime = log_parser(filename)
print "Distinct url count: %s" %distinct
print "Most requested url: %s" %mostRequestUrl
print "Most time consuming url:%s time: %s" %(biggestUrl, biggestTime)

