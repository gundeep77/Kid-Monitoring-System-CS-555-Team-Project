import unittest
from login import login


class TestLogin(unittest.TestCase):

    def test_login(self):
        
        """
        **Description**:
        Tests the login function given a set of user inputs, both right and wrong
        """

        # user exits and password is correct
        email = 'user1@gmail.com'
        password = 'pks#$)85|}'
        result = login(email, password)
        self.assertEqual(result, 1)

        # user does not exist
        email = 'uyt775@gmail.com'
        password = 'psgh#4*-jh&'
        result = login(email, password)
        self.assertEqual(result, None)

        # user exits but the password is incorrect
        email = 'user1@gmail.com'
        password = 'psgh#4*-jh&'
        result = login(email, password)
        self.assertEqual(result, None)

        # user does not exit and the password is incorrect
        email = 'usr/2@gmail.com'
        password = 'psgh#4*-jh&'
        result = login(email, password)
        self.assertEqual(result, None)

         # user does not exits but password is correct
        email = 'us*&/@gmail.com'
        password = 'pks#$)85|}'
        result = login(email, password)
        self.assertEqual(result, None)

if __name__ == '__main__':
   unittest.main(exit = False, verbosity = 2)
