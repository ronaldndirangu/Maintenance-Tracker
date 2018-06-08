import psycopg2
import datetime
from flask import jsonify
from instance.config import SECRET_KEY

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")


class User():
    def __init__(self):
        pass

    def create_user(self, username, email, password, role=False):
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

class Request:

    def __init__(self):
        pass

    def create_request(self, request_title, request_description, request_location,
                            request_priority, request_status, requester_id):
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

    def get_all_requests(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests;")
        columns = ('request_id','request_date', 'request_title', 'request_description', 
                    'request_location', 'request_priority', 'request_status', 'requester_id')
        requests = []
        for request in cur.fetchall():
            print (request)
            requests.append(dict(zip(columns, request)))
        return requests

    def get_a_request(self, id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests WHERE request_id = (%s)", [id])
        columns = ('request_id','request_date', 'request_title', 'request_description', 
                    'request_location', 'request_priority', 'request_status', 'requester_id')
        requests = []
        for request in cur.fetchall():
            print (request)
            requests.append(dict(zip(columns, request)))
        return requests

    def update_a_request(self, id, title, description):
        pass
        
        
