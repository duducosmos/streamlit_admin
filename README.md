# Basic Authenticator for Streamlit Using Database

Loggin system based on pydal to connect Database.
First user is Admin.
## Install
```bash
pip install streamlit-admin
```

## Usage Example

```python
STAuthView(databaseInfo, databaseFolder)
```

databaseInfo -> see list of database \
databaseFolder -> Folder to save data base info and data

## User table 

The basic authentication create the following user table:
```python
database.define_table("users",
                        Field("username", "string", unique=True),
                        Field("email", "string", unique=True),
                        Field("password", "string"),
                        Field("role", "string", default="guest")
                        )

```

## Usage Example

```python
import streamlit as st

from streamlit_admin import AdminUsers, STAuth

# 
auth = STAuth('sqlite://storage.db', './database')
admin = AdminUsers(auth)

if admin.session_state['loggedIn'] == False:
    admin.login_page()
else:
    admin.logout_page()
    st.write("Oi Mundo")

```
### Login Page
![Loggin](https://raw.githubusercontent.com/duducosmos/streamlit_admin/main/images/init_page.png)

### Sign (Create User) Page
![Loggin](https://raw.githubusercontent.com/duducosmos/streamlit_admin/main/images/sigin.png)

### Home Page with logout button

![Loggin](https://raw.githubusercontent.com/duducosmos/streamlit_admin/main/images/logged.png)

## List of Database:

SQLite	sqlite://storage.sqlite \
MySQL	mysql://username:password@localhost/test?set_encoding=utf8mb4 \
PostgreSQL	postgres://username:password@localhost/test \
MSSQL (legacy)	mssql://username:password@localhost/test \
MSSQL (>=2005)	mssql3://username:password@localhost/test \
MSSQL (>=2012)	mssql4://username:password@localhost/test \
FireBird	firebird://username:password@localhost/test \
Oracle	oracle://username/password@test \
DB2	db2://username:password@test \ 
Ingres	ingres://username:password@localhost/test \
Sybase	sybase://username:password@localhost/test \
Informix	informix://username:password@test \
Teradata	teradata://DSN=dsn;UID=user;PWD=pass;DATABASE=test \
Cubrid	cubrid://username:password@localhost/test \
SAPDB	sapdb://username:password@localhost/test \
IMAP	imap://user:password@server:port \
MongoDB	mongodb://username:password@localhost/test \
Google/SQL	google:sql://project:instance/database \
Google/NoSQL	google:datastore \
Google/NoSQL/NDB	google:datastore+ndb 

