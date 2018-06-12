import os
import psycopg2
import datetime
from flask import jsonify
from instance.config import SECRET_KEY

conn = psycopg2.connect(
            host=os.getenv("HOST"), database=os.getenv("DATABASE"),
            user=os.getenv("USER"), password=os.getenv("PASSWORD"))


class User():
    def __init__(self):
        pass

    def create_user(self, username, email, password, role):
        cur = conn.cursor()
        sql = "INSERT INTO users (username, email, password, role)\
                            VALUES (%s, %s, %s, %s)"
        data = (username, email, password, role)
        cur.execute(sql, data)

        conn.commit()
        cur.close()
        print ("New user added to user table")

    def login(self, name, pswd):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = (%s)", [name])
        columns = ('user_id', 'username', 'email', 'password', 'role')
        users = []
        for user in cur.fetchall():
            users.append(dict(zip(columns, user)))
        return users

    def get_user(self, id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = (%s)", [id])
        columns = ('user_id', 'username', 'email', 'password', 'role')
        users = []
        for user in cur.fetchall():
            users.append(dict(zip(columns, user)))
        return users

    def get_role(self, id):
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE user_id = (%s)", [id])
        roles = []
        for role in cur.fetchall():
            roles.append(role)
        return roles

    def get_all_users(self):
        cur = conn.cursor()
        cur.execute("SELECT username FROM users")
        users = []
        for user in cur.fetchall():
            users.append(user)
        return users


class Request:

    def __init__(self):
        pass

    def create_request(self, request_title, request_description,
                       request_location, request_priority, request_status,
                       requester_id):
        cur = conn.cursor()
        sql = "INSERT INTO requests(request_date, request_title, request_description, request_location,\
                                    request_priority, request_status, requester_id)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s);"
        date = datetime.datetime.now()
        data = (date, request_title, request_description, request_location,
                request_priority, request_status, requester_id)
        cur.execute(sql, data)

        conn.commit()
        cur.close()

        print ("New request added to user table")

    def get_user_requests(self, id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests WHERE requester_id = (%s)", [id])
        columns = ('request_id', 'request_date', 'request_title',
                   'request_description', 'request_location',
                   'request_priority', 'request_status', 'requester_id')
        requests = []
        for request in cur.fetchall():
            requests.append(dict(zip(columns, request)))
        return requests

    def get_a_request(self, id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests WHERE request_id = (%s)", [id])
        columns = ('request_id', 'request_date', 'request_title',
                   'request_description', 'request_location',
                   'request_priority', 'request_status', 'requester_id')
        requests = []
        for request in cur.fetchall():
            print (request)
            requests.append(dict(zip(columns, request)))
        return requests

    def update_a_request(self, id, title, description, priority):
        cur = conn.cursor()
        sql = "UPDATE requests SET request_title=(%s), request_description=(%s),\
                 request_priority=(%s) WHERE request_id = (%s)"
        data = (title, description, priority, id)
        cur.execute(sql, data)
        return {'message': 'request updated successfully'}

    def delete_a_request(self, id):
        cur = conn.cursor()
        cur.execute("DELETE from requests WHERE request_id=(%s)", [id])
        conn.commit()
        return {'message': 'request deleted'}

    def get_all_requests(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests;")
        columns = ('request_id', 'request_date', 'request_title',
                   'request_description', 'request_location',
                   'request_priority', 'request_status', 'requester_id')
        requests = []
        for request in cur.fetchall():
            requests.append(dict(zip(columns, request)))
        return requests

    def get_status(self, id):
        cur = conn.cursor()
        cur.execute(
            "SELECT request_status FROM requests WHERE request_id = (%s)", [id])
        status = []
        for s in cur.fetchall():
            status.append(s)
        return status

    def approve(self, id):
        cur = conn.cursor()
        sql = "UPDATE requests SET request_status=(%s) WHERE request_id=(%s)"
        data = ("Approved", id)
        cur.execute(sql, data)
        return {'message': 'request approved'}

    def disapprove(self, id):
        cur = conn.cursor()
        sql = "UPDATE requests SET request_status=(%s) WHERE request_id=(%s)"
        data = ('Disapproved', id)
        cur.execute(sql, data)
        return {'message': 'request rejected'}

    def resolve(self, id):
        cur = conn.cursor()
        sql = "UPDATE requests SET request_status=(%s) WHERE request_id=(%s)"
        data = ('Resolved', id)
        cur.execute(sql, data)
        return {'message': 'request resolved'}
