def assuming_rightside_first10():
    with open("problem_13_nums.txt", "r") as infile:  # open file stuffed to the gills with numbers
        sum = 0
        for line in infile.readlines():
            print(int(line[-11:]))
            sum += int(line[-10:])
    print("Sum =", sum)
    print("1st 10 digits of sum =", str(sum)[-10:])

# assuming left side first 10 digits
with open("problem_13_nums.txt", "r") as infile:  # open file stuffed to the gills with numbers
    # num_list = []
    sum = 0
    for line in infile.readlines():
        sum += int(line)
        # num_list.append(line)
print("Sum =", sum)
print("1st 10 digits of sum =", str(sum)[:10])