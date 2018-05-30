import json
from models import User


def register(firstname, lastname, email, password):

    user = User(firstname, lastname, email, password)   
    #Append user detail dictionary into users list
    user_dict ={"firstname":user.firstname, "lastname":user.lastname,
                "email":user.email, "password":user.password}

    #Dump users into text file users.txt
    all_users = open("users.txt", "w")
    users_list = json.dumps(user_dict)

    all_users.write(users_list)
    all_users.close()

def login(email, password):
    all_users = open("users.txt", "r")
    datastore = json.load(all_users)
    if email == datastore["email"] and password==datastore["password"]:
        print ("Login Successful")


if __name__ == "__main__":
    choice = input("Enter 1 to register or 2 to login:")
    if choice == '1':
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        email = input("Enter your email: ")
        
        if '@' not in email and '.' not in email:
            raise ValueError("Enter a valid email address: ")

        password = input("Enter your password: ")

        if len(password) < 8:
            raise ValueError("The password should be atleast 8 characters long")

        register(firstname, lastname, email, password)

    elif choice == '2':
        email = input("Enter your email: ")
        password = input("Enter your password")

        login(email, password)

    else:
        print ("Please enter a valid choice")
