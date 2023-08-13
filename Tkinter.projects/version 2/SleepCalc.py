from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3

root = Tk()
root.title("SleepCalc")

root.configure(background="Light blue")

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)

###
def load_options():
    # Retrieve the who is signed in from the text file
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

        # Display the username on the GUI
        user_label = ttk.Label(root, text=f"Welcome, {current_user}!", font=("Arial", 11, "bold"), background="Light Blue")
        user_label.grid(row=2, column=0, pady=(0, 5), padx=100)

# display username automatically
load_options()

# Select age range label and dropdown menu
Label_age = ttk.Label(root, text="Select your age range", font=("Arial", 9, "bold"), background="Light Blue")
Label_age.grid(row=5, column=0, pady=(10,0))

chosen_option1 = StringVar()

options_age = ['less than 5 Years', '7-13 Years', '14-18 Years', '19-30 Years', '30 or more Years']

OptionMenu_age = ttk.OptionMenu(root, chosen_option1, options_age[0], *options_age)
OptionMenu_age.grid(row=6, column=0, pady=(0, 30))

# Wake-up time label and dropdown menu
Label_wakeuptime = ttk.Label(root, text="What time do you want to wake up?", font=("Arial", 9, "bold"), background="Light Blue")
Label_wakeuptime.grid(row=7, column=0)

chosen_option2 = StringVar()

options_wakeuptime = ['4 AM', '4:30 AM', '5 AM', '5:30 AM', '6 AM', '6:30 AM', '7 AM', '7:30 AM', '8 AM', '8:30 AM', '9 AM', '9:30 AM', '10 AM', '10:30 AM', '11 AM', '11:30 AM']

OptionMenu2 = ttk.OptionMenu(root, chosen_option2, options_wakeuptime[0], *options_wakeuptime)
OptionMenu2.grid(row=8, column=0, pady=(0, 30))

# Sleep duration label and dropdown menu
Label_sleepamount = ttk.Label(root, text="Roughly how long did you sleep last night?", font=("Arial", 9, "bold"), background="Light Blue")
Label_sleepamount.grid(row=9, column=0)

chosen_option3 = StringVar()

options_sleepamount =  options = ["6 Hours or less", "7 Hours", "8 Hours", "9 Hours","10 Hours or more"]

OptionMenu_sleepamount = ttk.OptionMenu(root, chosen_option3, options_sleepamount[0], *options_sleepamount)
OptionMenu_sleepamount.grid(row=10, column=0, pady=(0, 30))

# tesing .get() and reading values from a text file
def save_options():
    # Retrieve who is signed in from who logined in on the login page from the txt file called current_user.txt
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

    # Get the selected options from the drop-down menus
    age_range = chosen_option1.get()
    wake_up_time = chosen_option2.get()
    sleep_duration = chosen_option3.get()

    # Save the options to the database for the current user
    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()
    cursor.execute("UPDATE users SET age_range=?, wake_up_time=?, sleep_duration=? WHERE username=?",
                   (age_range, wake_up_time, sleep_duration, current_user))
    connect_db.commit()
    connect_db.close()

#go to result page
def resultpage():
    subprocess.Popen(["python", r"version 2\resultpage.py"])
    root.destroy() 

###
def commands():
    resultpage()
    save_options()

# Calculate button and testing the command to see if it will save the options #Function to destroy the root window
#tested it and it dosent work becuase: "SyntaxError: keyword argument repeated: command" so i will fix this
Button = ttk.Button(root, text="Calculate", command=commands)  
Button.grid(row=11, column=0, pady=(0,30))

root.mainloop()