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


    def delete_profile(self):
        '''
        Test to delete user's profile
        '''
        User.profile_list.remove(self)


# end of users instances
#starts of accounts credentials
## generate credentials instances


class Credential:
    '''
    This class helps generate instances for new and or existing online accounts log in credentials
    '''


    credentials_list = [] # empty list that will hold online accounts log in details

    def __init__(self, accountName, accountUsername, accountPassword):
        '''
        This function helps define properties of new and or existing accounts objects.
        Args:
            accountName: brand name of user online account. For example; 'pintrest'
            accountUsername: user username of a specified online account.
            accountPassword: user password for an online account.
        '''




