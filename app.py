from flask import Flask, request, jsonify
from app import create_app, users, requests

app = Flask(__name__)

# Create new request
@app.route("/api/v1.0/users/requests/", methods=["POST"])
def create_request():
	if request.json:
		new_request = {
			"request_id": request.json.get('request_id', ''),
			"date": request.json.get('date', ''),
			"title": request.json.get('title', ''),
			"location": request.json.get('location', ''),
			"priority": request.json.get('priority', ''),
            "description": request.json.get('description', ''),
			"status": request.json.get('status', ''),
            "created_by": request.json.get("created_by", '')
		}
		requests.append(new_request)
		return jsonify({
			"request_id": new_request["request_id"],
			"date": new_request["date"],
            "title": new_request["title"],
            "location": new_request["location"],
			"priority": new_request["piority"],   
			"description": new_request["description"],
			"status": new_request["status"],
            "created_by": new_request["created_by", '']
		}), 201
	return app

#View user requests for logged in user
@app.route("/api/v1.0/users/requests/", methods=["GET"])
def user_requests():
    name = request.headers["name"]
    requests_by_user = []
    if name != 'admin':
        for req in requests:
            if req["created_by"] == "name":
                user_req = {
					"request_id": req["request_id"],
			        "date": req["date"],
			        "title": req["title"],
			        "location": req["location"],
                    "priority": req["priority"],
                    "description": req["description"],
			        "status": req["status"],
                    "created_by": req["created_by"]
		        } 
                requests_by_user.append(user_req)
        return jsonify(requests_by_user), 
    elif name == "admin":
        return jsonify(requests), 200
    return app

#View a specific request
@app.route("/api/v1.0/users/requests/<int:id>/", methods=["GET"])
def get_request(id):
	name = request.headers["name"]
	requests_by_user = []
	for req in requests:
		if req["created_by"] == name:
			if req["id"] == id:
				user_req = {
					"request_id": req["request_id"],
					"date": req["date"],
			        "title": req["title"],
			        "location": req["location"],
                    "priority": req["priority"],
                    "description": req["description"],
			        "status": req["status"],
                    "created_by": req["created_by"]
				}
				requests_by_user.append(user_req)
	return jsonify(requests_by_user), 200
	return app

# Update a specific request
@app.route("/api/v1.0/users/requests/<int:id>/", methods=["POST"])
def update_request(id):
	name = request.headers["name"]
	if name != "admin":
		for req in requests:
			if req["created_by"] == name:
				if req["id"] == id:
					req["title"] = request.json.get('title'),
					req["description"] = request.json.get('description'),
					req['location'] = request.json.get('location')
				return jsonify({
					"request_id": req["request_id"],
					"date": req["date"],
                    "title": req["title"],
                    "location": req["location"],
                    "priority": req["priority"],
                    "description": req["description"],
                    "status": req["status"],
                    "created_by": req["created_by"]
                    }), 200
			else:
				if name == "admin":
					for req in requests:
						if req["id"] == id:
							req["status"] = request.json.get('status')
					return jsonify({
						"message": "Update"
					})
		return app