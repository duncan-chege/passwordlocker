#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(fname, email):
    '''
    Function to create a new user
    '''
    new_user = User(fname, email)
    return new_user


def create_credential(uname, pword):

    new_credential = Credential(uname, pword)
    return new_credential

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def save_credentials(credential):

    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)


def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credential.credential_exist(username)


# def display_users():
#     '''
#     Function that returns all the saved users
#     '''
#     return User.display_users()


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def generate_password():
    '''
    Function to generate random password
    '''
    return Credential.generate_password()

def main():
    print("Welcome to your account manager app. What is your name?")
    kwanza_name = input()

    print(f"Hello {kwanza_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: ca- create an account, la- log into an account, ex- exit an account")
        shortcode= input().lower()

        if shortcode='ca':
            print("Social media account:")
            sm_account= input()
            print("New Username")
            u_name = input()
            print("New password")
            p_word= input()
            save_credentials(create_credential(sm_account,u_name, p_word))
            print(f"{sm_account} account created for {u_name}")
            print('\n')

        
        print("Use these short codes : cc - create new credentials, dc - display credenials,  del- delete user credenials, ex -exit the user list")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-" * 10)

            print ("First name -")
            f_name = input()

            print("Email address - ")
            e_address = input()

            print ("User name -")
            u_name = input()
            p_word = input()

            # create and save new user.
            save_users(create_user(f_name, e_address))
            # create and save new credential.
            save_credentials(create_credential(u_name, p_word))

            print ('\n')
            print(f"New User {f_name}, alias '{u_name}' created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your users")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.myusername}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'del':
            print("Enter username so that account can be deleted")
            search_username = input()
            if check_existing_credentials(search_username):
                search_credential = find_credential(search_username)
                delete_credential(search_credential)
                print(f"{search_username} is deleted")

            else:
                print("That username doesn't exist")

        elif short_code == "ex":
            print("Until next time")
            break

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
