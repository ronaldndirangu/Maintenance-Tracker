from flask import Flask, Response, abort, request, jsonify
import json
from instance.config import app_config

requests = []
users = []


# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	
	#Home Page
	@app.route('/')
	def home():
		return "You are at the home page"
		
	# Create new request
	@app.route("/api/v1/users/requests", methods=["POST"])
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
		return jsonify({'requests':requests}), 200 


	#View a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["GET"])
	def get_request(id):
		req = [request for request in requests if int(request['request_id'])==id]
		return jsonify(req), 200

	# Update a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["PUT"])
	def update_request(id):
		update_request = [request for request in requests if int(request['request_id'])==id]
		if len(update_request) == 0:
			abort(404)
		if not request.json:
			abort(400)  

		update_request[0]['title'] = request.json.get('title', update_request[0]['title'])
		update_request[0]['description'] = request.json.get('description', update_request[0]['description'])
		update_request[0]['priority'] = request.json.get('type', update_request[0]['priority'])
		return jsonify({'requests': requests}), True

	#Delete a specific user
	@app.route("/api/v1/users/requests/<int:id>", methods=["DELETE"])
	def del_request(id):
		for request in requests:
			if request["request_id"] == id:
				requests.remove(request)
			return jsonify({'requests':requests}), True

	#User can login using email and password
	@app.route("/api/v1/users/login", methods=["GET"])
	def login():
		if request.json:
			for user in users:
				if user['email'] == request.json['email'] and user['password'] == request.json['password']:
					return jsonify({"login":"successful"}), 200
			return jsonify({"login":"failed"}), 401

	#user can signup
	@app.route("/api/v1/users/signup", methods=["POST"])
	def signup():
		if request.json:
			new_user = {
				"user_id":len(users)+1,
				"firstname":request.json['firstname'],
				"lastname":request.json['lastname'],
				"email":request.json['email'],
				"password":request.json['password']
			}
			users.append(new_user)
			return jsonify(new_user), 201

	return app