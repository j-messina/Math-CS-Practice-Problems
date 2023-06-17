# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

product = 0
highestPalindrome = 0
isPalindrome = False
for x in range(101, 1000):
    if x % 10 == 0:
        continue
    else:
        for y in range(101, 1000):
            product = str(x * y)
            isPalindrome = True
            w = 0
            for z in range(0, int(len(product)/2)):
                w -= 1
                if product[z] != product[w]:
                    isPalindrome = False
                    break
            if isPalindrome and int(product) > highestPalindrome:
                highestPalindrome = int(product)
                print("New highest palindrome:", highestPalindrome)
