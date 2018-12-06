#import modules
import os
import csv

#create path
pypollCSV = os.path.join("C:/Users/sarah/Desktop/SMDA201811DATA2-master/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

#set lists
voters = []
candidates = []
votes1 = 0
votes2 = 0
votes3 = 0
votes4 = 0

#open path & pull list values
with open(pypollCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    csv_header = next(csvfile)
    #add values to list
    for column in csvreader:
        candidates.append(column[2])

#pull unique candidates
candidates_set = set(candidates)
print(candidates_set)

#---------------------------------1st commit        
