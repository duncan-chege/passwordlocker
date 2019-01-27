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
    contact.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    contact.delete_user()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
