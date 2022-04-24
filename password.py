class User:
    '''
    This class helps generate instances for creating a new account on this application
    '''
    profile_list = [] # empty profile list
    def __init__(self, userName, password):
        '''
        This function helps define properties to create a PASSWORD-MANAGER account.
        Args: 
            userName: user's username
            password: user's password
        '''
        self.userName = userName
        self.password = password


    def save_profile(self):
        '''
        Test to save a new profile
        '''
        User.profile_list.append(self)



