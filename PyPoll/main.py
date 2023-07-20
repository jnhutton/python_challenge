import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

candidate = []
unique_candidate = []
vote_count = []
vote_percentage = []

count = 0

# Open the CSV using the set path 
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1

        candidate.append(row[2])
    # x = counts amount of unique candidates
    for x in set(candidate):
        unique_candidate.append(x)
        # y = amount of votes each candidate receives
        y = candidate.count(x)
        vote_count.append(y)
        # z = percentage of votes that each candidate receives
        z = (y/count) * 100
        vote_percentage.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print out results
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Create a txt file 
import sys
file = open('analysis', 'w')
sys.stdout = file

print("Election Results\n")   
print("-------------------------\n")
print("Total Votes :" + str(count) + "\n")    
print("-------------------------\n")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")\n")
print("-------------------------\n")
print("The winner is: " + winner + "\n")
print("-------------------------")

file.close()