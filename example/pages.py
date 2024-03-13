import streamlit as st


def home():

    st.write("# Home")
    st.sidebar.success("Select an option.")

    st.markdown("""
# User Administration Dashboard

Welcome to the User Administration Dashboard! This dashboard provides a simple interface for managing users in your system.

## Features

### User Management

- **Add User**: Add a new user to the system by providing their details.
- **Edit User**: Edit existing user details such as name, email, and role.
- **Delete User**: Remove a user from the system.

### User Listing

- **View Users**: See a list of all users currently registered in the system.
- **Search Users**: Search for users by name, email, or role.

## Usage

To get started, simply navigate through the sidebar to access the different features of this dashboard.

## Technologies Used

This project is built using Streamlit, a powerful framework for building data-driven web apps with Python. It provides a simple and intuitive way to create interactive dashboards like this one.


Thank you for using the User Administration Dashboard!""")
