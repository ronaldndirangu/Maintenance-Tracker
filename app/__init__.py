from flask import Flask
from instance.config import app_config


# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	return app

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

app = create_app("development")