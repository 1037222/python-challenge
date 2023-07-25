#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes 
#and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

# Set the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables to store election analysis data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read in the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Update the total number of votes
        total_votes += 1

        # Update the candidates dictionary with their respective vote counts
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Check if the current candidate has the most votes so far
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]

# Prepare the election analysis summary
summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, votes in candidates.items():
    percent_votes = round((votes / total_votes) * 100, 3)
    summary += f"{candidate}: {percent_votes:.3f}% ({votes})\n"
summary += f"-------------------------\n"
summary += f"Winner: {winner}\n"
summary += f"-------------------------\n"

# Print the election analysis to the terminal
print(summary)

# Export the election analysis summary to a text file
output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write(summary)






