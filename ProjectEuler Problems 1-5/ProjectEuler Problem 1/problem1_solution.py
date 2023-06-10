# Project 1 Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sumOfMultiples = 0  # This will be our variable for adding all of the multiples together
for num in range(1,1000): # note that when using range(x,y) it will go from the range of x to y-1; y will not be counted
    if(num % 3 == 0 or num % 5 == 0): # it is easy to forget that "or" is the logical operator in Python
        sumOfMultiples += num # the += operator takes the inital value of the left, adds it to the right, and then stores in left
print("The sum of all multiples of 3 or 5 below 1000 is", sumOfMultiples) # note the print operation default separates with a " "
