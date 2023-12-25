import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
def sum_diags(spiral_layer):
    # Declare some variables
    DOWN_RIGHT_START = 1
    DOWN_LEFT_START  = 1
    UP_LEFT_START    = 1
    UP_RIGHT_START   = 1
    d_r = DOWN_RIGHT_START
    d_l = DOWN_LEFT_START
    u_l = UP_LEFT_START
    u_r = UP_RIGHT_START

    incr = 2
    next_add = 2
    diag_sum = 1
    iterations_count = 2
    iterations_end = (spiral_layer+1)/2
    fourths_counter = 0

    while iterations_count <= iterations_end:
        if fourths_counter == 0:
            d_r      += next_add
            diag_sum += d_r
            next_add += incr
        elif fourths_counter == 1:
            d_l      += next_add
            diag_sum += d_l
            next_add += incr
        elif fourths_counter == 2:
            u_l      += next_add
            diag_sum += u_l
            next_add += incr
        elif fourths_counter == 3:
            u_r      += next_add
            diag_sum += u_r
            next_add += incr
        elif fourths_counter == 4:
            fourths_counter = 0
            iterations_count += 1
            continue
        fourths_counter+=1
    return diag_sum
        
target = 1001
result = sum_diags(target)
print("Sum of diagonals on a", target, "by", target, "spiral is:", result)