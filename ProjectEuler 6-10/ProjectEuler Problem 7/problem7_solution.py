# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import sys
sys.path.append("../..")
from Algorithms.isPrime import *

counter = 1
nextOddNum = 3
while(counter < 10001):
    if(isPrime(nextOddNum)):
        counter += 1
    nextOddNum += 2
the_10001st_prime = nextOddNum - 2 # have to do this to compensate for extra += 2 on last iteration of while loop

print("The 10001st prime is", the_10001st_prime)
