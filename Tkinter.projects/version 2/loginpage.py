from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3

root = Tk()
root.title("Login")

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

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=0, column=0)

Label_login = ttk.Label(root, text="Login", font=("Arial", 20, "bold"), background="Light Blue")
Label_login.grid(row=1, column=0, pady=30, padx=100)

Label_username = ttk.Label(root, text="Username", font=("Arial", 12, "bold"), background="Light Blue")
Label_username.grid(row=2, column=0, pady=0, padx=100)

Entry_username = ttk.Entry(root)
Entry_username.grid(row=3, column=0, pady=(0,20), padx=100)

Label_password = ttk.Label(root, text="Password", font=("Arial", 12, "bold"), background="Light Blue")
Label_password.grid(row=4, column=0, pady=0, padx=100)

Entry_password = ttk.Entry(root, show="*")
Entry_password.grid(row=5, column=0, pady=(0,10), padx=100)

# Initialize the message_label variable
message_label = None

def show_message(message, colour):
    global message_label
    if message_label:
        message_label.grid_forget()
    message_label = ttk.Label(root, text=message, foreground=colour, background="light blue", font=('Arial', 12, 'bold'))
    message_label.grid(row=7, column=0)
    if message == "Login Successful":
        # Save the current username to a text file
        with open("current_user.txt", "w") as user_file:
            user_file.write(Entry_username.get())
        root.after(1000, open_sleep_calc)

# Function to open SleepCalc.py and destroy the current window
def open_sleep_calc():
    subprocess.Popen(["python", r"version 2\SleepCalc.py"])
    root.destroy()

# Creating Database Connection
connect_db = sqlite3.connect('database.db')
cursor = connect_db.cursor()

###############
def login():
    # Get the username and password from entry boxes
    username = Entry_username.get()
    password = Entry_password.get()

    # Check the username and password in the database
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
########

# login button
login_button = ttk.Button(root, text="login", command=login)  
login_button.grid(row=6, column=0, pady=0, padx=100)

# Or label
Label_or = ttk.Label(root, text="Or", font=("Arial", 9, "bold"), background="Light Blue")
Label_or.grid(row=8, column=0, pady=(20,0), padx=100)

#open new file and destroy current one for when signup button is hit
def signup():
    subprocess.Popen(["python", r"version 2\signuppage.py"])
    root.destroy()
    
#Sign up button
Button = ttk.Button(root, text="Go back sign up",command=signup)  
Button.grid(row=9, column=0, pady=(0,30), padx=100)

root.mainloop()