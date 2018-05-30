class User:

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


class Request:

    def __init__(self, date, title, location, priority, description):
        self.date = date
        self.title = title
        self.location = location
        self.priority = priority
        self.description = description
