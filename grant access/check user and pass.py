def check_user_and_pass():
    admin_username = "kaku"
    admin_password = "harsh"
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == admin_username and password == admin_password:
        print("Correct")
    else:
        print("Invalid username or password")
check_user_and_pass()