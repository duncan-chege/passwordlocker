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
