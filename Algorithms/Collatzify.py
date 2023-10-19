def Collatzify(num):
    if num % 2 == 0:
        return num/2
    else:
        return (3*num) + 1