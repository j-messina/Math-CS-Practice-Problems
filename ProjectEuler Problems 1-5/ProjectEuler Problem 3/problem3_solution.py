# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Steps:
# 1) Make/borrow a function for checking if the value is prime
#       - approach 1: make it myself -->
#       - approach 2: find and use some already built method for finding if a number is prime
# 2) Use that function to find largest prime factor
#       - approach 1: increments starting at 3, if value divides evenly (check using modulus operator)
#         then check if its factor pair partner is prime --> first that does is returned
#       - approach 2: decrements from product/3 rounded down, checks if number is prime
#         --> if so, return it