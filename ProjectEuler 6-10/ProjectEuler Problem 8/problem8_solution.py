# The four adjacent digits in the 1000-digit number that have the greatest product
# are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest
# product. What is the value of this product?

# My Notes: The number will be read from a separate text file.
#         : It is stored in the shape of 20 rows of 50 digits each.

# What are the ways that we can store this massive 1000-digit number?
# - Option 1) Store as a list of lists, essentially a 20-by-50 matrix/array with each list entry
#             being an individual digit
# - Option 2) Store as a list of strings, wherein each list entry is a string that stores all
#             the numbers on the given row
# - Option 3) Assuming that "adjacent" refers only to numbers immediately left and right of each
#             other, than we can store the numbers as one long list and iterate through just that

with open("number.txt", "r") as beegNumFile: # open file reading in the beeeeeg number
    
    # The following processes the text from the file as a list of strings into a list of list of ints
    #   Need to start with an empty list to append it later
    beegNumAsList = []
    #   Take the file text as a list of strings separated by newlines
    for x in beegNumFile.readlines():
        # the "list(map(int..." portion Processes each string in the aforementioned list of strings 
        # by first removing all whitespace via .strip(), then converting the string into a list of ints
        # Each of these newly created lists of ints is then appended onto the empty list we made earlier
        beegNumAsList.append(list(map(int,x.strip())))
    # The end result here is essentially a 2D list of ints, 20 rows by 50 columns
    
    # Before we search for the greatest product, we must have an initial value for the "greatest"
    # The lowest possible product in this case is 0
    greatestProduct = 0
    tempProduct = 0
    skipCounter = 100

    # Note: Using "x" and "y" as variable names here for easier readability;
    # x is going to be the "row number" and y is going to be the "column number" in our 2D list
    
    # As so, we will iterate though the list one adjacent digit at a time, with
    # adjustments for not going out of bounds on each row, and adjusting for zeroes
    # as they will nullify the twelve digits to either side of them
    
    # We've got two cases for when getting the product:
    #   Case 1) All of the digits are on the same row
    #   Case 2) Some of the digits are on the next row
    # We've got two special cases to consider
    #   Special Case 1) When we encounter a 0, we can optimize by skipping ahead 13 places
    #                1a) Additionally, consider when a subsequent zero is found while skipping 13 places
    #   Special Case 2) When we are on the last row, we must end at y = 37      
    for x in range(0, len(beegNumAsList)):
        for y in range(0, len(beegNumAsList[x])):
            # Special Case 2
            if x == len(beegNumAsList) - 1 and y >= len(beegNumAsList[x]) - 13:
                break
                
            # Special Case 1
            if beegNumAsList[x][y] == 0:
                skipCounter = 0
                continue
            elif skipCounter < 13:
                skipCounter += 1
                continue
    
            tempProduct = 1
            # Case 1
            if len(beegNumAsList[x]) - y >= 13:    
                for z in range(0, 13):
                    tempProduct *= beegNumAsList[x][y+z] # z works as the offset for the 13 numbers
            # Case 2
            else: 
                remainingLength = len(beegNumAsList[x]) - y
                for z in range(0, remainingLength): # multiply remaining numbers on current row
                    tempProduct *= beegNumAsList[x][y+z]
                for z in range(0, 13 - remainingLength): # then do the remaining amount at start of next row
                    tempProduct *= beegNumAsList[x+1][z]
        
            if tempProduct > greatestProduct:
                greatestProduct = tempProduct
                
    print("Greatest product of 13 adjacents =", greatestProduct)
                
            
#------------------------------------------------------------------------
# End of program, closing the opened file now
# beegNumFile.close() # <--- only necessary if not using with statement