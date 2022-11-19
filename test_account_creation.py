
import unittest

from account_creation import  isValidPhoneNumber, isValidEmail


class TestAccount_reation(unittest.TestCase):
     
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


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)