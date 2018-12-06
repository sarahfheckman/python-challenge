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
pull_candidates = set(candidates)
print(pull_candidates)
#--------------------------------------1st commit 

#set voter variables
total_voters = len(voters)
print(total_voters)

#set candidate vote amounts
li_vote = 0
otooley_vote = 0
khan_vote = 0
correy_vote = 0

#run loop to determine number of votes
for candidate in candidates:
    if candidate == "Li":
        li_vote = li_vote + 1
    elif candidate == "O'Tooley":
        otooley_vote = otooley_vote + 1
    elif candidate == "Khan":
        khan_vote = khan_vote + 1
    elif candidate == "Correy":
        correy_vote = correy_vote + 1

print(li_vote)
print(otooley_vote)
print(khan_vote)
print(correy_vote)


