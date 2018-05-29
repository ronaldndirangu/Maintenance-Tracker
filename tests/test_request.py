import unittest
from datetime import datetime

class TestRequest(unittest.TestCase):

    def test_request_date_valid(self):
        if request["date"].month == datetime.now().month and request["date"].year == datetime.now().year: 
            self.assertIs(request["date"].day, datetime.now().day)

    def test_title_not_null(self):
        self.assertNotEqual(request["title"], " ")

    def test_location_not_null(self):
        self.assertNotEqual(request["location"], " ")

    def test_priority_valid(self):
        self.assertIn(request["priority"], ['High','Medium','Low'])
        self.assertNotEqual(request["priority"], " ")

    def test_description_not_null(self):
        self.assertNotEqual(request["description"], " ")


if __name__ == "__main__":
    request = {"date":datetime.now(), "title":"Repair Motor", "location":"Liquid Plant",
                "priority":"High", "description":"Motor overheating due to unbalanced windings"}
    unittest.main()