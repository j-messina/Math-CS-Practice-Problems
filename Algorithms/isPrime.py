def isPrime(num):
    if num % 2 == 0:
        return False

    if num < 10000:
        for x in range(3, int(num/3) + 1, 2):
            if num % x == 0:
                return False
    else:
        ten_power = 2
        while num / 100**ten_power >= 100:
             ten_power+=1
        for x in range(3, int(num/10**ten_power) + 1, 2):
            if num % x == 0:
                return False
    return True

