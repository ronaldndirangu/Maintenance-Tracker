class User:

    def __init__(self, user_id, firstname, lastname, email, password):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __str__(self):
        return '<User: {}+" "+{}>'.format(self.firstname, self.lastname)  

class Request:

    def __init__(self, date, title, location, priority, description, status, created_by):
        self.date = date
        self.title = title
        self.location = location
        self.priority = priority
        self.description = description
        self.status = status
        self.created_by = created_by

    def __str__(self):
        return '<User: {}+" "+{}>'.format(self.title, self.description)