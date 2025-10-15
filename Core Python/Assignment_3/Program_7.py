#7 Write a program to check if user has entered correct userid and password.
username = "user123"
password = "user@123"

enter_user = (input("Enter User Id :"))
enter_pass = (input("Enter Password Id :"))

if(username == enter_user and password == enter_pass):
    print("Login is Successfully...")
else:
    print("Incorrect username and password.Sorry try again")




