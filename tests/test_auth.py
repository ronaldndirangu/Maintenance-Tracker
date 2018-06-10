import os
import unittest
import json
from app import create_app

class TestRequests(unittest.TestCase):

    def setUp(self):
        #Initialize our variable before test        
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.user = {"username":'test', "email":'test@gmail.com', "password":'test123', "role":False}	
        self.user2 = {"username":'test', "password":'wrong'} 

    def test_user_signup(self):
        #test api for user signup unsuccessful
        response = self.client().post('/api/v2/auth/signup', data = json.dumps(self.user),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 201)             

    def test_valid_user_login(self):
        #test api for user login successful
        response = self.client().post('/api/v2/auth/login', data = json.dumps(self.user),
                    content_type = 'application/json')
        data = json.loads(response.data.decode()) 
        self.assertTrue(data["token"])

    def test_invalid_user_login(self):
        #test api for user login unsuccessful
        response = self.client().post('/api/v2/auth/login', data = json.dumps(self.user2),
                    content_type = 'application/json')
        self.assertEquals(response.status_code, 401)
    

if __name__ == "__main__":
    unittest.main()