import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

import os
import shutil
PARENT_DIRECTORY = "/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/"
TEMPLATE_FILE_PATH = '/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/ProjectEuler Problems Folder Template/ProjectEuler Problem _ 1/problem_x_solution.py'
TEMPLATE_FILENAME = 'problem_x_solution.py'
directory = ''
path = ''

def make_new_folder():
    print('Note: New ProjectEuler directories come in groups of 5.')
    make_x_directories = input('Enter how many new directories: ')
    while not make_x_directories.isdigit():
        print("Invalid input '{}', please try again.\n".format(make_x_directories))
        make_x_directories = input('Enter how many new directories: ')
    print('To confirm, are you sure you want to create {} new directories? (Y/*)')
    decision = input("Anything other than 'Y' will end cancel this process and return to the main menu: ")
    if decision != 'Y':
        return
    valid_start_number = False
    while not valid_start_number:
        start_number = input('What is the starting problem number? ')
        if start_number.isdigit():
            valid_start_number = True
            start_number = int(start_number)
        elif start_number == 'q' or start_number == 'Q':
            return
        else:
            print("Invalid input.")
    
    for count in range (0, int(make_x_directories)):
        folder_name = 'ProjectEuler Problems {}-{}'.format(str(start_number), str(start_number+4))
        folder_path = os.path.join(PARENT_DIRECTORY, folder_name)
        os.mkdir(folder_path) # now we need to make the specific problem folders inside
        for problem_num in range(start_number, start_number+5):
            # first make the problem folder
            problem_folder_name = 'ProjectEuler Problem ' + str(problem_num)
            problem_folder_path = os.path.join(folder_path, problem_folder_name)
            os.mkdir(problem_folder_path)
            # then add in the .py file
            shutil.copy(TEMPLATE_FILE_PATH, problem_folder_path)
            problem_file_new_name = os.path.join(problem_folder_path, 'problem_{}_solution.py'.format(problem_num))
            copied_file_path = os.path.join(problem_folder_path, TEMPLATE_FILENAME)
            os.rename(copied_file_path, problem_file_new_name)
            # add in the README file
            readme_filename = 'README.md'
            readme_file_path = os.path.join(problem_folder_path, readme_filename)
            f = open(readme_file_path, 'w')
            readme_text = "<h1> ProjectEuler Problem {0}: </h1>\n\n<hr>\n\nURL: https://projecteuler.net/problem={0}".format(problem_num)
            f.write(readme_text)
            f.close()
            


        print("Directory '% s' created" % folder_name)
        print('...')
        start_number += 5




def print_main_menu():
    print("Main Menu\n____")
    print_options()
    print("_______________________________________________")
    




def print_options():
    print("Enter 1 to create new ProjectEuler directories.")
    print("Enter q to quit.")





running = True
while running:
    print_main_menu()
    user_input = ''
    valid_user_input = False
    while not valid_user_input:
        user_input = input("Select an option: ")
        if user_input == '1':
            make_new_folder()
            valid_user_input = True
        elif user_input == 'q' or user_input == 'Q':
            running = False
            valid_user_input = True
        else:
            print("Unrecognized input '{}', please try again.\n".format(user_input))
            print_options()
            print()


print("Ending program now...")

