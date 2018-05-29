import json
from models import Request


def create_request(date, title, location, priority, description):

    request = Request(date, title, location, priority, description)
    request_dict = {"date":request.date, "title":request.title, "location":request.location,
                "priority":request.priority, "description":request.description}

    all_requests = open("requests.txt", "w")
    requests_list = json.dumps(request_dict)

    all_requests.write(requests_list)
    all_requests.close()


if __name__ == "__main__":
    date = input("Enter date: ")
    title = input("Enter title: ")
    location = input("Enter location: ")
    priority = input("Enter priority. Must be High, Medium or Low: ")
    description = input("Enter description: ")

    create_request(date, title, location, priority, description)