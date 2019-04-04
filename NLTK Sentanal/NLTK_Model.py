import os
import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import EnglishStemmer

from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

"""
This is a sentiment analyses model using the NLTK classifier

Authors: Luis Hernandez, Jordan Jefferson, Matthew Layne
"""

trainFile = open('.\\Data\\jsonFiles\\train.json') 
testFile = open('.\\Data\\jsonFiles\\test.json') 

trainArticlesJson = json.load(trainFile)
testArticlesJson = json.load(testFile)

trainReal = []
trainFake = []

testReal = []
testFake = []

for article in trainArticlesJson:
	if article['label'] == 'pos':
		trainReal.append(article['text'])
	else:
		trainFake.append(article['text'])

for article in testArticlesJson:
	if article['label'] == 'pos':
		testReal.append(article['text'])
	else:
		testFake.append(article['text'])



print("Length of real training set: {0}".format(len(trainReal)))
print("Length of real test set: {0}".format(len(testReal)))
print("Length of fake training set: {0}".format(len(trainFake)))
print("Length of fake test set: {0}".format(len(testFake)))



