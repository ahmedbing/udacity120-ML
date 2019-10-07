#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(
    open("../final_project/final_project_dataset.pkl", "rb"))

paym = 0
poi_say = 0

for ind, people in enumerate(enron_data):
    num = enron_data[people]['total_payments']
    poinum = enron_data[people]['poi']
    if poinum == True:
        poi_say += 1
    if num == 'NaN':
        paym = paym+1
print("Paym Number  ", paym, " Index ", ind, " Poi Sayısı", poi_say)
