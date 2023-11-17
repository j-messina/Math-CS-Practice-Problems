from math import factorial

num_as_str = str(factorial(100))
sum = 0

for x in num_as_str:
    sum += int(x)

print('Sum of digits in 100! is', sum)