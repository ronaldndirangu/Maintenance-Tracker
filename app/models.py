import psycopg2

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
cur = conn.cursor()

class User():
    def __init__(self):
        pass

    def create_user(self, username, email, password, role=False):
        sql = "INSERT INTO users (username, email, password, role)\
                            VALUES (%s, %s, %s, %s)"
        data = (username, email, password, role)
        cur.execute(sql, data)
                    
        conn.commit()
        cur.close()
        print ("New user added to user table")

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