def isPrime(num):
    for x in range(2, int(num/3) + 1):
        if num % x == 0:
            return False
    return True