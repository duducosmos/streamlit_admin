import streamlit as st

from streamlit_admin import AdminUsers, STAuth

from pages import home

#
auth = STAuth('sqlite://storage.db', './database', pool_size=1)
admin = AdminUsers(auth)


if admin.session_state['loggedIn'] == False:
    admin.login_page()
else:

    with st.sidebar:
        admin.logout_page()

        if auth.user is None:
            auth.logout()

        if auth.is_admin:

            page_names_to_funcs = {
                "Home": home,
                "Create User": admin.page_to_create_user_as_admin,
                "Update of Users": admin.page_to_admin_users,
                "Delete Users": admin.page_to_delete_user,
                "My Account": admin.page_my_account,
            }
        else:

            page_names_to_funcs = {
                "Home": home,
                "My Account": admin.page_my_account,
            }

        pages_name = st.selectbox("Select a Option",
                                  page_names_to_funcs.keys())

    page_names_to_funcs[pages_name]()
