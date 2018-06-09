from flask import Flask, Response, abort, request, jsonify, make_response
import json
from instance.config import app_config, SECRET_KEY
from app.models import User, Request
import jwt
import datetime
from functools import wraps


Users= User()
Requests= Request()

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
				kwargs['current_user_id']=data['user_id']
	
			except:
				return jsonify({'message':'Invalid token'}), 401
			return f(*args, **kwargs)
		return decorated


	#Sign up user
	@app.route("/api/v1/users/signup", methods=["POST"])
	def signup():
		if request.json:
			new_user = {
						"username":request.json['username'],
						"email":request.json['email'],
						"password":request.json['password'],
						"role":request.json['role']
					}
			Users.create_user(new_user['username'], new_user['email'], new_user['password'], new_user['role'])
			return jsonify({'message':'User created successfully'}), 201

	#User can login using email and password
	@app.route("/api/v1/users/login", methods=["POST"])
	def login():
		if request.json:
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
	@login_required
	def create_request(current_user_id):
		if not request.json:
			abort(404)		
		req = {
			"request_title":request.json['request_title'],
			"request_description":request.json['request_description'],
			"request_location":request.json['request_location'],
			"request_priority":request.json['request_priority'],			
			"request_status":request.json['request_status'],
			"requester_id":current_user_id
		}
		
		Requests.create_request(req['request_title'], req['request_description'], req['request_location'], 
								req['request_priority'], req['request_status'],	req['requester_id'])
		return jsonify({'message':'Request created successfully'}), 201

	#View user requests for logged in user
	@app.route("/api/v1/users/requests", methods=["GET"])
	@login_required
	def user_requests(current_user_id):
		user_req = Requests.get_user_requests(current_user_id)
		return jsonify(user_req), 200
		

	#View a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["GET"])
	@login_required
	def get_request(current_user_id, id):
		req_id = int(id)
		request = Requests.get_a_request(req_id)
		if request[0]['requester_id'] == current_user_id:
			return jsonify(request), 200
		return jsonify({'message':'Not authorized to view request'})

	# Update a specific request
	@app.route("/api/v1/users/requests/<int:id>", methods=["PUT"])
	@login_required
	def update_request(current_user_id, id):
		if not request.json:
			abort(404)
		title = request.json['request_title']
		description = request.json['request_description']
		priority = request.json['request_priority']
		message = Requests.update_a_request(id, title, description, priority)
		if message:
			return jsonify(message)
		else:
			return ({'message':'update failed'})

	#Admin can view all requests
	@app.route("/api/v1/requests")
	@login_required
	def get_all_requests(current_user_id):
		if Users.get_role(current_user_id):
			req = Requests.get_all_requests()
			if req[0]:
				return jsonify(req), 200
			return jsonify({'message':'no requests found'})
		return jsonify({'message', 'Not admin'})

	# Approve a request
	@app.route("/api/v1/requests/<int:id>/approve", methods=["PUT"])
	def approve_request(id):
		status_list = Requests.get_status(id)
		status = status_list[0][0]
		print (status)
		if status == "Pending":
			message = Requests.approve(id)
			return jsonify(message)
		return jsonify({'message':'Request has already been reviewed'})

	# Dissapprove a request
	@app.route("/api/v1/requests/<int:id>/disapprove", methods=["PUT"])
	def disapprove_request(id):
		status_list = Requests.get_status(id)
		status = status_list[0][0]
		print (status)
		if status == "Pending":
			message = Requests.disapprove(id)
			return jsonify(message)
		return jsonify({'message':'Request has already been reviewed'})

	# Resolve a request
	@app.route("/api/v1/requests/<int:id>/resolve", methods=["PUT"])
	def resolve_request(id):
		status_list = Requests.get_status(id)
		status = status_list[0][0]
		print (status)
		if status == "Pending":
			message = Requests.resolve(id)
			return jsonify(message)
		return jsonify({'message':'Request has already been reviewed'})

	return app