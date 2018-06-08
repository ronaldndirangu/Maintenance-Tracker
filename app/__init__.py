from flask import Flask, Response, abort, request, jsonify, make_response
import json
from instance.config import app_config, SECRET_KEY
from app.models import User, Request
import jwt
import datetime
from functools import wraps


Users= User()
Requests= Request()
users=[]
requests = []

# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	
	def login_required(f):
		@wraps(f)
		def decorated(*args, **kwargs):
			token = None

			if 'x-access-token' in request.headers:
				token = request.headers['x-access-token']
			
			if not token:
				return jsonify({'message':'token is missing'}), 401
			
			try:
				data = jwt.decode(token, SECRET_KEY)
				users = Users.get_user(data['user_id'])
				for user in users:
					current_user = jsonify(user)
					return current_user
			except:
				return jsonify({'message':'Invalid token'}), 401
			return f(current_user, *args, **kwargs)
		return decorated


	#Sign up user
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
				if user['username'] == username and user['password'] == password:
					token = jwt.encode({"user_id" : user['user_id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
					return jsonify({'token':token.decode('UTF-8')}), 200
		return jsonify({"message":"no valid user"}), 401

	# Create new request
	@app.route("/api/v1/users/requests", methods=["POST"])
	def create_request():
		if not request.json:
			abort(404)		
		req = {
			"request_title":request.json['request_title'],
			"request_description":request.json['request_description'],
			"request_location":request.json['request_location'],
			"request_priority":request.json['request_priority'],			
			"request_status":request.json['request_status'],
			"requester_id":request.json['requester_id']
		}
		Requests.create_request(req['request_title'], req['request_description'], req['request_location'], 
								req['request_priority'], req['request_status'],	req['requester_id'])
		return jsonify({'message':'Request created successfully'}), 201

	#View user requests for logged in user
	@app.route("/api/v1/users/requests", methods=["GET"])
	def user_requests():
		requests = Requests.get_all_requests()
		if requests:
			return jsonify(requests), 200
		return jsonify({'message':'no requests found'})


	#View a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["GET"])
	def get_request(id):
		req_id = int(id)
		requests = Requests.get_a_request(req_id)
		if requests:
			return jsonify(requests), 200
		return jsonify({'message':'no requests found'})

	# Update a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["PUT"])
	def update_request(id):
		pass


	# Approve a request
	@app.route("/api/v1/users/requests/<int:id>/approve", methods=["PUT"])
	def approve_request(id):
		pass

	# Dissapprove a request
	@app.route("/api/v1/users/requests/<int:id>/dissaprove", methods=["PUT"])
	def disapprove_request(id):
		pass

	# Resolve a request
	@app.route("/api/v1/users/requests/<int:id>/resolve", methods=["PUT"])
	def resolve_request(id):
		pass

	return app