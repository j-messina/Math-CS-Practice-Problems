import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()
#--------------------------------------
# Step 0: Define some variables
# Step 1: Proof of concept - Identify a single repeating decimal
# Step 2: Proof of concept - Identify a double repeating decimal
# Step 3: Implement detection for any length repeating decimal
# Step 4: Run the any-length function to find answer
#
# Note: Initial testing determined that using the decimal package was necessary for better precision
#--------------------------------------

# Step 0: Define some variables
best_denom = 7
num_range_end = 1000

# Step 1: Proof of concept - Identify a single repeating decimal
def is_Single_Repeating(num):
    num_as_str = str(num)
    for index in range(0, len(num_as_str) - 2):
        innerdex = index + 1
        while num_as_str[index] == num_as_str[innerdex]:
            innerdex+=1
            if innerdex == len(num_as_str)-1:
                return True
    return False

# Step 2: Proof of concept - Identify a double repeating decimal
def is_Single_Or_Double_Repeating(num):
    num_as_str = str(num)
    for index in range(0, len(num_as_str) - 4):
        first_innerdex = index+2
        second_innerdex = index+3
        while num_as_str[index] == num_as_str[first_innerdex] and num_as_str[index+1] == num_as_str[second_innerdex]: 
            first_innerdex+=2
            second_innerdex+=2
            if first_innerdex >= len(num_as_str) - 2 or second_innerdex >= len(num_as_str)-1:
                return True
    return False

# Step 3: Implement detection for any length repeating decimal
# take "next" given value in sequence - MARK
        #  end limit is len - 7
    # proceed through rest of sequence
    # when same value is found - SECOND MARK
        # the distance between the two now denotes the potential repetition distance
        # in tandem, check if sequence of values after first mark matches sequence after second mark
        # if success, then return sequence length as confirmation of True
        # if fail, then return 0 as confirmation of False              

def IAR2(num):
    num_as_str = str(num)
    numlen = len(num_as_str)
    for index in range(2, numlen - 7): # this sets the possible starting point of the pattern
        starting_val = num_as_str[index]
        for innerdex in range(index+1, numlen - 5): # this sets the location of next "mark" in the pattern, if there is one
            potential_same_val = num_as_str[innerdex]
            if starting_val == potential_same_val:
                dig_place_distance = innerdex - index
                matching_in_between = True
                for next_mark in range(innerdex, numlen-1, dig_place_distance): # this checks all of the remaining marks in the pattern, as well as that the values between them are consistent
                    next_mark_val = num_as_str[next_mark]
                    if starting_val != num_as_str[next_mark]: # all marks match
                        matching_in_between = False
                        break
                    for offset in range(1, dig_place_distance): # check values between marks match
                        try:
                            if num_as_str[index+offset] != num_as_str[next_mark+offset]:
                                matching_in_between = False
                                break
                        except IndexError:
                            pass
                    if not matching_in_between:
                        break
                else:
                    return dig_place_distance   
    return 0

# Step 4: Run the any-length function to find answer
import decimal
from decimal import Decimal
decimal.getcontext().prec=000
best_pattern_length = 0
best_length_num = 1

for x in range(1,1000):
    result = IAR2(Decimal(1)/Decimal(x))
    if result > best_pattern_length:
        best_pattern_length = result
        best_length_num = x
    print("For 1/{}: ".format(x), end='')
    if result>0:
        print("Repeating decimal of length {} -- {}".format(result,1/x))
    else:
        print("Non-repeating")
print()
print("The longest length from the set found was", best_pattern_length, "from 1/{}".format(best_length_num))