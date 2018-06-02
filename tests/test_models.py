import os
import unittest
from app.models import User, Request


class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User(1, 'Ron', 'Ndirangu', 'ron@gmail.com', 'rrrrnnnn')
        self.request = Request(1, '12/1/2018', "Replace Motor", "Liquid Plant",	"High",
			         "Motor overheating due to unbalanced windings","pending","John")

    def test_user_model(self):
        self.assertEqual(self.user.user_id, 1)
        self.assertEqual(self.user.firstname, 'Ron')
        self.assertEqual(self.user.lastname, 'Ndirangu')
        self.assertEqual(self.user.email, 'ron@gmail.com')
        self.assertEqual(self.user.password, 'rrrrnnnn')

    def test_request_model(self):
        self.assertEqual(self.request.request_id, 1)
        self.assertEqual(self.request.date, '12/1/2018')
        self.assertEqual(self.request.title, 'Replace Motor')
        self.assertEqual(self.request.location, "Liquid Plant")
        self.assertEqual(self.request.priority, 'High')
        self.assertEqual(self.request.description, 'Motor overheating due to unbalanced windings')
        self.assertEqual(self.request.status, 'pending')
        self.assertEqual(self.request.created_by, 'John')
