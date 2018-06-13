import os
import unittest
import json
from app import create_app


class TestRequests(unittest.TestCase):

    def setUp(self):
        # Initialize our variable before test
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.user = {"username": 'test', "email": 'test@gmail.com',
                     "password": 'test123'}
        self.user2 = {"username": 'test', "password": 'wrong'}
        self.user3 = {"username": "test2", "email": "test2@gmail.com",
                      "password": "1234"}
        self.user4 = {"username": "test3", "email": "test23.com",
                      "password": "123456"}

    def test_user_signup(self):
        # test api for user signup unsuccessful
        response = self.client().post('/api/v2/auth/signup',
                                      data=json.dumps(self.user),
                                      content_type='application/json')
        self.assertEquals(response.status_code, 201)

    def test_valid_user_login(self):
        # test api for user login successful
        response = self.client().post('/api/v2/auth/login',
                                      data=json.dumps(self.user),
                                      content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertTrue(data["token"])

    def test_invalid_user_login(self):
        # test api for user login unsuccessful
        response = self.client().post('/api/v2/auth/login',
                                      data=json.dumps(self.user2),
                                      content_type='application/json')
        self.assertEquals(response.status_code, 401)

    def test_invalid_user_email(self):
        # test invalid email signup
        response = self.client().post('/api/v2/auth/signup',
                                      data=json.dumps(self.user4),
                                      content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEquals(data['message'], 'Enter valid email')

    def test_invalid_password_length(self):
        # test invalid password length should be atleast 6 char
        response = self.client().post('/api/v2/auth/signup',
                                      data=json.dumps(self.user3),
                                      content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEquals(data['message'],
                          'Password should be atleast 6 characters')


if __name__ == "__main__":
    unittest.main()
