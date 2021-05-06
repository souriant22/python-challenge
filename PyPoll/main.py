# import os and libr
import os
import csv

# create paths to files 
input_file = os.path.join('./Resources','election_data.csv')
output_file = os.path.join('./Analysis','election_results.txt')
print(input_file)

# declare global variables
vote_total = 0
candidate_vote = {}
candidate_list = []
winner = ''
winner_vote = 0
perc_winner = 0

# with statement to open the files
with open(input_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)


# for loop all of the processing inside the for loop
    for row in reader:
        vote_total += 1

        # Remaining calculations

print(f'The total votes {vote_total}')