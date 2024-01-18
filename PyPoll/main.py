## PyPoll

# Importing dependencies

import os
import csv

# Setting file path

election_csv = os.path.join(".", "Resources", "election_data.csv")

# Opening and reading csv file

with open(election_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    # Reading and storing the header row first
    
    csv_header = next(csv_file)
    
    # Setting requisite variables
    
    total_votes = 0
    candidate = None
    candidates = []
    votes_per_candidate = []
    percent_per_candidate = []
    
    # (For use of "None" see https://stackoverflow.com/questions/664294/is-it-possible-only-to-declare-a-variable-without-assigning-any-value-in-python)
    
    # Reading through each row of the csv file, increasing the total number of votes, and storing the candidate's name
    
    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        
        # If we already have the candidate in our list, we simply want to increase the number of votes they received
        
        if candidate in candidates:
            i = candidates.index(candidate)
            votes_per_candidate[i] = votes_per_candidate[i] + 1
        
        # If we don't already have the candidate in our list, we need to add them to the list, then add a place to start counting votes for that candidate in a separate list
        
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate.append(1)
            
        # ("if a in b" syntax first seen here https://stackoverflow.com/questions/14515274/how-to-check-if-a-string-is-in-a-list-of-strings)

# Calculating the percent of the votes each candidate received and appending the appropriate list with the value
                
for j in range(len(votes_per_candidate)):
    percent = str(round(100 * votes_per_candidate[j] / total_votes, 3)) + "%"
    percent_per_candidate.append(percent)

# Finding the winner based on the greatest number of votes received
    
for k in range(len(votes_per_candidate)-1):
    
    if votes_per_candidate[k + 1] > votes_per_candidate[k]:
        winner = candidates[k + 1]
        
    else:
        winner = candidates[k]

# Printing the desired results to the terminal
    
print(
      "Election Results", "\n", "\n",
      "----------------------------", "\n", "\n",
      "Total Votes: " + str(total_votes), "\n", "\n",
      "----------------------------", "\n", "\n",
      )

for l in range(len(candidates)):
    print(f"{candidates[l]}: {percent_per_candidate[l]} ({votes_per_candidate[l]})", "\n", "\n")

print(
      "----------------------------", "\n", "\n",
      "Winner: " + winner, "\n", "\n",
      "----------------------------"
      )

# (For line break info, see https://stackoverflow.com/questions/5982206/how-to-print-a-linebreak-in-a-python-function)

# Setting the variable and path for the output file

output_path = os.path.join(".", "analysis", "election_data_analysis.txt")

# Opening the output file

with open(output_path, "w") as output_file:
    
    # Writing the rows of the output file (see https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python)
    
    output_file.write("Election Results""\n""\n")
    output_file.write("----------------------------""\n""\n")
    output_file.write(f"Total Votes: {total_votes}""\n""\n")
    output_file.write("----------------------------""\n""\n")
    for m in range(len(candidates)):
        output_file.write(f"{candidates[m]}: {percent_per_candidate[m]} ({votes_per_candidate[m]})""\n""\n")
    output_file.write("----------------------------""\n""\n")
    output_file.write(f"Winner: {winner}""\n""\n")
    output_file.write("----------------------------")