# -*- coding: utf-8 -*-
"""
1. Create ./write_to/users.csv with column headers, if not already exist
2. Create a new user with unique ID num and appends to ./write_to/users.csv
NOTE: The order of values in header in create_csv() need to match with the 
    order of values in user_info in create_user()
    NOTE: get_info() reads existing CSV-file to check for duplicate e-mails
"""

import datetime
import getpass

file_path = './write_to/users.csv'  # TODO: Let user select file

class printcolors:
    GREEN ='\033[0;32m'
    OKGREEN = '\033[1;32m'    # bold, color
    YELLOW ='\033[0;33m'
    WARNING = '\033[1;31m'    # bold, color
    NOCOLOR = '\033[0m'

def create_csv(csv_file):       # Create file with headers if file don't exist
    headers = ['User', 'Admin', 'Name', 'Password', 'Birthdate', 'E-mail']    # TODO: For modularity: this variable should be outside the function and passed as an arg form user input
    
    with open(csv_file, 'w') as csv_file:
        for header in headers:
            csv_file.write(header + ',')
        csv_file.write('\n')    # Add line break after last header

    print(f'\n{printcolors.OKGREEN}  Created:{printcolors.NOCOLOR}', file_path)

def already_registered(new_email):          # Checks if new_mail is already registered
        with open(file_path, 'r') as csv_file:
            line = csv_file.readline()

            for line in csv_file:
                existing_user = line.split(',')

                existing_e_mail = existing_user[-2]     # Second last val of user_info is e-mail, last val is a linebreak
                
                if new_email == existing_e_mail:
                    print(f'{printcolors.WARNING}This e-mail is already registered{printcolors.NOCOLOR}')
                    
                    return True

                elif new_email != existing_e_mail:
                    continue                            # Continue to compare all registered e-mail adresses for duplicates

            return False

def get_info():                 # Get users info from input()
    print(f'{printcolors.OKGREEN}Enter user information{printcolors.NOCOLOR}')

    while True:                 # Loop until valid input
        print(f'- Numbers and special characters NOT allowed -')    # States desiered format
        
        name = input(f'{printcolors.GREEN}Name: {printcolors.NOCOLOR}')
        
        forbid_chars = '123456789§½!"#¤%&/()=+?,.-_\'*<>|@£$€¥{[]}±~¶¡'  # TODO: Is this complete?
        
        if not(len(name) < 2 or any(char in forbid_chars for char in list(name))):
            break   # Breaks if valid input
        
    while True:                 # Loop until valid input
        print(f'- Password may not start with a "0" (zero) -')  # States desiered format
        
        pw = getpass.getpass(f'{printcolors.GREEN}Select Password: {printcolors.NOCOLOR}')
        
        forbid_chars = '0'      # Password may not start with "0" (zero), because the csv shortens e.g. "0001" to "1"
        
        test_pw = list(pw)      # To use in below logical comparison
        
        if not(len(pw) == 0 or test_pw[0] == forbid_chars):
            pw_confirm = getpass.getpass(f'{printcolors.GREEN}Confirm Password: {printcolors.NOCOLOR}')     # Confirm password
        
        if pw == pw_confirm:    # Comfirms password
            break   # Breaks if valid input
    
    while True:                 # Loop until valid input
        print(f'- YYMMDD -')    # States desiered format
        
        birthdate = input(f'{printcolors.GREEN}Birthday: {printcolors.NOCOLOR}')
        
        try:
            int(birthdate)      # Accept only numbers as valid format
        except:
            continue
        else:
            if len(birthdate) == 6:     # TODO: Check for plausible birthdate
                break

    while True:                 # Loop until valid input
        print(f'- Enter your -')        # Formating output to terminal
        
        e_mail = input(f'{printcolors.GREEN}E-mail: {printcolors.NOCOLOR}') # TODO: Validate that it is a proper e-mail adress

        if len(e_mail) >= 6 and not(already_registered(e_mail)):
            e_mail_confirm = input(f'{printcolors.GREEN}Confirm e-mail: {printcolors.NOCOLOR}')     # Confrim e-mail

            if e_mail == e_mail_confirm:    # Comfirms password
                break   # Breaks if valid input

    return pw, name, birthdate, e_mail

def create_user():              # Returns complete user info as list
    is_admin = False

    pw, name, birthdate, e_mail = get_info()

    id_num = str(datetime.datetime.now())    # Give unique value to id_num
    
    # id_num has special characters and whitespace from datetime.datetime.now()
    id_num = id_num.replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
    id_num = 'user' + id_num

    name = name.title()             # Title to accomodate for first and last name

    user_info = [id_num, is_admin, name, pw, birthdate, e_mail]     # TODO: Is tuple better?
    return user_info

def w_user_to_csv(user_info, csv_file):     # Formats list values and append to csv_file
    with open(csv_file, 'a') as csv_file:
        for info in user_info:
            csv_file.write(str(info) + ',')
        csv_file.write('\n')     # Add line break after last info

    print(f'\n{printcolors.OKGREEN}  User have been appended to:{printcolors.NOCOLOR}', file_path, '\n')
    
def new_users():                # Writes user info and asks for more users  
    while True:
        print()     # For formating of output to consol
        
        w_user_to_csv(create_user(), file_path)     # Writes info from create_user() to file_path

        add_more = input('Add more users? y/n: ')

        if add_more.lower() == 'n' or add_more.lower() == 'no':
            print(f'\n{printcolors.WARNING}  PROGRAM TERMINATED{printcolors.NOCOLOR}\n')
            
            break

def main():
    try:
        csv_file = open(file_path, 'r')
        csv_file.close()
    except:
        print('\n ', file_path, f'{printcolors.WARNING}doesn\'t exist{printcolors.NOCOLOR}\n')  # First string is to indent output by two spaces
        
        user_input = input('Would you like to create the file? y/n: ')
        
        if user_input.lower() == 'y' or user_input.lower() == 'yes':
            create_csv(file_path)
            new_users()
        elif user_input.lower() == 'n' or user_input.lower() == 'no':     # TODO: Select new file to write to
            print(f'\n{printcolors.WARNING}  PROGRAM TERMINATED{printcolors.NOCOLOR}\n')
    else:
        new_users()

if __name__ == '__main__':
    main()