# note: the with statement below automatically handles closing a file at the end of the program
with open("problem_11_20x20_grid.txt", "r") as theGRID:  # open file reading of *Jeff Bridges' voice* "THE GRID"
    temp_str = ""
    grid_as_2D_list = []
    temp_list = []

    #
    for line in theGRID.readlines():
        temp_list = []
        temp_str = ''
        for char in line:
            if char >= '0' and char <= '9':
                temp_str += char
                if len(temp_str) >= 2:
                    temp_list.append(int(temp_str))
                    temp_str = ''
            else:
                continue
        grid_as_2D_list.append(temp_list)

    # grid_as_2D_list should now be a list of list of ints

    # let's first process the horizontal direction
    greatest_product = 0
    num_of_multiplicands = 4
    for line in grid_as_2D_list:
        for item_index in range(0, len(line) - num_of_multiplicands):
            temp_product = 1
            for offset in range(0,4):
                temp_product *= line[item_index + offset]
            # by this line we have the product of the numbers in the current grouping
            if greatest_product < temp_product:
                greatest_product = temp_product
    print("Greatest adjacent product of 4 numbers in the grid is:", greatest_product)


    # now vertical direction
    for row in range(0, len(grid_as_2D_list) - num_of_multiplicands):
        for col in range(0, len(grid_as_2D_list[row])):
            temp_product = 1
            for offset in range(0,4):
                temp_product *= grid_as_2D_list[row + offset][col]
            if greatest_product < temp_product:
                greatest_product = temp_product
    print("Greatest adjacent product of 4 numbers in the grid is:", greatest_product)

    # now bottom-left to upper-right diagonal
    for row in range(num_of_multiplicands - 1, len(grid_as_2D_list)):
        for col in range(0, len(grid_as_2D_list[row]) - num_of_multiplicands):
            temp_product = 1
            for offset in range(0, 4):
                temp_product *= grid_as_2D_list[row - offset][col + offset]
            if greatest_product < temp_product:
                greatest_product = temp_product
    print("Greatest adjacent product of 4 numbers in the grid is:", greatest_product)

    # now upper-left to bottom right diagonal
    for row in range(0, len(grid_as_2D_list) - num_of_multiplicands):
        for col in range(0, len(grid_as_2D_list[row]) - num_of_multiplicands):
            temp_product = 1
            for offset in range(0, 4):
                temp_product *= grid_as_2D_list[row + offset][col + offset]
            if greatest_product < temp_product:
                greatest_product = temp_product
    print("Greatest adjacent product of 4 numbers in the grid is:", greatest_product)