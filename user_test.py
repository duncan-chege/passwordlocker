import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Clark","c@gmail.com") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.myfirstname,"Clark")
        self.assertEqual(self.new_user.myemail,"c@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Oliver","o@gmail.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.save_contact()
        test_user = User("Hal","h@gmail.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)




if __name__ == '__main__':
    unittest.main()
