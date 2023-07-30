# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import sys
sys.path.append("../..")
from Algorithms.isPrime import *

sum = 2
for x in range(3,2000000, 2):
    if x % 5**6 == 0:
        print("sum {}, x ~ {}".format(sum, x))
    if isPrime(x):
        sum += x

print("Sum of all primes below 2,000,000 =", sum)