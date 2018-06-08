import psycopg2
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

    def __init__(self, request_id, date, title, location, priority, description, status, created_by):
        self.request_id = request_id
        self.date = date
        self.title = title
        self.location = location
        self.priority = priority
        self.description = description
        self.status = status
        self.created_by = created_by

    def __str__(self):
        return '<User: {}+" "+{}>'.format(self.title, self.description)