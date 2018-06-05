from flask import Flask, Response, abort, request, jsonify
import json
from instance.config import app_config

# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")
	return app

app = create_app('development')