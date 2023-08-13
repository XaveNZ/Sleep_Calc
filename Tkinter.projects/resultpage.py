"""
This script accesses the database for the age range, wake up time and sleep duration options
for the signed-in user (whose username is read from a text file). It performs calculations to
determine if the user got enough sleep for their age and provides a recommended bedtime for
their wake-up time. Additionally, it displays sleep benefits, negative effects of lack of sleep,
and sleep tips.
"""

from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import subprocess
import sqlite3

root = Tk()
root.title("resultpage")
root.configure(background="Light blue")

# Setting GUI to open at a set resolution and prevent it from being changed
WINDOW_WIDTH = 420
WINDOW_HEIGHT = 700
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
label_sleepcalc = ttk.Label(root, image=image, background="Light Blue")
label_sleepcalc.grid(row=1)

# Display "Your info"
label_userinfo = ttk.Label(root, text="Your info:", font=("Arial", 9), background="Light Blue")
label_userinfo.grid(row=3, pady=(0, 0))

# Importing the options the user selected from the database for the signed-in user
def load_options():
    # Retrieve the signed-in user from the text file
    with open("current_user.txt", "r") as user_file:
        current_user = user_file.read()

    # Display the username and loaded options on the GUI
    user_label = ttk.Label(root, text=f"User: {current_user}", font=("Arial", 12, "bold"),
                           background="Light Blue")
    user_label.grid(row=2, pady=(0, 0), padx=100)

    # Connect to the database
    connect_db = sqlite3.connect('database.db')
    cursor = connect_db.cursor()

    # Retrieve user's options from the database based on the current username
    cursor.execute("SELECT age_range, wake_up_time, sleep_duration FROM users WHERE username=?",
                   (current_user,))
    user_options = cursor.fetchone()

    # Close the database connection
    connect_db.close()

    # Extract user options
    age_range = user_options[0]
    wake_up_time = user_options[1]
    sleep_duration = user_options[2]

    # Display the loaded options on the GUI
    result_label = ttk.Label(root, text=
    f"Age Range: {age_range}\nWake-up Time: {wake_up_time}\nPrevious Sleep Duration: {sleep_duration}",
    font=("Arial", 9), background="Light Blue")
    result_label.grid(row=4, pady=(0, 0))

    # Perform calculations for bedtime and sleep sufficiency
    bedtime = calculate_bedtime(age_range, wake_up_time)
    sleep_sufficiency = check_sleep_sufficiency(age_range, sleep_duration)

    # Display the calculated sleep sufficiency and bedtime
    sufficiency = check_sleep_sufficiency(age_range, sleep_duration)
    sufficiency_label_color = "green" if "✅" in sufficiency else "red"

    sufficiency_label = ttk.Label(root, text=f"{sleep_sufficiency}", font=("Arial", 9, "bold"),
                                  background="Light Blue", foreground=sufficiency_label_color)
    sufficiency_label.grid(row=5, pady=(5, 0))

    bedtime_label = ttk.Label(root, text=
    f"According to your age and wake-up time, you\nshould be in bed no later than: {bedtime}",
    font=("Arial", 9, "bold"), background="gainsboro", relief="solid")
    bedtime_label.grid(row=6, pady=(0, 10))

# Calculate bedtime based on age range and wake-up time
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
        sufficiency = "Your sleep was most likely sufficient for your age ✅"
    elif age_range == '7-13 Years' and sleep_hour >= 10:
        sufficiency = "Your sleep was most likely sufficient for your age ✅"
    elif age_range == '14-18 Years' and sleep_hour >= 8:
        sufficiency = "Your sleep was most likely sufficient for your age ✅"
    elif age_range == '19-30 Years' and sleep_hour >= 7:
        sufficiency = "Your sleep was most likely sufficient for your age ✅"
    elif age_range == '30 or more Years' and sleep_hour >= 7:
        sufficiency = "Your sleep was most likely sufficient for your age ✅"
    else:
        sufficiency = "Your sleep was most likely not sufficient enough for your age ❌"

    return sufficiency

# Benefits of sleep and negatives from lack of sleep
label_sleepinfo = ttk.Label(root, text=
            "  Lack of sleep can lead to impaired concentration, increased stress,\n"
            "increase risk of health issues and a weakened immune system while\n"
            " better sleep can improve memory, mood, mental and physical health\n"
            "                                     and overall cognitive function",
            background="light blue", font=("Arial", 9))
label_sleepinfo.grid(row=7, pady=(0, 0))

# Open a new file and destroy the current one when the "Go Back" button is hit
def sleep_calc():
    subprocess.Popen(["python", r"SleepCalc.py"])
    root.destroy()

# Go Back button
button_go_back = ttk.Button(root, text="Go Back", command=sleep_calc)
button_go_back.grid(row=8, pady=(20, 5), padx=100)

# Logout and go to signuppage.py
def signup_page():
    subprocess.Popen(["python", r"signuppage.py"])
    root.destroy()

# Logout button
button_logout = ttk.Button(root, text="Logout", command=signup_page)
button_logout.grid(row=9, pady=(0, 12), padx=100)

# Sleep tips
label_sleeptips = ttk.Label(root, text=
            "Sleep Tips:\n"
            "Stick to a consistent sleep schedule.\n"
            "Optimize your sleep environment (comfortable, dark, good temperature)         .\n"
            "Minimize screen time before bed.\n"
            "Avoid heavy meals, caffeine, and alcohol close to bedtime.\n"
            "Stay physically active.\n"
            "Limit daytime naps.", background="gainsboro", font=("Arial", 9))
label_sleeptips.grid(row=10)

# Load the options automatically
load_options()

root.mainloop()
