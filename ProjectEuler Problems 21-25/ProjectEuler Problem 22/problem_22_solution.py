import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

# Step 1: Load the file
# Step 2: Sort list alphabetically
# Step 3: Calculate alphabetical value for each name, and store it
# Step 4: Multiply name's alphabetical value by its location in the sorted list to get its name score
# Step 5: Sum all of the name scores
# ----------------------------------

# Step 0: Change to the proper directory (because VS Code and Python don't play well together)
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir) # Change the working directory to the script's directory

# Step 1: Load the file
filename = "names.txt"
with open(filename, 'r') as file:
    raw_text = file.read().strip().replace('"','') #strip removes whitespace, then replace gets rid of quote marks

list_of_names = raw_text.split(",") # splits text into list of words, using , as a delimiter

# Step 2: Sort List Alphabetically
list_of_names.sort()

# Step 3: Calculate Alphabetical Value for each name, and store it
for name_index in range(0, len(list_of_names)):
    total_alphab_value = 0
    for letter in list_of_names[name_index]:
        total_alphab_value += ord(letter) - 64
    list_of_names[name_index] = [list_of_names[name_index], total_alphab_value]

# Use this to print out some entries of the list to check
# for x in range(10):
#     print(list_of_names[x])
    
# Step 4: Multiply name's alphabetical value by its location in the sorted list to get its name score
name_scores = []
for name_index in range(0, len(list_of_names)):
    total_alphab_value = list_of_names[name_index][1]
    name_scores.append(total_alphab_value * (name_index+1))

# Step 5: Sum all of the name scores
sum_of_name_scores = 0
for score in name_scores:
    sum_of_name_scores += score

print("Total name score is ", sum_of_name_scores)