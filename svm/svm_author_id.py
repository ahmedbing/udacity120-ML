
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
import sys
from time import time
sys.path.append("../tools/")
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

########################################################)
clf = SVC(gamma= 'auto', C = 10000 ,kernel ='rbf')
#features_train = features_train[:round(len(features_train)/2)]
#labels_train = labels_train[:round(len(labels_train)/2)]

#clf = LinearSVC(random_state=0, tol=1e-7)
t0 = time()
clf.fit(features_train, labels_train)
print("Train time", round(time()-t0,3))
t1 = time()
pred = clf.predict(features_test)
number = 0 
for x in pred:
	if x == 1:
		number += 1
	else:
		continue
print ("Pred number " , number)
#accuracy = accuracy_score(labels_test, pred)
#print("Accuracy score is ", accuracy)
