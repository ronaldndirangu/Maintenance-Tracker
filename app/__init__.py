from flask import Flask, Response, abort, request, jsonify
import json
from instance.config import app_config


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

# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	
	# Create new request
	@app.route("/api/v1/users/requests/", methods=["POST"])
	def create_request():
		if not request.json:
			abort(400)
		new_req = {
			"request_id":len(requests)+1,
			"date":request.json['date'],
			"title":request.json['title'],
			"location":request.json['location'],
			"priority":request.json['priority'],
			"description":request.json['description'],
			"status":request.json['status'],
			"created_by":request.json['created_by']
		}
		requests.append(new_req)
		return jsonify(new_req),201

	#View user requests for logged in user
	@app.route("/api/v1/users/requests", methods=["GET"])
	def user_requests():
		logged_in_user = 'John'
		user_req=[]
		for req in requests:
			if req["created_by"]==logged_in_user:
				user_req.append(req)
		user_requests = json.dumps(user_req)
		resp = Response(user_requests, status=200, mimetype='application/json')
		return resp


	#View a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["GET"])
	def get_request(id):
		logged_in_user = 'John'
		user_req=[]
		for req in requests:
			if req["created_by"]==logged_in_user and int(req["request_id"])==id:
				user_req.append(req)
		user_request = json.dumps(user_req)
		resp = Response(user_request, status=200, mimetype="application/json")
		return resp

	# Update a specific request
	@app.route("/api/v1/users/requests/<int:id>/", methods=["POST"])
	def update_request(id):
		update_request = [request for request in requests if int(request['id'])==id]
		if len(update_request) == 0:
			abort(404)
		if not request.json:
			abort(400)  

		update_request['title'] = request.json.get('title', update_request['title'])
		update_request['description'] = request.json.get('description', update_request['description'])
		update_request['type'] = request.json.get('type', update_request['type'])
		return jsonify({'update_request': update_request}), 201

	@app.route("/api/v1/users/login", methods=["POST"])
	def login():
		if request.json:
			for user in users:
				if user['email'] == request.json['email'] and user['password'] == request.json['password']:
					return jsonify({"login":"successful"}), 200
				else:
					return jsonify({"login":"failed"}), 401

	@app.route("/api/v1/users/signup", methods=["POST"])
	def signup():
		if request.json:
			new_user = {
				"user_id":len(users)+1,
				"firstname":request.json['firstname'],
				"lastname":request.json['lastname'],
				"email":request.json['email'],
				"password":request.json['password'],
				"password":request.json['password']
			}
			users.append(new_user)
			return jsonify(new_user), 201

	return app