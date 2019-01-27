class User:
    '''
    Class that generates new users
    '''
    user_list=[]

    def __init__(self,firstname,email):
        '''
        defining properties for our object
        '''
        self.myfirstname=firstname
        self.myemail=email

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_User(self):

        '''
        delete_User method deletes a saved User from the User_list
        '''

        User.User_list.remove(self)
