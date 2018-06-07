from flask import Flask, Response, abort, request, jsonify
import json
from instance.config import app_config, SECRET_KEY
from app.models import User
import jwt
import datetime


Users= User()
users=[]
requests = []

# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	
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
	@app.route("/api/v1/users/requests/<int:id>", methods=["POST"])
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

	#User can login using email and password
	@app.route("/api/v1/users/login", methods=["GET"])
	def login():
		if request.authorization:
			username = request.authorization["username"]
			password = request.authorization["password"]
		elif request.json:
			username = request.json["username"]
			password = request.json["password"]
		
		users = Users.login(username, password)
		if users:
			for user in users:
				print (user)
				if user['username'] == username and user['password'] == password:
					token = jwt.encode({"username" : "username", 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
					return jsonify({'token':token.decode('UTF-8')}), 200
		return jsonify({"message":"no valid user"}), 401

	@app.route("/api/v1/users/signup", methods=["POST"])
	def signup():
		if request.json:
			new_user = {
						"username":request.json['username'],
						"email":request.json['email'],
						"password":request.json['password']
					}
			Users.create_user(new_user['username'], new_user['email'], new_user['password'])
			return jsonify({'message':'User created successfully'}), 201

	return app