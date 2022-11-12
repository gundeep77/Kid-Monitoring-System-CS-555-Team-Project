
import unittest
from authenticate import authenticate
import pyotp
import time

class TestAuthenticate(unittest.TestCase):
    """
    **Description**:
    
    Class for unit testing the authentication methods.
    """

    def test_authenticate (self) -> None:
        """
        **Description**:
        
        Tests the authentication function given a set of user inputs, both right and wrong
        """

        totp = pyotp.TOTP('base32secret3232')

        # arbritary wrong input with 10 digit 
        user_input1 = '0000000001'

        self.assertEqual(authenticate(user_input1), False)

        # remplace user_input1 with correct input which must have 6 digits
        user_input2 = totp.now()

        self.assertEqual(authenticate(user_input2), True)

        time.sleep(30)

        # verify user_input2 after 30 secondes
        self.assertEqual(totp.verify(user_input2), False)

        # input_user2 is no more valid 
        self.assertEqual(authenticate(user_input2), False)
       
    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)