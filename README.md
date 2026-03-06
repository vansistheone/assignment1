
# Assignment 1 – Login and Registration System

## Project Description

This assignment implements a **Login and Registration System** for the NGO Content Management System (CMS).
The system allows users to register, log in securely, access a dashboard, and log out.

The purpose of this module is to provide **secure authentication and session management** for users of the system.

---

## Features Implemented

* User Registration
* User Login using Email and Password
* Password Hashing for Security
* Dashboard Access after Login
* Session Management
* Logout Functionality

---

## Technologies Used

* Python
* Django
* SQLite
* HTML / CSS

---

## Database Schema (Users Table)

| Column Name   | Description                 |
| ------------- | --------------------------- |
| user_id       | Unique ID for each user     |
| full_name     | User's full name            |
| email         | Unique email used for login |
| password_hash | Encrypted password          |
| role          | Defines user access level   |
| status        | Active or inactive user     |
| created_at    | Account creation time       |

---

## How to Run the Project

1. Clone the repository
2. Navigate to the project folder

```
cd ngo_cms
```

3. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

4. Run the server

```
python manage.py runserver
```

5. Open in browser

```
http://127.0.0.1:8000/register
```

---

## Usage Instructions

### Register

* Open the Register page
* Enter full name, email, password, and role
* Submit the form

### Login

* Enter email and password
* After successful login, the user is redirected to the dashboard

### Logout

* Click the logout button to securely exit the system

---

## Author

Vanshika Sahani
