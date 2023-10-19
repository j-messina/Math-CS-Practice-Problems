import math

# This problem unfortunately does not require much code, if any at all, because it is all mathematically solveable
# That being said, I will type here what I worked on paper

# Firstly, with a little research, a correlation between Lattice Paths and Pascal's Triangle becomes apparent
# Specifically, the total paths for a given grid of size n x n can be found in the middle of 2n'th row on Pascal's Triangle

# In this case, we are looking for the total paths for a 20 x 20 grid; therefore, our answer would be the middle value
# of the 40th row on Pascal's Triangle

# Moreover, note that the total number of elements on the given row in Pascal's Triangle is 1 more than its row number
# So, in this case, there are 41 elements on the 40th row of Pascal's Triangle, and we are looking for the one that is
# smack-dab right in the middle

# Moreover, the row-elements in Pascal's Triangle are counted like arrays in Python, where the first element is at index 0
# Therefore, while there are 41 elements in our target row, their indexes range from 0 to 40,
# and from there we can identify that the middle element would be at index 20

# So to recap, we can calculate the total number of paths of an n x n grid by the corresponding value in the middle
# of the 2n'th row on Pascal's triangle. In this case, we are looking for element 20 on row 40.
# Put another way, n = 40 and k = 20

# Now we implement the formula for calculating the value of on Pascal's Triangle, given its row and index
# That formula is the combination "n-choose-k", or in our case "40-choose-20"

# The formula for a combination "n choose k" equals:
#               n! / ( k! * (n-k)! )
# where the exclamation mark "!" represents the factorial of the number preceding it

# Plugging in our values of n = 40 and k = 20, we get:
#               40! / (20! * (20!)) == 40! / (20!)^2

# Now that we know what to plug in, we just need to make use of the factorial function from Python's Math library

from math import factorial

answer = factorial(40) / (factorial(20)**2)

print("The total paths of a 20x20 grid is", answer)