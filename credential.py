class Credential:

    '''
    Class that creates new instance of credentials
    '''
    credential_list=[]

    def __init__(self,username,password):
        self.myusername=username
        self.mypassword=password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_username(cls,personusername):
        '''
        Method that takes in a username and returns a credential that matches that username.
        '''

        for credential in cls.credential_list:
            if credential.myusername == personusername:
                return credential

    @classmethod
    def credential_exist(cls,personusername):
        '''
        Method that checks if a credential exists from the credential list.
        '''
        for credential in cls.credential_list:
            if credential.myusername == personusername:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
