# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

# import isPrime method
import sys
sys.path.append("../..")
from Algorithms.isPrime import *

# So to be honest, this is more of a math problem than a programming one
# Even so, I will write out my thinking here and use Python code where appropriate

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# below is the above list of numbers decomposed into all their prime factors
# 1 2 3 2 2 5 2 3 7 2 2 2 3 3 2 5 11 2 2 3 13 2 7 3 5 2 2 2 2 17 2 3 3 19 2 2 5
#   need four 2's to cover all the even numbers
#   need two 3's to cover 3,6,9,12,18
#   need one 5 to cover 5, 10, 15, 20
#   need to include other primes: 19, 17, 13, 11, 7
#   results with: 16 * 9 * 5 * 19 * 17 * 13 * 11 * 7
# smallestProduct = 16 * 9 * 5 * 19 * 17 * 13 * 11 * 7
# for x in range(2,21):
#     if smallestProduct % x != 0:
#         print("Not correct at", x)
#
# print("Smallest product is:", smallestProduct)

#----------------------------------------------------------------------------------------------------

# For a more general solution, we could use the range to check each number for if it is prime
# We can also develop a dictionary for numbers counting up from 1, tracking whether each of them is prime or not
# From the largest numbers we can select their factors and filter them from the list, adding only the remaining unique factors

numberOf2s = 0
num = int(input("Enter a number: "))

print("Calculating smallest positive number evenly divisible by all integers from 1 to {}...".format(num))

finalProduct = 1
commonNumsChecklist = [2,3,5]
counter = 0

for x in commonNumsChecklist:
    counter = 0
    temp = num
    while temp >= x:
        finalProduct *= x
        counter += 1
        temp = int(temp/x)
    print("Found {} {}'s in {}".format(counter, x, num))


for x in range(7, num, 2):
    if (isPrime(x)):
        print(x,"is prime")
        finalProduct *= x

print("The smallest product of all integers from 1 to {} is {}".format(num, finalProduct))