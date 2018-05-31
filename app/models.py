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

users = [{"user_id": '1', "firstname": "Ron", "lastname": "Ndi", 
		"email": "ron.ndi@gmail.com","password": 'rrrrnnnn'	},
		{"user_id": '2', "firstname": "Trev","lastname": "Kar", 
		"email": "trev.kar@gmail.com","password": 'ttttkkkk'},
		]

requests = [{"request_id":1,"date": '12/1/2018',"title": "Replace Motor",
			"location": "Liquid Plant",	"priority":"High",
			"description": "Motor overheating due to unbalanced windings",
			"status":"pending",
			"created_by":"John"},
			{"request_id":2,"date": '12/1/2018',"title": "Replace Sensor",
			"location": "Soap Plant","priority":"Medium",
			"description": "Sensor misbehaving needs replacement",
			"status":"approved",
			"created_by":"Mary"},
			]