#!/usr/bin/env python3.8
from password import Credential
from password import User

def create_profile(username, password):
    '''
    Function to create a new user profile
    '''
    new_profile = User(username, password)
    return new_profile

def save_profile(profile):
    '''
    Function to save user profile
    '''
    profile.save_profile()

    ## user class code above
## credential class code below
def create_account(accountName, accountUsername, accountPassword):
    '''
    Function to creates a new account
    '''
    new_account = Credential(accountName, accountUsername, accountPassword)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()