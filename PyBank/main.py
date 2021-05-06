# Import os and import csv
import os
import csv

# Open the file 
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:

    # Creating a variable to split up the file
    readingthefile = csv.reader(csvfile, delimiter=',')

print(readingthefile)