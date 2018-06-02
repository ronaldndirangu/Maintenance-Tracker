import os
import unittest
from app.models import User, Request


class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User(1, 'Ron', 'Ndirangu', 'ron@gmail.com', 'rrrrnnnn')

    def test_user_model(self):
        self.assertEquals(self.user.user_id, 1)
        self.assertEquals(self.user.firstname, 'Ron')
        self.assertEquals(self.user.lastname, 'Ndirangu')
        self.assertEquals(self.user.email, 'ron@gmail.com')
        self.assertEquals(self.user.password, 'rrrrnnnn')
