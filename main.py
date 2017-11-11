import os
import csv
totalVote = 0
candidateList = []
candidateCount = {}
prevCand = 0
result = 0
# Open budget_data_1.cs\
with open("raw_data\\election_data_2.csv", 'r') as election:
    csvReader =csv.DictReader(election)
    for row in csvReader:
        totalVote += 1
        if row ["Candidate"] not in candidateList:
            candidateList.append(row["Candidate"])
            candidateCount[row["Candidate"]] = 1
        elif row ["Candidate"] in candidateList:
            candidateCount[row["Candidate"]] += 1
print("Election Results")
print("--------------------------")
print("Total Votes: ", totalVote)
print("--------------------------")
for key, value in candidateCount.items():
    result = float((value/totalVote) * 100)
    print(key, ": ", round(result, 1), "%   (", value, ")")
for key, value in candidateCount.items():
    if value > prevCand:
        mostVote = key
        prevCand = value
print("--------------------------")
print("Winner: ", mostVote)
print("--------------------------")
	