import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

def is_SO5PD(num):
    num_as_str = str(num)
    mysum = 0
    for digit in num_as_str:
        digit = int(digit)
        mysum += digit**5
    if num == mysum:
        return True
    else:
        return False

sum_results = 0
for x in range(2,1000000):
    if is_SO5PD(x):
        print("Found valid number:", x)
        sum_results+=x

print("Sum of them all:", sum_results)