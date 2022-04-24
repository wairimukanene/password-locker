import unittest #unitest module
from password import Credential #imports Credential class for testing
from password import User #imports User class for testing

class TestUser(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    Args:
        Testcase class taht helps create test cases for User
    '''

    # test to check if user object is instatiated properly
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_profile = User('Wairimu','Kanene')

    def test__init(self):
        '''
        Test case to test if User object is instantiated correctly
        '''
        self.assertEqual(self.new_profile.userName, 'Wairimu')
        self.assertEqual(self.new_profile.password, 'Kanene')

        #end of class user test
        #start of class credential test

class TestCredential(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    
    Args:
        Testcase class that helps create test cases for Credential
    '''

    #test to check if credential object is instantiated properly
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_account = Credential('instagram', 'wairimuKanene', 'wa.irim.u') #sample login details for a new instagram account 

    def test__init(self):
        '''
        Test case to test if credential object is instantiated correctly
        '''
        self.assertEqual(self.new_account.accountName, 'instagram')
        self.assertEqual(self.new_account.accountUsername,'wairimuKanene')
        self.assertEqual(self.new_account.accountPassword,'wa.irim.u')

         # save account
    def test_save_account(self):
        '''
        Test case to check account object is saved into the contact list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credential.credentials_list),1)



