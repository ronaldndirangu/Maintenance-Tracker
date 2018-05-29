import unittest
from datetime import datetime

class TestUser(unittest.TestCase):

    def test_user_firstname_isalpha(self):
        self.assertTrue(user["firstname"].isalpha(), msg=None)

    def test_user_lastname_isalpha(self):
        self.assertTrue(user["lastname"].isalpha(), msg=None)

    def test_email_validity(self):
        self.assertIn('@', user["email"])
        self.assertIn('.', user["email"])

    def test_length_of_password(self):
        self.assertGreaterEqual(len(user["password"]), 8)


if __name__ == "__main__":
    user = {"firstname": "Ronald", "lastname":"Ndirangu", 
        "email":"ron@gmail.com", "password":"1234asdf"}
    unittest.main()
