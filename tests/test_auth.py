import os
import unittest
import json
from app import create_app

class TestRequests(unittest.TestCase):


    def setUp(self):
        #Initialize our variable before test	    
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {'email':'ron.ndi@gmail.com', 'password':'rrrrnnnn'}

    def test_valid_user_login(self):
        #test api for user login successful
        response = self.client().post('/api/v1/users/login', data = json.dumps(self.user),
                    content_type = 'application/json') 
        self.assertEquals(response.status_code, 200)
    

if __name__ == "__main__":
    unittest.main()