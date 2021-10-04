import utils
import streamlit as st


def input_user_pass():
    username = st.text_input("Enter the username: ")
    password = st.text_input("Enter the password: ")
    if username == "" or password == "":
        return
    eligible, role = utils.check_user_and_pass(username, password)
    if eligible:
        st.success(f"Welcome {username} {role}")
    else:
        st.error("Invalid Username or Password")
        return
    if role == "Admin":
        names = []
        for name in utils.get_data():
            names.append(name)
        st.info(" , ".join(names))
        if st.checkbox("Add employee"):
            utils.employee_creation()


input_user_pass()
