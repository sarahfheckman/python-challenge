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

#-----------------------------------------------2nd commit
#create percentages
li_percentage = round(((li_vote/total_voters) * 100), 3)
otooley_percentage = round(((otooley_vote/total_voters) * 100), 3)
khan_percentage = round(((khan_vote/total_voters) * 100), 3)
correy_percentage = round(((correy_vote/total_voters) * 100), 3)

#create function to consolidate results
def election_results(candidate, percent, total):
    statement = f"{candidate}: {percent}% ({total})"
    print(statement)

#printing everything
print("ELECTION RESULTS")
print("----------------------")
print("Total Votes: " + str(total_voters))
print("----------------------")
election_results("Khan", khan_percentage, khan_vote)
election_results("Correy", correy_percentage, correy_vote)
election_results("Li", li_percentage, li_vote)
election_results("O'Tooley", otooley_percentage, otooley_vote)
print("----------------------")
print("Winner: Khan")
print("----------------------")