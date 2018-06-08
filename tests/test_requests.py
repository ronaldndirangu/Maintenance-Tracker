import os
import unittest
import json
from app import create_app
from app.models import User

class TestRequests(unittest.TestCase):

    def setUp(self):
        #Initialize our variable before test	    
        self.app = create_app("testing")
        self.client = self.app.test_client 
        users = User()
        self.request ={
                        "date": '12/1/2018',
                        "title": "Replace Motor",
                        "location": "Liquid Plant",
                        "priority":"High",
                        "description": "Motor overheating due to unbalanced windings",
                        "status":"pending",
                        "created_by":"John"
                    }
        self.user = {"username":'test', "email":'test@gmail.com', "password":'test123'}
        self.logged_in_user = users.login(self.user['username'], self.user['password'])
        response = self.client().get('/api/v1/users/login', data = json.dumps(self.user),
                    content_type = 'application/json')
        self.data = json.loads(response.data.decode())
        

    def test_api_for_user_create_request(self):
        #test endpoint to create request by user
        token = self.data['token']
        response = self.client().post("/api/v1/users/requests", headers=dict(Authorization="Bearer " + token),
                                        data = json.dumps(self.request))
        print (response)
        self.assertTrue(response.headers)

    def test_api_for_user_read_request(self):
        #test endpoint for user to view requests
        response = self.client().get('/api/v1/users/requests')
        self.assertEquals(response.status_code,200)

    def test_api_to_view_a_request(self):
        #test api to view request
        response = self.client().get('/api/v1/users/requests/1')
        self.assertEquals(response.status_code, 200)

    def test_api_to_update_a_request(self):
        #test api to update a request
        response = self.client().put("/api/v1/users/requests", data = json.dumps(self.request),
                    content_type='application/json')
        self.assertTrue(response.status_code)

    def test_api_to_delete_a_request(self):
        #test api to delete a request
        response = self.client().delete('/api/v1/users/requests/1')
        self.assertTrue(response.status_code)


if __name__ == "__main__":
    unittest.main()