# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025.

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
sumOfNums = 0
sumOfSquares = 0
for num in range(1,101):
    sumOfNums += num
    sumOfSquares += pow(num, 2)

squareOfSumOfNums = pow(sumOfNums, 2)
finalDifference = squareOfSumOfNums - sumOfSquares

print("Difference is:\n{} - {} = {}".format(squareOfSumOfNums, sumOfSquares, finalDifference))