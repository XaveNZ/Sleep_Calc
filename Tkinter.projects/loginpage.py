"""
This script implements a login system that saves the current user who is signed in
to a text file so that the program has access to the currently logged-in user.
Values saved onto the 'SleepCalc.py' database will be associated with the correct user,
saving data in the same column as the username and password.
"""

import subprocess
import sqlite3
from tkinter import *
from tkinter import ttk

# Create and configure the main GUI window
root = Tk()
root.title("Login")
root.configure(background="Light blue")
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

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
label_sleepcalc = ttk.Label(root, image=image, background="Light Blue")
label_sleepcalc.grid(row=0)

# Labels and entries for username and password
label_login = ttk.Label(root, text="Login", font=("Arial", 20, "bold"), background="Light Blue")
label_login.grid(row=1, pady=30, padx=100)

label_username = ttk.Label(root, text="Username", font=("Arial", 12, "bold"),
                           background="Light Blue")
label_username.grid(row=2, pady=0, padx=100)

entry_username = ttk.Entry(root)
entry_username.grid(row=3, pady=(0, 20), padx=100)

label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"),
                           background="Light Blue")
label_password.grid(row=4, pady=0, padx=100)

entry_password = ttk.Entry(root, show="*")
entry_password.grid(row=5, pady=(0, 10), padx=100)

# Initialize the message_label variable
message_label = None

def show_message(message, colour):
    """
    displays a message according to which gets used in the if statements 
    """
    global message_label
    if message_label:
        message_label.grid_forget()
    message_label = ttk.Label(root, text=message, foreground=colour, background="light blue",
                              font=('Arial', 12, 'bold'))
    message_label.grid(row=7)
    if message == "Login Successful":
        # Save the current username to a text file
        with open("current_user.txt", "w") as user_file:
            user_file.write(entry_username.get())
        root.after(1000, open_sleep_calc)

def open_sleep_calc():
    """
    command which opens the main page when someone logs in
    """
    subprocess.Popen(["python", r"SleepCalc.py"])
    root.destroy()

def login():
    # Get the username and password from entry boxes
    username = entry_username.get()
    password = entry_password.get()

    # Check the username and password in the database
    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()

    if user_data:
        # If the user is found, check if the password matches
        if user_data[1] == password:
            show_message("Login Successful", "green")
        else:
            show_message("Invalid Password", "red")
    else:
        show_message("User not found", "red")
    connect_db.close()

# Login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(row=6, pady=0, padx=100)

# "Or" label
Label_or = ttk.Label(root, text="Or", font=("Arial", 9, "bold"), background="Light Blue")
Label_or.grid(row=8, pady=(20, 0), padx=100)

def signup():
    # Open a new file and destroy the current window when the Go back sign up button is pressed
    subprocess.Popen(["python", r"signuppage.py"])
    root.destroy()

# Go back sign up button
signup_Button = ttk.Button(root, text="Go back sign up", command=signup)
signup_Button.grid(row=9, pady=(0, 30), padx=100)

root.mainloop()
