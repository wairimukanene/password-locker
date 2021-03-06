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

    def tearDown(self):
        '''
        cleans up each credential list after instance
        '''
        Credential.credentials_list = []


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

         # save multiple accounts
    def test_save_multiple_accounts(self):
        '''
        Test case to check if users can save multiple accounts
        '''
        self.new_account.save_account()
        test_account = Credential('Test', 'ninakamau', 'nania')
        test_account.save_account()
        self.assertEqual(len(Credential.credentials_list),2)


        #delete account
    def test_delete_account(self):
        '''
        Test case to check if user can delete an account
        '''
        self.new_account.save_account()
        test_account = Credential('Test', 'ninakamau', 'nania')
        test_account.save_account()

        self.new_account.delete_account() #deletes account object
        self.assertEqual(len(Credential.credentials_list),1)

        # search account by id
    def test_find_account_by_id(self):
        '''
        Test case to check if we can find an account by username and display information
        '''
        self.new_account.save_account()
        test_account = Credential('Test', 'ninakamau', 'nania')
        test_account.save_account()

        found_account = Credential.find_by_id('ninakamau')
        self.assertEqual(found_account.accountUsername,test_account.accountUsername)

        # check if account exist
    def test_account_exists(self):
        '''
        Test case to check if a user account already exist returns a boolean
        '''
        self.new_account.save_account()
        test_account = Credential('Test', 'ninakamau', 'nania')
        test_account.save_account()

        account_exists = Credential.account_exist('ninakamau')
        self.assertTrue(account_exists)

         # display available accounts
    def test_display_all_accounts(self):
        '''
        Method that returns a list of all saved accounts

        '''

        self.assertEqual(Credential.display_accounts(),Credential.credentials_list)

        #class condition
if __name__ == '__main__':
    unittest.main()



