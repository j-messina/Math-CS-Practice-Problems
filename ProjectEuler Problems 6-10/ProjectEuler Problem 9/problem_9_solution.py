"""
a + b + c = 1000
a^2 + b^2 = c^2
a < b < c

range?

c = (a^2 + b^2)^0.5

a + b + (a^2 + b^2)^0.5 = 1000
a^2 + b^2 = (1000 - a - b)^2
          = (1000000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab + b^2)
         0 = 1000000 - 2000a - 2000b + 2ab
         1000000 = 2000a + 2000b - 2ab
          500000 = 1000a + 1000b - ab
          500000 = a(1000 - b) + 1000b

let a = 50
500000 = (50)(1000 - b) + 1000b
500000 = 50000 - 50b + 1000b
500000 - 50000 = 950b
450000 = 950b
b = 450000/950 = 473.68

The problem becomes: Given a, and solve for b --> if b is integer, return
500000 = 1000a + b(1000 - a)
500000 - 1000a = b(1000 - a)
b = (500000 - 1000a) / (1000 - a)
"""

import math

# b = 0
# for a in range(1, 1000):
#     b = (500000 - 1000*a) / (1000 - a)
#     print("a = {}\nb = {}\nc = {}\n\n".format(a, b, 1000 - a - b))
#     if type(b) == type(1) or a >= int(b):
#         break
#     if a >= 999:
#         print("YOU FAIL")

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = (math.sqrt(a**2 + b**2))
        # print("a = {}\nb = {}\nc = {}\n\n".format(a, b, c))
        if c > b:
            if a + b + c == float(1000):
                print("a = {}\nb = {}\nc = {}\nabc = {}\n\n".format(a, b, c, a*b*c))
                break