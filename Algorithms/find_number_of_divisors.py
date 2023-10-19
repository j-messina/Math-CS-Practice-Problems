import math
def find_number_of_divisors (num):
    num_of_divisors = 2
    sq_rt = math.sqrt(num)
    if sq_rt == int(sq_rt):
        # is_whole = True
        num_of_divisors += 1
    for x in range(2, int(sq_rt)):
        if num % x == 0:
            num_of_divisors += 2
    return num_of_divisors