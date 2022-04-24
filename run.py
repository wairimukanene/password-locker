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