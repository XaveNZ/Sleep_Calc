"""
This script manages user options for age range, wake-up time, and sleep duration,
storing them in the database associated with the signed-in username. These options
are accessible for calculations and are saved for future program use.
"""

import subprocess
import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("SleepCalc")
root.configure(background="Light blue")

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 700
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
label_sleepcalc = ttk.Label(root, image=image, background="Light Blue")
label_sleepcalc.grid(row=1)

def load_options():
    """
    Load user options from the database and display the username.
    """
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

    user_label = ttk.Label(root, text=f"Welcome, {current_user}!", font=("Arial", 11, "bold"),
                           background="Light Blue")
    user_label.grid(row=2, pady=(0, 5), padx=100)

    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()
    cursor.execute("SELECT age_range, wake_up_time, sleep_duration FROM users WHERE username=?",
                   (current_user,))
    user_options = cursor.fetchone()
    connect_db.close()

    if user_options[0] is not None:
        Label_userinfo = ttk.Label(root, text="your previous info:", font=("Arial", 9, "bold"),
                                    background="Light Blue")
        Label_userinfo.grid(row=3)

        age_range = user_options[0]
        wake_up_time = user_options[1]
        sleep_duration = user_options[2]

        result_label = ttk.Label(root, text=f"""
        Age Range: {age_range}
        Wake-up Time: {wake_up_time}
        Previous Sleep Duration: {sleep_duration}""",
        font=("Arial", 9), background="Light Blue")
        result_label.grid(row=4, pady=(0, 0))

load_options()

label_age = ttk.Label(root, text="Select your age range", font=("Arial", 9, "bold"),
                      background="Light Blue")
label_age.grid(row=5, pady=(10,0))

chosen_option1 = StringVar()
options_age = ['less than 5 Years', '7-13 Years', '14-18 Years', '19-30 Years', '30 or more Years']

optionmenu_age = ttk.OptionMenu(root, chosen_option1, options_age[0], *options_age)
optionmenu_age.grid(row=6, pady=(0, 30))

label_wakeuptime = ttk.Label(root, text="What time do you want to wake up?",
                             font=("Arial", 9, "bold"),
                             background="Light Blue")
label_wakeuptime.grid(row=7)

chosen_option2 = StringVar()
options_wakeuptime = ['4 AM', '4:30 AM', '5 AM', '5:30 AM', '6 AM', '6:30 AM', '7 AM', '7:30 AM', '8 AM', '8:30 AM', '9 AM', '9:30 AM', '10 AM', '10:30 AM', '11 AM', '11:30 AM']

optionmenu_time = ttk.OptionMenu(root, chosen_option2, options_wakeuptime[0], *options_wakeuptime)
optionmenu_time.grid(row=8, pady=(0, 30))

label_sleepamount = ttk.Label(root, text="Roughly how long did you sleep last night?",
                              font=("Arial", 9, "bold"), background="Light Blue")
label_sleepamount.grid(row=9)

chosen_option3 = StringVar()
options_sleepamount =  options = ["6 Hours or less", "7 Hours", "8 Hours", "9 Hours","10 Hours or more"]

optionmenu_sleepamount = ttk.OptionMenu(root, chosen_option3, options_sleepamount[0],
                                        *options_sleepamount)
optionmenu_sleepamount.grid(row=10, pady=(0, 30))

def save_options():
    """
    Save selected options to the database for the current user.
    """
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

    age_range = chosen_option1.get()
    wake_up_time = chosen_option2.get()
    sleep_duration = chosen_option3.get()

    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()
    cursor.execute("UPDATE users SET age_range=?, wake_up_time=?, sleep_duration=? WHERE username=?",
                   (age_range, wake_up_time, sleep_duration, current_user))
    connect_db.commit()
    connect_db.close()

def resultpage():
    """
    Open the result page and save user options.
    """
    save_options()
    subprocess.Popen(["python", r"resultpage.py"])
    root.destroy()

Button = ttk.Button(root, text="Calculate", command=resultpage)  
Button.grid(row=11, pady=(0,30))

root.mainloop()
