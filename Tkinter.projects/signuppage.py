"""
This script creates the database table and defines column names.
It also provides a sign-up page that saves the username and password to the database.
Various if statements are used for username and password validations.
"""

import subprocess
import sqlite3
import re
from tkinter import *
from tkinter import ttk

# Create the main application window
root = Tk()
root.title("SignUp")
root.configure(background="Light blue")

# Setting GUI to open at a set resolution and prevent it from being changed
WINDOW_WIDTH = 420
WINDOW_HEIGHT = 700
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# Create a connection to the database
CONNECTION_DB = sqlite3.connect('database.db')
# Create a cursor to interact with the database
CURSOR = CONNECTION_DB.cursor()
CURSOR.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT PRIMARY KEY, password TEXT,
                   age_range TEXT, wake_up_time TEXT, sleep_duration TEXT)''')
# Commit changes to the database
CONNECTION_DB.commit()
# Close the database connection
CONNECTION_DB.close()

# Prevents NameError: name 'message_label'
message_label = None

def create_account():
    """
    Create a new user account.

    Validates user input and inserts a new user into the database.
    """
    global message_label
    # Get the username and passwords from entry boxes
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirmpassword.get()

    connection_db = sqlite3.connect('database.db')
    cursor = connection_db.cursor()

    # Hide the existing message_label if it's present
    if message_label:
        message_label.grid_forget()

    # Check if the username and password are the same
    if username == password:
        message_label = ttk.Label(root, text="Username and password cannot be the same.",
                            foreground="red", background="Light blue",
                            font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
        return

    # Check username and password length requirements
    if len(username) < 4 or len(username) > 30:
        message_label = ttk.Label(root, text="Username must be between 4 and 20 characters.",
                            foreground="red", background="Light blue",
                            font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
        return

    if len(password) < 8 or len(password) > 30:
        message_label = ttk.Label(root, text="Password must be between 8 and 20 characters.",
                            foreground="red", background="Light blue",
                            font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        message_label = ttk.Label(root, text=
                            "Password must contain at least one\n uppercase letter and one number.",
                            foreground="red", background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
        return

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Display an error message if the username already exists
        message_label = ttk.Label(root, text="Username already Exists", foreground="red",
                            background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
        connection_db.close()
    elif password != confirm_password:
        # Check if the passwords match
        message_label = ttk.Label(root, text="Passwords don't match.", foreground="red",
                            background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection_db.commit()

        # Display success message and run the login.py file
        message_label = ttk.Label(root, text="Registered Successfully", foreground="green",
                            background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, padx=10, pady=5, columnspan=2)

        root.after(1000, open_loginpage)

    connection_db.close()

def open_loginpage():
    """
    Open the login page and close the current window.
    """
    subprocess.Popen(["python", r"loginpage.py"])
    root.destroy()

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
label_sleepcalc = ttk.Label(root, image=image, background="Light Blue")
label_sleepcalc.grid(row=0)

label_signup = ttk.Label(root, text="Sign up", font=("Arial", 20, "bold"),
                         background="Light Blue")
label_signup.grid(row=1, pady=30, padx=100)

label_username = ttk.Label(root, text="Username", font=("Arial", 12, "bold"),
                           background="Light Blue")
label_username.grid(row=2, pady=0, padx=100)

entry_username = ttk.Entry(root)
entry_username.grid(row=3, pady=(0, 20), padx=100)

label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"),
                           background="Light Blue")
label_password.grid(row=4, pady=0, padx=100)

entry_password = ttk.Entry(root, show="*")
entry_password.grid(row=5, pady=0, padx=100)

label_confirmpassword = ttk.Label(root, text="Confirm Password", font=("Arial", 10,),
                                  background="Light Blue")
label_confirmpassword.grid(row=6, pady=(20, 0), padx=100)

entry_confirmpassword = ttk.Entry(root, show="*")
entry_confirmpassword.grid(row=7, padx=100)

# Create account button
create_Account_Button = ttk.Button(root, text="Create Account", command=create_account)
create_Account_Button.grid(row=9, pady=(25, 0), padx=100)

# Go to login page button
def loginpage():
    subprocess.Popen(["python", r"loginpage.py"])
    root.destroy()

login_Button = ttk.Button(root, text="Login", command=loginpage)
login_Button.grid(row=10, pady=(25, 25), padx=100)

root.mainloop()
