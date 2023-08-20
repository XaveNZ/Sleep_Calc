"""
(for the signup page - for version 1) test to check that if that if the password entered matches the comfirm password entered that the password validation will work
"""

from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3
import re 

root = Tk()
root.title("password_test")

root.configure(background="Light blue")

#prevents NameError: name 'message_label'
message_label = None

def create_account():
    global message_label
    # Get password
    password = Entry_password.get()
    confirm_password = Entry_confirmpassword.get()

    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()

      # Hide the existing message_label if it's present
    if message_label:
        message_label.grid_forget()

    if len(password) < 8 or len(password) > 30:
        message_label = ttk.Label(root, text="Password must be between 8 and 20 characters.", foreground="red",
                                  background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    # Check if the password contains at least one uppercase letter and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        message_label = ttk.Label(root, text="Password must contain at least one\n uppercase letter and one number.",
                                  foreground="red", background="Light blue", font=('Arial', 12, 'bold'))
        message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
        return

    elif password != confirm_password:
            # Check if the passwords match
            message_label = ttk.Label(root, text="Passwords don't match.", foreground="red",
                                    background="Light blue", font=('Arial', 12, 'bold'))
            message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)
 
Label_signup = ttk.Label(root, text="Sign up", font=("Arial", 20, "bold"), background="Light Blue")
Label_signup.grid(row=1, column=0, pady=30, padx=100)

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

root.mainloop()