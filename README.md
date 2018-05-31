# Maintenance-Tracker
An application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

To run the application follow this steps on the root directory:
  1. Enable your virtual environment
  2. run: pip install -r requirements.txt in your shell.
  3. Test the following endpoints using postman or curl:
      a)GET http://127.0.0.1/api/v1/users/requests/
      b)POST http://127.0.0.1/api/v1/users/requests/
      c)GET http://127.0.0.1/api/v1/users/requests/1
      d)POST http://127.0.0.1/api/v1/users/requests/1
  4. To run test on for the endpoint install pytest using pip and run pytest -v
