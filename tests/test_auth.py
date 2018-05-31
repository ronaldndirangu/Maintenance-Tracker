import os
import unittest
import json
from app import create_app

class TestRequests(unittest.TestCase):


    def setUp(self):
        #Initialize our variable before test	    
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user1 = {'email':'ron.ndi@gmail.com', 'password':'rrrrnnnn'}
        self.user2 = {'email':'test@gmail.com', 'password':'pppp'}
        self.user3 = {"user_id": '3', "firstname": "Troy", "lastname": "Now",
                     "email": "troy@gmail.com","password": 'troynow'	}

    def test_valid_user_login(self):
        #test api for user login successful
        response = self.client().post('/api/v1/users/login', data = json.dumps(self.user1),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 200)

    def test_invalid_user_login(self):
        #test api for user login unsuccessful
        response = self.client().post('/api/v1/users/login', data = json.dumps(self.user2),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 401)

    def test_user_signup(self):
        #test api for user login unsuccessful
        response = self.client().post('/api/v1/users/signup', data = json.dumps(self.user3),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 201)
    

if __name__ == "__main__":
    unittest.main()