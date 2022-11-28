
import unittest
from random import Random

from account_creation import isValidPhoneNumber, isValidEmail, register_user, generateFile_key


class TestAccount_creation(unittest.TestCase):
     
    def test_isValidPhoneNumber(self) -> None:
        """
        **Description**:
        
        Tests the isValidPhoneNumber function given a set of user inputs, both right and wrong
        """
        # phone number with no parentheses
        phoneNumber = '2015589634'
        self.assertEqual(isValidPhoneNumber(phoneNumber), False)

        # phone number with more than 10 digits 
        phoneNumber = '(201) 558-963478'
        self.assertEqual(isValidPhoneNumber(phoneNumber), False)
        
        # wrong input with characters
        phoneNumber = 'h25456h7jkk'
        self.assertEqual(isValidPhoneNumber(phoneNumber), False)

        # wrong input with less than 10 digits; test should fail
        phoneNumber = '(201) 563-856'
        self.assertNotEqual(isValidPhoneNumber(phoneNumber), True)

        # correct phone number
        phoneNumber = '(201) 558-9634'
        self.assertEqual(isValidPhoneNumber(phoneNumber), True)
  
    def test_isValidEmail(self) -> None:

        """
        **Description**:
        
        Tests the isValidEmail function given a set of user inputs, both right and wrong
        """
        # wrong email 
        email = 'user#hkolmn.com'
        self.assertEqual(isValidEmail(email), False)

        # wrong email
        email = 'user2@ghh.'
        self.assertEqual(isValidEmail(email), False)

        # correct email
        email = 'user1@gmail.com'
        self.assertEqual(isValidEmail(email), True)

        # correct email
        email = 'user2@stevens.edu'
        self.assertEqual(isValidEmail(email), True)

    def test_register_user(self) -> None:
        
        """
        **Description**:
        
        Tests the register_user function given a set of user inputs, both right and wrong
        """
        # add new account
        email = 'user1@gmail.com'
        phoneNumber = '(201) 256-5632'
        password = 'pks#$)85|}'
        cfm_password = 'pks#$)85|}'

        result = register_user(email, phoneNumber, password, cfm_password)

        # if user already exists, function should return 0 else create a new account
        if(result != 1):
            self.assertEqual(result, 0)
        else:
            self.assertEqual(result, 1)

        # passwords do not match
        email = 'user3@gmail.com'
        phoneNumber = '(201) 256-5632'
        password = 'pks#$)85|}'
        cfm_password = 'pks#$)85|}7'
        result = register_user(email, phoneNumber, password, cfm_password)
        self.assertEqual(result, None)

        # invalid email address
        email = 'user4gmail.com'
        phoneNumber = '(201) 256-5632'
        password = 'pks#$)85|}'
        cfm_password = 'pks#$)85|}'
        result = register_user(email, phoneNumber, password, cfm_password)
        self.assertEqual(result, None)

        # invalid phone number format
        email = 'user3@gmail.com'
        phoneNumber = '(201) 2565632'
        password = 'lpebs#$)77|}'
        cfm_password = 'lpebks#$)77|}'
        result = register_user(email, phoneNumber, password, cfm_password)
        self.assertEqual(result, None)

        # passwords is not at least 8 characters long
        email = 'user3@gmail.com'
        phoneNumber = '(201) 256-5732'
        password = 'pks#$)'
        cfm_password = 'pks#$)'
        result = register_user(email, phoneNumber, password, cfm_password)
        self.assertEqual(result, None) 
  
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)