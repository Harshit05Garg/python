employee = []
password = []
with open("record.txt", "r") as record:
    for line in record.readlines():
        employee.append(line.split(" - ")[0])
        password.append(line.split(" - ")[1][:-1])


def show_records():
    for name in employee:
        print(name)
    return


def employee_creation():
    show_records()
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


def check_user_and_pass(username, password_input):
    admin_username = "kaku"
    admin_password = "harsh"
    if username == admin_username and password_input == admin_password:
        return True, "Admin"
    else:
        try:
            if password[employee.index(username)] == password_input:
                return True, "Guest"
            else:
                return False, "Guest"
        except ValueError:
            return False, "Invalid user"
