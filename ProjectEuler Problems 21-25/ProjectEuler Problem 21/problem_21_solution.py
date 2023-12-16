# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors 
# of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# this print statement removes the python printing path segment that 
# always appears at the beginning of the output
print('\033c')

from math import sqrt

# this function takes an integer and returns the sum of its divisors
def SumOfDivisors(amicandidate):
    sum_of_divisors = 1
    root = sqrt(amicandidate)
    # find and sum together all of the divisors
    for num in range(2, int(root) + 1):
        if amicandidate % num == 0:
            # this part takes advantage of sets not allowing duplicates to account for square root divisors
            amicable_pair = {num, amicandidate/num} 
            for val in amicable_pair:
                 sum_of_divisors += val
    return sum_of_divisors

sum_of_amicable_nums = 0
for x in range(1, 10000):
    y = SumOfDivisors(x)
    if x == SumOfDivisors(y) and x != y:
        sum_of_amicable_nums += x
        print("Found amicable number pair: ", x, y)

print()
print("Sum of all amicable numbers under 10000 = ", sum_of_amicable_nums)