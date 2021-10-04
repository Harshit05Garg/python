import utils
import streamlit as st
import importlib
importlib.reload(utils)


def input_user_pass():
    st_username = st.empty()
    st_password = st.empty()
    username = st_username.text_input("Enter the username: ")
    password = st_password.text_input("Enter the password: ", type="password")
    if username == "" or password == "":
        return
    eligible, role = utils.check_user_and_pass(username, password)
    if not eligible:
        st.error("Invalid Username or Password")
        return
    st_username.empty()
    st_password.empty()
    if role == "Admin":
        st.write("**Current Employees**: " + ", ".join([f"`{key}`" for key in utils.get_data()]))
        if st.checkbox("Add employee"):
            utils.employee_creation()
    else:
        utils.guest_access(username)

input_user_pass()
