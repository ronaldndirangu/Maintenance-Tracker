import os
import unittest
import json
from app import create_app, requests
from app.views import app

class TestRequests(unittest.TestCase):


    def setUp(self):
        #Initialize our variable before test	    
        self.app = create_app("testing")
        self.client = self.app.test_client 
        self.request ={
                        "request_id":3,
                        "date": '12/1/2018',
                        "title": "Replace Motor",
                        "location": "Liquid Plant",
                        "priority":"High",
                        "description": "Motor overheating due to unbalanced windings",
                        "status":"pending",
                        "created_by":"John"
                    }

    def test_api_for_user_create_request(self):
        #test endpoint to create request by user
        response = self.client().post("/api/v1/users/requests/", data = json.dumps(self.request)
                    ,content_type='application/json')
        self.assertEquals(response.status_code, 201)

    def test_api_for_user_read_request(self):
        resource = self.client().get('/api/v1/users/requests')
        self.assertEqual(resource.status_code,200)

    
    

if __name__ == "__main__":
    unittest.main()