import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#               012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# --------------------------------
# Step 0: Import necessary libraries
# Step 1: Define function for step-by-step processing of target location
# Step 2: Run function and print results
# --------------------------------
# Step 0: Import necessary libraries
from math import factorial

# Step 1: Define function for step-by-step processing of target location
def find_nth_lexo_perm(list_of_digits, relative_location, result_list):
    the_factorial = factorial(len(list_of_digits)-1)
    current_index = 0
    while the_factorial*(current_index + 1) < relative_location:
        current_index += 1

    relative_location -= the_factorial*current_index
    result_list.append(list_of_digits[current_index])
    list_of_digits.pop(current_index)
    if len(list_of_digits) > 1:
        return find_nth_lexo_perm(list_of_digits, relative_location, result_list)
    else:
        result_list.append(list_of_digits[0])
        return result_list
    
# Step 2: Run function and print results
starting_list_of_digits = [0,1,2,3,4,5,6,7,8,9]
initial_location = 1000000
end_result_list = []

end_result_list = find_nth_lexo_perm(starting_list_of_digits, initial_location, end_result_list)
print(''.join(map(str,end_result_list)))
    