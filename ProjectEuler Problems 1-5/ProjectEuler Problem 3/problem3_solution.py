# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Steps:
# 1) Make/borrow a function for checking if the value is prime
#       - approach 1: make it myself -->
#       - approach 2: find and use some already built method for finding if a number is prime
# 2) Use that function to find largest prime factor
#       - approach 1: increments starting at 3, if value divides evenly (check using modulus operator)
#         then check if its factor pair partner is prime --> first success is returned
#       - approach 2: decrements from product/3 rounded down, checks if number is prime
#         --> if so, return it
def isPrime(num):
    for x in range(2, int(num/3)):
        if num % x == 0:
            return False
    return True


def findHighestPrimeFactor(inputValue):
    largestPrimeFactorFound = 1
    for x in range(2, int(inputValue/3)):
        if inputValue % x == 0:
            if isPrime(inputValue/x):
                return inputValue/x
            elif isPrime(x):
                largestPrimeFactorFound = x
        if x >= int(inputValue/x):
            #print("Approx root reached at", inputValue/x)
            return largestPrimeFactorFound
    # normally, the function should never reach the next line, so it will have a distinct return value just in case
    return 0

pe_inputValue = 600851475143
print("The largest prime factor of", pe_inputValue, "is", findHighestPrimeFactor(pe_inputValue))