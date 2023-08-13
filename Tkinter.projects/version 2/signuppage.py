from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3
import re 

root = Tk()
root.title("SignUp")

root.configure(background="Light blue")

#Creating Database
connect_db= sqlite3.connect('database.db')
#Creating CursorF
cursor = connect_db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT PRIMARY KEY, password TEXT,
                   age_range TEXT, wake_up_time TEXT, sleep_duration TEXT)''')

#Commiting Changes
connect_db.commit()
#Closing 
connect_db.close

#prevents NameError: name 'message_label'
message_label = None

def create_account():
    global message_label
    # Get the username and passwords from entry boxes
    username = Entry_username.get()
    password = Entry_password.get()
    confirm_password = Entry_confirmpassword.get()

    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()

      # Hide the existing message_label if it's present
    if message_label:
        message_label.grid_forget()

    # Check if the username and password are the same
    if username == password:
        message_label = ttk.Label(root, text="Username and password cannot be the same.", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check username and password length requirements
    if len(username) < 4 or len(username) > 30:
        message_label = ttk.Label(root, text="Username must be between 4 and 20 characters.", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    if len(password) < 8 or len(password) > 30:
        message_label = ttk.Label(root, text="Password must be between 8 and 20 characters.", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        message_label = ttk.Label(root, text="Password must contain at least one \n uppercase letter and one number.",
                                  foreground="red", background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Display an error message if the username already exists
        message_label = ttk.Label(root, text="Username already Exists", foreground="red", background="Light blue",
        font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)

        connect_db.close() 
    elif password != confirm_password:
            # Check if the passwords match
            message_label = ttk.Label(root, text="Passwords don't match.", foreground="red",
                                    background="Light blue", font=('Arial', 12, 'bold'))
            message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)

    else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connect_db.commit()

            # Display success message and run the login.py file
            message_label = ttk.Label(root, text="Registered Successfully", foreground="green", background="Light blue",
                                        font=('Arial', 12, 'bold'))
            message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
            
            root.after(1000, open_loginpage)

    connect_db.close() 

def open_loginpage():
    subprocess.Popen(["python", r"version 2\loginpage.py"])
    root.destroy() 

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=0, column=0)

Label_signup = ttk.Label(root, text="Sign up", font=("Arial", 20, "bold"), background="Light Blue")
Label_signup.grid(row=1, column=0, pady=30, padx=100)

Label_username = ttk.Label(root, text="Username", font=("Arial", 12, "bold"), background="Light Blue")
Label_username.grid(row=2, column=0, pady=0, padx=100)

Entry_username = ttk.Entry(root)
Entry_username.grid(row=3, column=0, pady=(0,20), padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"), background="Light Blue")
Label_password.grid(row=4, column=0, pady=0, padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=5, column=0, pady=0, padx=100)

Label_confirmpassword = ttk.Label(root, text="Confirm Password", font=("Arial", 10,), background="Light Blue")
Label_confirmpassword.grid(row=6, column=0, pady=(20,0), padx=100)

Entry_confirmpassword = ttk.Entry(root, show="*")
Entry_confirmpassword.grid(row=7, column=0, padx=100)

#create account
Button = ttk.Button(root, text="Create Account", command=create_account)  
Button.grid(row=9, column=0, pady=(25,0), padx=100)

#go to login page
#open new file and destroy current one for when create account button is hit
def loginpage():
    subprocess.Popen(["python", r"version 2\loginpage.py"])
    root.destroy() 

#go to login
Button = ttk.Button(root, text="login", command=loginpage)  
Button.grid(row=10, column=0, pady=(25,25), padx=100)

root.mainloop()