"""
(for the result page - for version 1) test to check if the age range option saved to a text file called selected_options will be read and displayed and testing bedtime calculation  
"""

from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import subprocess

root = Tk()
root.title("display_age_test")
root.configure(background="Light blue")

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)

#display "Your info"
Label_userinfo = ttk.Label(root, text="Your info", font=("Arial", 11, "bold"), background="Light Blue")
Label_userinfo.grid(row=2, column=0, pady=(0, 15), padx=100)

# Load the selected options from the text file 
def load_options():
    with open('selected_options.txt', 'r') as file:
        lines = file.readlines()
        # Extract the selected options from the lines in the text file 
        # (split separates a string into a list of substrings and strip removes any leading and trailing whitespace characters)
        age_range = lines[0].split(": ")[1].strip()
        wake_up_time = lines[1].split(": ")[1].strip()

        # Tesing if it Displays the loaded options on the GUI so that i will know that the values are getting imported or not
        result_label = ttk.Label(root, text=f"Age Range: {age_range}\nWake-up Time: {wake_up_time}", font=("Arial", 9), background="Light Blue")
        result_label.grid(row=3, column=0, pady=(0, 0))

        # Perform calculations for bedtime and sleep sufficiency
        bedtime = calculate_bedtime(age_range, wake_up_time)

        # Display the calculated bedtime and sleep sufficiency
        bedtime_label = ttk.Label(root, text=f"According to your wake up time you should be in bed no later than: {bedtime}", font=("Arial", 9), background="Light Blue")
        bedtime_label.grid(row=4, column=0, pady=(30,0))

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

#open new file and destroy current one for when go back button is hit
def SleepCalc():
    subprocess.Popen(["python", r"version 1\SleepCalc.py"])
    root.destroy() 

#Function to destroy the root window
Button2 = ttk.Button(root, text="Go Back",command=SleepCalc)
Button2.grid(row=9, column=0, pady=(0,30), padx=100)

# Load the selected options automatically
load_options()

root.mainloop()