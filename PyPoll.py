# Import csv  and os module
import csv
from importlib.resources import open_binary
import os
from turtle import clear


#Assign a variable to load a file from a path.
file_to_load = os.path.join(r"C:\Users\kusha\Desktop\Elections_Project\Resources\election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize the variable total_votes =0
total_votes=0

#Declare Candidate_options
candidate_options=[]

#Declare empty dictionary
candidate_votes={}

# Declare Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

#Read  the header row.
    headers= next(file_reader)

# Print each row in the CSV file
    for row in file_reader:

       # Add to the total vote count.
       total_votes += 1

# 1. Print the total number of votes cast

    #print(total_votes)

# 2. A complete list of candidates who received votes
       candidate_name = row[2]

    
    
       #If the candidate does not match any existing candidate...
       if candidate_name not in candidate_options:

        # Add to the list
        candidate_options.append(candidate_name)

#print(total_votes)
#print(candidate_options)

# 4. The total number of votes each candidate won
        candidate_votes[candidate_name]=0

# Add a vote to that candidate's account
       candidate_votes[candidate_name]+=1

# Print the candidate vote dictionary
#print(candidate_votes)        

# 3. The percentage of votes each candidate won

# Iterate through  the candidate list.
for candidate_name in candidate_votes:

    #  Retrieve vote count of a candidate
    votes= candidate_votes[candidate_name]

    # Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100

          #print(f"{candidate_name}:received {vote_percentage}% of the vote.")   

# 5. The winner of the election based on popular vote.

    if (votes > winning_count) and (vote_percentage> winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")   

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    



