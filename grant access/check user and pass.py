def employee_creation():
    employee = []
    password = []
    while True:
        employee.append(input("Enter the new employee's name: "))
        password.append(input("Enter the new password name: "))
        print(employee[-1])
        print(password[-1])


def check_user_and_pass():
    admin_username = "kaku"
    admin_password = "harsh"
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == admin_username and password == admin_password:
        print("Correct")
        employee_creation()
    else:
        print("Invalid username or password")


check_user_and_pass()