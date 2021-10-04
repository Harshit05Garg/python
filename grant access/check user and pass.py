def show_records():
    record = open("record.txt", "r")
    for line in record.readlines():
        print(line, end="")
    record.close()
    return


def employee_creation():
    show_records()
    employee = []
    password = []
    record = open("record.txt", "a")
    while True:
        employee.append(input("Enter the new employee's name: "))
        password.append(input("Enter the new password name: "))
        print(employee[-1])
        record.write(employee[-1] + " - " + password[-1] + "\n")
        print(password[-1])
        close = input("Do you want to close the program (Y/n): ")
        if close.lower() == "y":
            record.close()
            return


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