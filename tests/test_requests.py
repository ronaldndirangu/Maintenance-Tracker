import unittest
import json
from app import create_app


class TestRequests(unittest.TestCase):

        def setUp(self):
            # Initialize our variable before test
            self.app = create_app("testing")
            self.client = self.app.test_client
            self.request = {
                "request_title": "Test_update_3 request",
                "request_description": "Testing_update_3 request",
                "request_location": "Test locationn_3",
                "request_priority": "High",
                "request_status": "Pending"
            }
            self.user = {"username": 'test', "email": 'test@gmail.com',
                         "password": 'test123'}
            # Create test user
            response = self.client().post('/api/v2/auth/signup',
                                          data=json.dumps(self.user),
                                          content_type='application/json')
            self.assertEquals(response.status_code, 201)

            # Login test user created
            response = self.client().post('/api/v2/auth/login',
                                          data=json.dumps(self.user),
                                          content_type='application/json')
            data = json.loads(response.data.decode())

            self.assertTrue(data[0]['token'])
            self.assertEquals(response.status_code, 201)

            self.headers = {'token': data[0]['token']}

            # Create user request
            response = self.client().post('/api/v2/users/requests',
                                          data=json.dumps(self.request),
                                          headers=self.headers,
                                          content_type='application/json')
            self.assertEquals(response.status_code, 201)

            # create request
            response = self.client().post("/api/v2/users/requests",
                                          data=json.dumps(self.request),
                                          headers=self.headers,
                                          content_type='application/json')
            self.assertEquals(response.status_code, 201)

        def test_api_for_user_create_request(self):
            response = self.client().post("/api/v2/users/requests",
                                          data=json.dumps(self.request),
                                          headers=self.headers,
                                          content_type='application/json')
            print(self.headers['token'])
            self.assertEquals(response.status_code, 201)

        def test_api_for_user_read_all_request(self):
            # test endpoint for user to view requests
            response = self.client().get("/api/v2/users/requests",
                                         headers=self.headers)
            print(self.headers['token'])
            self.assertEquals(response.status_code, 200)

        def test_api_to_view_a_request(self):
            # test api to view request
            response = self.client().get("/api/v2/users/requests/1",
                                         headers=self.headers)
            print(self.headers['token'])
            self.assertEquals(response.status_code, 200)

        def test_api_to_update_a_request(self):
            # test api to update a request
            response = self.client().put("/api/v2/users/requests/1",
                                         data=json.dumps(self.request),
                                         headers=self.headers,
                                         content_type='application/json')
            self.assertEquals(response.status_code, 201)

        def test_api_to_delete_a_request(self):
            # test api to delete a request
            response = self.client().delete('/api/v2/users/requests/1',
                                            headers=self.headers)
            self.assertEquals(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
