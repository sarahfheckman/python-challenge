#import modules
import os
import csv

#create path
pypollCSV = os.path.join("C:/Users/sarah/Documents/BOOTCAMP/SMDA201811DATA2-master/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")


#set lists
voters = []
candidates = []

#open path & pull list values
with open(pypollCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    csv_header = next(csvfile)
    #add values to lists
    for column in csvreader:
        candidates.append(column[2])
        voters.append(column[0])

#pull unique candidates
candidates_set = set(candidates)
print(candidates_set)

#---------------------------------1st commit 

#set voter variables
total_voters = len(voters)
print(total_voters)

with open(pypollCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    csv_header = next(csvfile)
    #determines        
