# -*- coding: utf-8 -*-
"""
1. Create ./write_to/users.csv with column headers, if not already exist
2. Create a new user with unique ID num and appends to ./write_to/users.csv
"""

import datetime

file_path = './write_to/users.csv'  # TODO: Let user select file

class printcolors:
    OKGREEN = '\033[1;32m'    # bold, color
    WARNING = '\033[1;31m'    # bold, color
    NOCOLOR = '\033[0m'

def create_csv(csv_file):       # Create file with headers if file don't exist
    headers = ['User', 'Admin', 'Password', 'Name', 'Birthdate']    # TODO: This variable should be outside the function and passed as an arg
    with open(csv_file, 'w') as csv_file:
        for header in headers:
            csv_file.write(header + ',')
        csv_file.write('\n')    # Add line break after last header

    print(f'\n{printcolors.OKGREEN}  Created:{printcolors.NOCOLOR}', file_path)

def get_info():
    print(f'{printcolors.OKGREEN}Enter user information{printcolors.NOCOLOR}')
    while True:                 # Loop until valid input
        name = input('Name: ')
        
        forbidden_chars = '123456789§½!"#¤%&/()=+?,.-_\'*<>|@£$€¥{[]}±~¶¡'  # TODO
        if len(name) < 2 or any(char in forbidden_chars for char in list(name)):
            continue
        else:   # Breaks if valid input
            break
        
    while True:                 # Loop until valid input
        pw = input('Select Password: ')
        
        forbidden_char = '0'    # Password may not start with "0" (zero), because the csv shortens e.g. "0001" to "1"
        test_pw = list(pw)
        if len(pw) == 0 or test_pw[0] == forbidden_char:
            continue
        else:
            break
    
    while True:                 # Loop until valid input           
        birthdate = input('Birthday | YYMMDD: ')
        try:
            int(birthdate)      # Accept only numbers as valid format
        except:
            continue
        else:
            if len(birthdate) == 6:     # TODO: Check for plausible birthdate
                break

    return pw, name, birthdate

def create_user():              # Returns complete user info as list
    is_admin = False

    pw, name, birthdate = get_info()

    id_num = str(datetime.datetime.now())    # Give unique value to id_num
    
    # id_num has special characters and whitespace from datetime.datetime.now()
    id_num = id_num.replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
    id_num = 'user' + id_num

    name = name.title()     # Title to accomodate for first and last name

    user_info = [id_num, is_admin, pw, name, birthdate]     # TODO: Is tuple better?
    return user_info

def w_user_to_csv(user_info, csv_file):
    with open(csv_file, 'a') as csv_file:
        for info in user_info:
            csv_file.write(str(info) + ',')
        csv_file.write('\n')     # Add line break after last info

    print(f'\n{printcolors.OKGREEN}  User have been appended to:{printcolors.NOCOLOR}', file_path, '\n')
    
def new_users():
    while True:
        print()     # For formating of output to consol
        w_user_to_csv(create_user(), file_path)

        add_more = input('Add more users? y/n: ')
        if add_more.lower() == 'n' or add_more.lower() == 'no':
            print(f'\n{printcolors.WARNING}  PROGRAM TERMINATED{printcolors.NOCOLOR}\n')
            break

def main():
    try:
        csv_file = open(file_path, 'r')
        csv_file.close()
    except:
        print(' ', file_path, f'{printcolors.WARNING}doesn\'t exist{printcolors.NOCOLOR}\n')  # First string is to indent output by two spaces
        user_input = input('Would you like to create the file? y/n: ')
        if user_input.lower() == 'y' or user_input.lower() == 'yes':  # TODO: Breaks program - can't read an existing file and append to
            create_csv(file_path)
            new_users()
        if user_input.lower() == 'n' or user_input.lower() == 'no':     # TODO: Select new file to write to
            print(f'\n{printcolors.WARNING}  PROGRAM TERMINATED{printcolors.NOCOLOR}\n')
    else:
        new_users()

if __name__ == '__main__':
    main()