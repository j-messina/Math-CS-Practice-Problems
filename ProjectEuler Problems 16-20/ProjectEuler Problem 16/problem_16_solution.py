import math
from Algorithms.find_number_of_divisors import *

target_num_of_divisors = 500
found = False
triangle_number = 55
adder = 11

while find_number_of_divisors(triangle_number) < 500:
    triangle_number += adder
    adder+=1

print("The first triangle number with at least 500 divisors is", triangle_number)