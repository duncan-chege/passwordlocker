#!/usr/bin/env python3.6
from user import User

def create_user(fname,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Welcome to your user list. What is your name?")
            first_name = input()

            print(f"Hello {first_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new user, dc - display users, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Email address ...")
                            e_address = input()

                            save_users(create_user(f_name,e_address)) # create and save new user.
                            print ('\n')
                            print(f"New User {f_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
