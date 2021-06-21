import unittest
from email_validator import validate_email, EmailNotValidError

# testing the email address
def email_validation():
        valid = validate_email('mikayla@trade245.com')
        return valid

class Email(unittest.TestCase):
    def checking(self):
        x = validate_email('mikayla@trade245.com')

    def testing(self):
        self.assertTrue(validate_email('mikayla@trade245.com'))

if __name__ == '__main__':
    unittest.main()
