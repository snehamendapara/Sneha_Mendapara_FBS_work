""" 8 Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha) """

import random
username = "user1234"
password = "user@123"

enter_username = input("Enter username : ")
enter_password = input("Enter password : ")



if(username == enter_username and password == enter_password):
    captcha = random.randint(1111 , 9999)
    print(f"captcha : {captcha}")

    user_captcha = int(input("Enter the same captcha : ")) 
    if(captcha == user_captcha):
        print("Successfully Login...")
    else:
        print("please enter same captcha")
else:
    print("Invalid user id")

