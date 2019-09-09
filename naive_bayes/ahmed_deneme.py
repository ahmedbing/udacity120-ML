#!/usr/bin/python

from time import time
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import sys
sys.path.append("../tools/")


""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###


#########################################################

clf = GaussianNB()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

accuracy = accuracy_score(labels_test, pred)

print("Accuracy score is ", accuracy)
