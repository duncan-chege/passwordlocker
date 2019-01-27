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
