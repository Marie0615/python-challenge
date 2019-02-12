import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Create the variable (lists) to store the information requested
CandidatesList=[]
CountVotes=[]
TotalCandidates=[]
UniqueCandidates=[]
VotesList=[]

# Read using CSV module
with open(csvpath, newline='', encoding="utf8") as election_data:
  csvreader = csv.reader(election_data, delimiter=',')

  # Remove the header so we will only work with values
  header = next(csvreader)

   # Loop to obtain the VotesList and the and the TotalCandidates
  for row in csvreader:
      # Calculate the length of the VotesLists
      VotesList.append(row[0])
      length = str(len(VotesList))

      # Create the List of all candidates
      TotalCandidates.append(row[2])

  # Identify unique candidates,
  
  for i in TotalCandidates:
      if i not in UniqueCandidates:
          UniqueCandidates.append(i)

  # Obtain total count of each candidates
  
  CandidateListTotalCount = [[x,TotalCandidates.count(x)] for x in set(TotalCandidates)]

  # Create a dictionary with the comprehension list
  SummaryTotalCandidates = dict((x,TotalCandidates.count(x)) for x in set(TotalCandidates))

  # Obtain keys value from the dictionary
  for key in SummaryTotalCandidates:
      keys = key
  for value in SummaryTotalCandidates.items():
      values = value

  # To obtain the winner we need to know the one that recevied more votes
  # Create a list of candidates and another for the votes. We will use the index of the maximum value in the votes list so we can apply this in the candidates list to know the winner's name
  for row in CandidateListTotalCount:
     CandidatesList.append(row[0])
     CountVotes.append(int(row[1]))

  # Obtain the max value of the list of votes.
  MaxValue = max(CountVotes)
  MaxValueIndex = CountVotes.index(MaxValue)
  Top = CandidatesList[MaxValueIndex]
print(" ")
print("Election Results")
print("-----------------------")
print(f"Total votes: {length}")
print("-----------------------")

for key, value in SummaryTotalCandidates.items():
  print(f"{key}: {round((int(value)/int(length))*100),3}% ({value})")
print("-----------------------")
print(f"Winner: {Top}")