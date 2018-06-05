import os
import unittest
import json
from app.views import app

class TestRequests(unittest.TestCase):

    def setUp(self):
        #Initialize our variable before test        
        self.app = app
        self.client = self.app.test_client
        self.user = {"user_id": '1', "firstname": "Ron", "lastname": "Ndi", 
		                "email": "ron.ndi@gmail.com","password": 'rrrrnnnn'	}

    def test_valid_user_login(self):
        #test api for user login successful
        response = self.client().get('/api/v1/users/login', data = json.dumps(self.user),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 200)

    def test_invalid_user_login(self):
        #test api for user login unsuccessful
        response = self.client().get('/api/v1/users/login', data = json.dumps(self.user),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 401)

    def test_user_signup(self):
        #test api for user signup unsuccessful
        response = self.client().post('/api/v1/users/signup', data = json.dumps(self.user),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 201)
    

if __name__ == "__main__":
    unittest.main()