hundred = 'hundred'

num_to_words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
   100: 'hundred',
  1000: 'onethousand'
}

def find_num_words(num):
    output_list = []
    if num == 1000:
        output_list.append(num_to_words[1000])
    if 100 <= num <= 999:
        hundreds_digit = int(num/100)
        # total_letters = len(num_to_words[hundreds_digit]) + len(num_to_words[100]) + len("and")
        output_list.append(num_to_words[hundreds_digit])
        output_list.append(num_to_words[100])
        if num % 100 != 0:
            output_list.append("and")
    if 20 <= num % 100 <= 99:
        tens_digit = int((num % 100)/10)
        output_list.append(num_to_words[tens_digit * 10])
        ones_digit = num % 10
        output_list.append(num_to_words[ones_digit])
    elif 1 <= num%100 <= 19:
        output_list.append(num_to_words[num % 100])
    return output_list

def debug_calc_num_words(input_num):
    word_list = find_num_words(input_num)
    output_string = ""
    total_letters = 0
    for word in word_list:
        for letter in word:
            output_string += letter + " "
            total_letters += 1
        output_string += '= ' + str(len(word)) + '\n'
    output_string += "Total number of letters = " + str(total_letters)
    print(output_string)

def test_output():
    my_input = ""
    while my_input != "end":
        my_input = ""
        my_input = input("Enter any number from 1 to 1000: ")
        if my_input == 'end':
            print("Ending program now...")
            break
        try:
            my_input = int(my_input)
        except:
            print("Invalid input, please try again.")
        else:
            if my_input == -1:
                testing_sum = 0
                for x in range(1,1001):
                    debug_calc_num_words(x)
                    testing_sum += find_total_letters(x)
                    print('\nCURRENT TOTAL LETTERS====', testing_sum, '\n')

            else:
                print(debug_calc_num_words(my_input))

def find_total_letters(num):
    word_list = find_num_words(num)
    total_letters = 0
    for word in word_list:
        for letter in word:
            total_letters += 1
    return total_letters

test_output()
