# Election Analysis

## Overview of Election Audit
In this project, we will be assisting a Colorado board of elections employee, Tom, in an election audit of tabulated results. We will go through the provided csv file and perform read and write functions with additional decision statements and logical operations in order to conclude the desired results.

## The purpose of this election analysis audit.
The main purpose of this project is to figure out:
- The total number of the votes in the election.
- Each Candidate's total votes and percentage of votes.
- The winner of the election, winning vote count, and winning percentage of votes 
- Each county and its total vote count.
- Each county and its percentage of the total votes.
- The county with the largest number of voters is printed to the terminal.
- writing the winning candidate results and the county election results to the election_results.txt text file.

# Election Audit Results:

 ## How many votes were cast in this congressional election?
- There were total of <b>369,711<b/> votes were cast in the election.

 ## Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
County Votes:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

 ## Which county had the largest number of votes?
- Largest County Turnout: Denver

 ## Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)


 ## Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

<b>In Conclusion, In the election total of 369,711 votes were cast. County Denver received the largest number of the votes( 306,055) and the candidate Diana DeGette    won the election with 272,892 number of the total votes.</b>


 ## The county with the largest number of voters is saved in the election_results.txt file.
 
![Test Image](/Resources/Election_Analysis.png)

 ## County Code 

     4a) Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b) Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c) Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5) Add a vote to that county's vote count.
        county_votes[county_name] += 1

    # 6a)  Write a repetition statement to get the county from the county dictionary.
    for county in county_list:

        # 6b) Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
        county_vote = county_votes.get(county)

        # 6c) Calculate the percent of total votes for the county.
        county_vote_percentage = float(county_vote) / float(total_votes) * 100

        # 6d) Print the county results to the terminal.
        county_results = f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n"

        # Print the counties to test.
        print(county_results)

        # 6e) Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f) Write a decision statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_turnout_count) and (
            county_vote_percentage > largest_county_percentage
        ):
            # True
            largest_county_turnout_count = county_vote
            largest_county_percentage = county_vote_percentage
            largest_county_turnout = county
            
 ## Candidate Code
    if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)



# Election Audit Summary

## Give at least two examples of how this script can be modified to be used for other elections.
- This script will be used to audit not only other congressional districts, but also senatorial districts and local elections.
- We can use crypto function such as encrypt or decrypt methods to protect the security of digital voting systems. Malwares can disrupt the regular voting procedure   and slow or completely shut down the entire system. In order to protect the systems from such malicious attacks cyber security is high priority for the election     administrators.
- We can perform Parallel testing, this process will identify any concerns related to the voting system which hinders or disrupts the elections.
