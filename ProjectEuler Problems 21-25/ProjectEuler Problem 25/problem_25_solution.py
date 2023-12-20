import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Let's start with viewing the fibonacci sequence up to a certain point
def Fibonacci_Numbers_By_DigitsCount(digit_count):
    fib_list = [1,1]

    while len(str(fib_list[-1])) < 1000:
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

results = Fibonacci_Numbers_By_DigitsCount(1000)
print(len(results))

# 1 digit  = 6
# 2 digits = 5
# 3 digits = 5
# 4 digits = 4
# 5 digits = 5
# 6 digits = 5
# 7 digits = 5
# 8 digits = 4