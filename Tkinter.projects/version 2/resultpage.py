from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import subprocess
import sqlite3

root = Tk()
root.title("resultpage")
root.configure(background="Light blue")

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)

#display "Your info"
Label_userinfo = ttk.Label(root, text="Your info:", font=("Arial", 11, "bold"), background="Light Blue")
Label_userinfo.grid(row=3, column=0, pady=(5, 5), )

###############
# improrting the options the user selected from the database from who is signed in 
def load_options():
    # Retrieve the who is signed in from the text file
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

    # Display the username and loaded options on the GUI
    user_label = ttk.Label(root, text=f"user: {current_user}", font=("Arial", 11, "bold"), background="Light Blue")
    user_label.grid(row=2, column=0, pady=(0, 15), padx=100)

    # Connect to the database
    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()

    # Retrieve user's options from the database based on the current username
    cursor.execute("SELECT age_range, wake_up_time, sleep_duration FROM users WHERE username=?", (current_user,))
    user_options = cursor.fetchone()
    
    # Close the database connection
    connect_db.close()

    # Extract user options
    age_range = user_options[0]
    wake_up_time = user_options[1]
    sleep_duration = user_options[2]

    # Display the loaded options on the GUI
    result_label = ttk.Label(root, text=f"Age Range: {age_range}\nWake-up Time: {wake_up_time}\nPrevious Sleep Duration: {sleep_duration}", font=("Arial", 9), background="Light Blue")
    result_label.grid(row=4, column=0, pady=(0, 0))

    # Perform calculations for bedtime and sleep sufficiency
    bedtime = calculate_bedtime(age_range, wake_up_time)
    sleep_sufficiency = check_sleep_sufficiency(age_range, sleep_duration)

    # Display the calculated bedtime and sleep sufficiency
    bedtime_label = ttk.Label(root, text=f"According to your wake up time you should be in bed no later than: {bedtime}", font=("Arial", 9), background="Light Blue")
    bedtime_label.grid(row=5, column=0, pady=(30,0))
    
    sufficiency_label = ttk.Label(root, text=f"{sleep_sufficiency}", font=("Arial", 9), background="Light Blue")
    sufficiency_label.grid(row=6, column=0, pady=(5,50))
##########

# Calculate bedtime based on age range and wake-up time 
# (%I Represents 01-12 hour)(%M: Represents minutes 00 to 59)(%p: Represents the AM or PM notation)
def calculate_bedtime(age_range, wake_up_time):
    if ":" in wake_up_time:
        wake_up_format = "%I:%M %p"
    else:
        wake_up_format = "%I %p"
    
    wake_up = datetime.strptime(wake_up_time, wake_up_format)
    
    if age_range == 'less than 5 Years':
        bedtime = wake_up - timedelta(hours=11)
    elif age_range == '7-13 Years':
        bedtime = wake_up - timedelta(hours=10)
    elif age_range == '14-18 Years':
        bedtime = wake_up - timedelta(hours=8)
    elif age_range == '19-30 Years':
        bedtime = wake_up - timedelta(hours=7)
    else:
        bedtime = wake_up - timedelta(hours=7)
    
    bedtime_str = bedtime.strftime("%I:%M %p")
    return bedtime_str

# Check sleep sufficiency based on age range and sleep duration
def check_sleep_sufficiency(age_range, sleep_duration):
    sleep_hour = int(sleep_duration.split()[0])  # Extract the hour from the sleep duration

    if age_range == 'less than 5 Years' and sleep_hour >= 11:
        sufficiency = "Your sleep was most likely sufficient for your age"
    elif age_range == '7-13 Years' and sleep_hour >= 10:
        sufficiency = "Your sleep was most likely sufficient for your age"
    elif age_range == '14-18 Years' and sleep_hour >= 8:
        sufficiency = "Your sleep was most likely sufficient for your age"
    elif age_range == '19-30 Years' and sleep_hour >= 7:
        sufficiency = "Your sleep was most likely sufficient for your age"
    elif age_range == '30 or more Years' and sleep_hour >= 7:
        sufficiency = "Your sleep was most likely sufficient for your age"
    else:
        sufficiency = "Your sleep was most likely not sufficient enough for your age"

    return sufficiency

#open new file and destroy current one for when go back button is hit
def SleepCalc():
    subprocess.Popen(["python", r"version 2\SleepCalc.py"])
    root.destroy() 

#Go back button
Button2 = ttk.Button(root, text="Go Back",command=SleepCalc)
Button2.grid(row=8, column=0, pady=(0,5), padx=100)

#logout and go to signuppage.py
def signuppage():
    subprocess.Popen(["python", r"version 2\signuppage.py"])
    root.destroy() 

#Logout button
Button3 = ttk.Button(root, text="Logout",command=signuppage)
Button3.grid(row=9, column=0, pady=(0,30), padx=100)

# Load the options automatically
load_options()

root.mainloop()