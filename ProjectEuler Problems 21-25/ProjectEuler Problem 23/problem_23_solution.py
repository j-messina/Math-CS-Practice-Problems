# The below code statement is just for removing the annoying path printed out in the terminal output
# whenever the file is run
import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Step 0: Define variables and functions
# Step 1: Find all abundant numbers below 28123
# Step 2: Calculate all possible sums from given list of abundant numbers
# Step 3: Sum all numbers below 28123 excluded from Step 2

# ---------------------------------------
# Step 0: Define variables and functions
SMALLEST_ABUNDANT_NUMBER = 12
SOFT_UPPER_LIMIT = 28123 # HIGHEST_NONABUNDANT_SUM = ?

from math import sqrt
def DPA(num):
    root = int(sqrt(num))
    sum_of_divisors = 1
    factor_pair = {}
    # The following for loop checks from two up to the median point for factor pairs (the square root)
    # It then addes them to a set (to account for squares), and then adds all contents of the set
    # to the sum
    for x in range(2, int(root+1)):
        if num % x == 0:
            factor_pair = {x, num/x}
            for y in factor_pair:
                sum_of_divisors += y

    # at this point of the function, the sum of all the divisors should be acquired
    # The next step is to determine whether this sum is less than ("deficient"),
    # equal to ("perfect"), or greater than ("abundant") the original num
    if sum_of_divisors < num:
        return "Deficient"
    elif sum_of_divisors > num:
        return "Abundant"
    else: # sum_of_divisors == num
        return "Perfect"
    
# Step 1: Sort all numbers below 28123 into deficient, perfect, or abundant
deficient_numbers = []
perfect_numbers = []
abundant_numbers = []

for num in range(1, SOFT_UPPER_LIMIT):
    if DPA(num) == "Deficient":
        deficient_numbers.append(num)
    elif DPA(num) == "Abundant":
        abundant_numbers.append(num)
    else: # num is a perfect number
        perfect_numbers.append(num)

# Step 2: Calculate all possible sums from given list of abundant numbers
abundant_sums = set()
for num1 in range(0, len(abundant_numbers)):
    for num2 in range(0, len(abundant_numbers)):
        abundant_sums.add(abundant_numbers[num1]+abundant_numbers[num2])

# abundant_sums_list = list(abundant_sums)
# for x in range(10):
#     print(abundant_sums_list[x])

# Step 3: Sum all numbers below 28123 excluded from Step 2
sum_of_nonabundant_sums = 0
for num in range(1, 28124):
    if num not in abundant_sums:
        sum_of_nonabundant_sums += num

print("The sum of all numbers that are not possible sums of abundant numbers is: ", sum_of_nonabundant_sums)