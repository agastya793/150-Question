''' Login Validation System
 Task:

Check username and password'''

def login(user,pwd):
    if user == "admin" and pwd == "1234":
        return "login successful"
    else:
        return "Invalid Credentials"
    
print(login("admin","1234"))
        