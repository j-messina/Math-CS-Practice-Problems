# note: the with statement below automatically handles closing a file at the end of the program
with open("problem_11_20x20_grid.txt", "r") as theGRID:  # open file reading of *Jeff Bridges' voice* "THE GRID"
    temp_str = ""
    grid_as_2D_list = []
    temp_list = []

    for line in theGRID.readlines():
        temp_list = []
        for char in line:
            if char >= '0' and char <= '9':
                temp_str += char
                if len(temp_str) >= 2:
                    temp_list.append(int(temp_str))
                    temp_str = ""
            else:
                continue
        grid_as_2D_list.append(temp_list)


