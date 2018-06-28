from flask import Flask, abort, request, jsonify
from instance.config import app_config, SECRET_KEY
from app.models import User, Request
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from validate_email import validate_email


Users = User()
Requests = Request()

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

            else:
                token = request.headers.get('token')

            if not token:
                return jsonify({'message': 'token is missing'}), 401

            try:
                data = jwt.decode(token, SECRET_KEY)
                kwargs['current_user_id'] = data['user_id']
            except:
                return jsonify({'message': 'Invalid token'}), 401
            return f(*args, **kwargs)
        return decorated

    # Sign up user
    @app.route("/api/v2/auth/signup", methods=["POST"])
    def signup():
        if request.json:
            print(request.json)
            new_user = {
                "username": request.json['username'],
                "email": request.json['email'],
                "password": request.json['password']
            }

            users = Users.get_all_users()
            all_users = []
            for user in users:
                all_users.append(user[0])

            for values in new_user.values():
                if values=="":
                    return jsonify({'message':'Please fill all fields'})
            
            if new_user['username'] in all_users:
                return jsonify({'message': 'User already registered'}), 201

            if len(request.json['password']) < 6:
                return jsonify({'message':
                                'Password should be atleast 6 characters'})
            elif not validate_email(request.json['email']):
                return jsonify({'message': 'Enter valid email'})

            hashed_pswd = generate_password_hash(new_user['password'])

            Users.create_user(
                new_user['username'], new_user['email'],
                hashed_pswd)
            return jsonify({'message': 'User created successfully'}), 201

    # User can login using email and password
    @app.route("/api/v2/auth/login", methods=["POST"])
    def login():
        if request.json:
            username = request.json["username"]
            password = request.json["password"]
        
        if username=="" or password=="":
            return jsonify({'message':'Please fill all fields'})

        users = Users.login(username, password)
        if users:
            for user in users:
                if user['username'] == username and check_password_hash(user['password'], password):
                    token = jwt.encode({"user_id": user['user_id'], 'exp': datetime.datetime.utcnow(
                    ) + datetime.timedelta(minutes=30)}, SECRET_KEY)
                    role = Users.get_role(user['user_id'])[0][0]
                    return jsonify({'token': token.decode('UTF-8')},
                             {'message':'Login successful'}, {'role':role}), 201
        return jsonify({"message": "no valid user"}), 401

    # Create new request
    @app.route("/api/v2/users/requests", methods=["POST"])
    @login_required
    def create_request(current_user_id):
        if not request.json:
            abort(404)
        req = {
            "request_title": request.json['request_title'],
            "request_description": request.json['request_description'],
            "request_location": request.json['request_location'],
            "request_priority": request.json['request_priority'],
            "request_status": "Pending",
            "requester_id": current_user_id
        }

        for values in req.values():
            if values == "":
                return jsonify({'message':'Please fill all fields'})

        requests = Requests.get_user_requests(current_user_id)
        titles = [request['request_title'] for request in requests]
        desc = [request['request_description'] for request in requests]
        if req['request_title'] in titles and req['request_description'] in desc:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            return jsonify({'message': 'Failed, Request already made'}), 201                                                                                                                                                                                                                                                                                                            
        Requests.create_request(req['request_title'], req['request_description'],
                                req['request_location'], req['request_priority'],
                                req['request_status'], req['requester_id'])
        return jsonify({'message': 'Request created successfully'}), 201                                                                                                                                                                            

    # View user requests for logged in user
    @app.route(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     "/api/v2/users/requests", methods=["GET"])
    @login_required
    def user_requests(current_user_id):
        user_req = Requests.get_user_requests(current_user_id)
        return jsonify(user_req), 200

    # View a specific request
    @app.route("/api/v2/users/requests/<int:id>", methods=["GET"])
    @login_required
    def get_request(current_user_id, id):
        req_id = int(id)
        request = Requests.get_a_request(req_id)
        if request:
            if request[0]['requester_id'] == current_user_id or Users.get_role(current_user_id)[0][0]:
                return jsonify(request), 200
            return jsonify({'message': 'Not authorized to view request'})
        return jsonify({'message': 'Request not found'}), 200

    # Update a specific request
    @app.route("/api/v2/users/requests/<int:id>", methods=["PUT"])
    @login_required
    def update_request(current_user_id, id):
        if not request.json:
            abort(404)
        title = request.json['request_title']
        description = request.json['request_description']
        location = request.json['request_location']

        if title=="" or description=="" or location=="":
            return jsonify({'message':'Please fill all fields'})

        message = Requests.update_a_request(id, title, description, location)
        if message:
            return jsonify(message), 201
        else:
            return ({'message': 'update failed'})

    # Delete a specific request
    @app.route("/api/v2/users/requests/<int:id>", methods=["DELETE"])
    @login_required
    def delete_request(current_user_id, id):
        req = Requests.get_a_request(int(id))
        if len(req) < 1:
            return jsonify({'message': 'request not found'})
        else:
            del_id = int(id)
            message = Requests.delete_a_request(del_id)
            print (message)
            if message:
                return jsonify(message), 200
            else:
                return jsonify({'message': 'deleting failed'})

    # Admin can view all requests
    @app.route("/api/v2/requests")
    @login_required
    def get_all_requests(current_user_id):
        if Users.get_role(current_user_id)[0][0]:
            req = Requests.get_all_requests()
            print (req)
            if len(req) > 0:
                return jsonify(req), 200
            return jsonify({'message': 'no requests found'})
        return jsonify({'message': 'Only allowed for the admin'})

    # Approve a request
    @app.route("/api/v2/requests/<int:id>/approve", methods=["PUT"])
    @login_required
    def approve_request(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            status_list = Requests.get_status(id)
            print(status_list)
            if len(status_list) == 0:
                return jsonify({'message':'No request found'}), 200
            status = status_list[0][0].lower()
            if status == "pending":
                message = Requests.approve(id)
                return jsonify(message), 200
            elif status == 'disapproved':
                return jsonify({'message':'Request already disapproved'})
            return jsonify({'message': 'Request has already been reviewed'})
        return jsonify({'message': 'Only allowed for the admin'})

    # Dissapprove a request
    @app.route("/api/v2/requests/<int:id>/disapprove", methods=["PUT"])
    @login_required
    def disapprove_request(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            status_list = Requests.get_status(id)
            print(status_list)
            if len(status_list) == 0:
                return jsonify({'message':'No request found'}), 200
            status = status_list[0][0].lower()
            print (status)
            if status == "pending":
                message = Requests.disapprove(id)
                return jsonify(message), 201
            elif status == 'approved':
                return jsonify({'message':'Request already approved'})
            return jsonify({'message': 'Request has already been reviewed'})
        return jsonify({'message': 'Only allowed for the admin'})

    # Resolve a request
    @app.route("/api/v2/requests/<int:id>/resolve", methods=["PUT"])
    @login_required
    def resolve_request(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            status_list = Requests.get_status(id)
            if len(status_list) == 0:
                return jsonify({'message':'No request found'}), 200
            status = status_list[0][0].lower()
            print (status)
            if status == "approved":
                message = Requests.resolve(id)
                return jsonify(message), 201
            return jsonify({'message': 'Request has already been reviewed'})
        return jsonify({'message': 'Only allowed for the admin'})

    # Promote user to admin
    @app.route("/api/v2/users/<int:id>/promote", methods=["PUT"])
    @login_required
    def promote_user(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            message = Users.promote_user(id)
            return jsonify(message), 200
        else:
            return jsonify({"message": "Only allowed for the admin"}), 200

    # View all users
    @app.route("/api/v2/users", methods=["GET"])
    @login_required
    def get_users(current_user_id):
        if Users.get_role(current_user_id)[0][0]:
            users = Users.show_users()
            return jsonify(users), 200
        else:
            return jsonify({"message": "Only allowed for the admin"}), 200

    # View user details
    @app.route("/api/v2/users/<int:id>", methods=["GET"])
    @login_required
    def get_user(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            user = Users.get_user(id)
            print(user)
            return jsonify(user), 200
        else:
            return jsonify({"message":"No user found"}), 200
            
    # Delete a user
    @app.route("/api/v2/users/<int:id>", methods=["DELETE"])
    @login_required
    def delete_user(current_user_id, id):
        if Users.get_role(current_user_id)[0][0]:
            message = Users.delete_user(id)
            return jsonify(message), 200
        else:
            return jsonify({"message":"No user found"}), 200

    return app
