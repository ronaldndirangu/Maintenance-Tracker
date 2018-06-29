import unittest
import json
from app import create_app


class TestRequests(unittest.TestCase):

  def setUp(self):
    # Initialize our variable before test
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.request = {
        "request_title": "Test_update request",
        "request_description": "Testing_update request",
        "request_location": "Test locationn",
        "request_priority": "High",
        "request_status": "Pending"
    }
    self.request_1 = {
        "request_title": "Test_update request",
        "request_description": "Testing_update request",
        "request_location": "Test locationn",
        "request_priority": "High",
        "request_status": "Pending"
    }
    
    self.user = {"username": 'admin', "email": 'admin@gmail.com',
                 "password": 'admin123', 'role': True}
    
    # Create test user
    response = self.client().post('/api/v2/auth/signup',
                                  data=json.dumps(self.user),
                                  content_type='application/json')
    self.assertEquals(response.status_code, 201)

    # Login test user created
    response = self.client().post('/api/v2/auth/login',
                                  data=json.dumps(dict(username="admin",
                                                  password="admin123")),
                                  content_type='application/json')
    data = json.loads(response.data.decode())

    self.assertTrue(data[0]['token'])
    self.assertEquals(response.status_code, 201)

    self.headers = {'token': data[0]['token']}
    print(self.headers)

    # Create user request 1
    response = self.client().post('/api/v2/users/requests',
                                  data=json.dumps(self.request),
                                  headers=self.headers,
                                  content_type='application/json')
    data = json.loads(response.data.decode())
    print(data)
    self.assertEquals(response.status_code, 201)

    # Create user request 2
    response = self.client().post('/api/v2/users/requests',
                                  data=json.dumps(self.request_1),
                                  headers=self.headers,
                                  content_type='application/json')
    data = json.loads(response.data.decode())
    print(data)
    self.assertEquals(response.status_code, 201)

  def test_view_all_requests(self):
    response = self.client().get('/api/v2/requests',
                                 headers=self.headers)
    self.assertEquals(response.status_code, 200)

  def test_admin_can_approve_request(self):
    response = self.client().put('/api/v2/requests/1/approve',
                                 headers=self.headers)
    data = json.loads(response.data.decode())
    print(data["message"])
    self.assertEquals(response.status_code, 200)

  def test_admin_can_disapprove_request(self):
    response = self.client().put('/api/v2/requests/2/disapprove',
                                 headers=self.headers)
    self.assertEquals(response.status_code, 200)

  def test_admin_can_resolve_request(self):
    response = self.client().put('/api/v2/requests/1/resolve',
                                 headers=self.headers)
    print(response)
    self.assertEquals(response.status_code, 200)

  def test_admin_promote_user(self):
    response = self.client().put('/api/v2/users/1/promote',
                                 headers=self.headers)
    self.assertEquals(response.status_code, 200)

  def test_admin_view_all_users(self):
    response = self.client().get('/api/v2/users',
                                 headers=self.headers)
    self.assertEquals(response.status_code, 200)

  def test_admin_view_user_details(self):
    response = self.client().get('/api/v2/users/1',
                                  headers=self.headers)
    self.assertEquals(response.status_code, 200)

  def test_admin_can_delete_user(self):
    response = self.client().delete('/api/v2/users/1',
                                  headers=self.headers)
    self.assertEquals(response.status_code, 200)



if __name__ == "__main__":
  unittest.main()
