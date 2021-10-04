import streamlit as st


def get_data():
    employee = []
    password = []
    with open("record.txt", "r") as record:
        for line in record.readlines():
            employee.append(line.split(" - ")[0])
            password.append(line.split(" - ")[1][:-1])
    return dict(zip(employee, password))


def employee_creation():
    record = open("record.txt", "a")
    new_employee = st.text_input("Enter the new employee's name: ")
    new_password = st.text_input("Enter the new password name: ", type="password")
    if new_employee == "" or new_password == "":
        return
    record.write(new_employee + " - " + new_password + "\n")
    record.close()


def check_user_and_pass(username, password_input):
    credentials = get_data()
    admin_username = "kaku"
    admin_password = "harsh"
    if username == admin_username and password_input == admin_password:
        return True, "Admin"
    else:
        try:
            if credentials[username] == password_input:
                return True, "Guest"
            else:
                return False, "Guest"
        except ValueError:
            return False, "Invalid user"
