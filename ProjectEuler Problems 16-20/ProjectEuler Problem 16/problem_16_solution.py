# idea 1: the obvious way - see if python can generate the number, convert it to a string, then sum the elements

# idea 2: build the number using a list, inserting new items at index 0
# when necessary as the number gets bigger...this probably the stupidest
# approach, but I can't think of a better one

print("This program calculates the sum of a given exponent-raised numbers digits.\n")
print("It first asks for the value of the base, then the value of the exponent.\n")
print("For example: if you wanted to sum the digits of 2^1000, you would enter 2 first as the base..")
print("and then enter 1000 for the exponent, as prompted.\n")

done = False
while not done:
    input_base     = input("Enter the value of the base: ")
    if input_base == 'end':
        done = True
        continue
    try:
        input_base = int(input_base)
    except:
        print("Base Value input error ")
        print('Please enter an integer value, or \"end\" to end the program.')
        continue

    input_exponent = input("Enter the value of the exponent: ")
    try:
        input_exponent = int(input_exponent)
    except:
        print("Exponent Value input error ")
        print('Please enter an integer value, or \"end\" to end the program.')
        continue

    # calculate value, convert to string
    beeeeg_NUM_as_string = str(input_base ** input_exponent)

    sum_beeeeg_NUMs_nums = 0

    for num in beeeeg_NUM_as_string:
        sum_beeeeg_NUMs_nums += int(num)

    print('The sum of the digits in {}^{} is {}'.format(input_base, input_exponent, sum_beeeeg_NUMs_nums))
    answer = input('Would you like to see the final value of the power? [Y/n]: ')
    if answer == 'Y':
        print("\n\nVery well.\nThe value of the power was:", beeeeg_NUM_as_string)
    print('\nReturning to start now...\n')
# ----end of while loop -------------------------
print("Ending program now...")