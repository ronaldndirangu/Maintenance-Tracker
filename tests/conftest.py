import pytest
from API import create_app

class User():

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

class Request():

    def __init__(self, date, title, location, priority, description):
        self.date = date
        self.title = title
        self.location = location
        self.priority = priority
        self.description = description



@pytest.fixture(scope="module")
def new_user():
    user = User("Ronald", "Ndirangu", "ron@gmail.com", "rrrrnnnn")
    return user

@pytest.fixture(scope="module")
def new_request():
    new_req = Request("15/04/2018", "Repair Motor", "Liquid Plant",
                     "High", "Motor overheating due to unbalanced windings")
    return new_req

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("flask_test.cfg")

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client # this is where the testing happens!
    ctx.pop()
