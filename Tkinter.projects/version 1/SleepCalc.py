from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("SleepCalc")

root.configure(background="Light blue")

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)

#your perviuos data:

# Select age range label and dropdown menu
Label_age = ttk.Label(root, text="Select your age range", font=("Arial", 9, "bold"), background="Light Blue")
Label_age.grid(row=2, column=0)

chosen_option1 = StringVar()

options_age = ['less than 5 Years', '7-13 Years', '14-18 Years', '19-30 Years', '30 or more Years']

OptionMenu_age = ttk.OptionMenu(root, chosen_option1, options_age[0], *options_age)
OptionMenu_age.grid(row=3, column=0, pady=(0, 30))

# Wake-up time label and dropdown menu
Label_wakeuptime = ttk.Label(root, text="What time do you want to wake up?", font=("Arial", 9, "bold"), background="Light Blue")
Label_wakeuptime.grid(row=4, column=0)

chosen_option2 = StringVar()

options_wakeuptime = ['4 AM', '4:30 AM', '5 AM', '5:30 AM', '6 AM', '6:30 AM', '7 AM', '7:30 AM', '8 AM', '8:30 AM', '9 AM', '9:30 AM', '10 AM', '10:30 AM', '11 AM', '11:30 AM']

OptionMenu2 = ttk.OptionMenu(root, chosen_option2, options_wakeuptime[0], *options_wakeuptime)
OptionMenu2.grid(row=5, column=0, pady=(0, 30))

# Sleep duration label and dropdown menu
Label_sleepamount = ttk.Label(root, text="Roughly how long did you sleep last night?", font=("Arial", 9, "bold"), background="Light Blue")
Label_sleepamount.grid(row=6, column=0)

chosen_option3 = StringVar()

options_sleepamount =  options = ["6 Hours or less", "7 Hours", "8 Hours", "9 Hours","10 Hours or more"]

OptionMenu_sleepamount = ttk.OptionMenu(root, chosen_option3, options_sleepamount[0], *options_sleepamount)
OptionMenu_sleepamount.grid(row=7, column=0, pady=(0, 30))

# tesing .get() and saving values to a text file
def save_options():
    # Get the selected options from the drop-down menus
    age_range = chosen_option1.get()
    wake_up_time = chosen_option2.get()
    sleep_duration = chosen_option3.get()

    # Save the options to a text file
    with open('selected_options.txt', 'w') as file:
        file.write(f"Age Range: {age_range}\n")
        file.write(f"Wake-up Time: {wake_up_time}\n")
        file.write(f"Sleep Duration: {sleep_duration}")

#open new file and destroy current one
def resultpage():
    subprocess.Popen(["python", r"version 1\resultpage.py"])
    root.destroy() 

###
def commands():
    resultpage()
    save_options()

# Calculate button and testing the command to see if it will save the options #Function to destroy the root window
#tested it and it dosent work becuase: "SyntaxError: keyword argument repeated: command" so i will fix this
Button = ttk.Button(root, text="Calculate", command=commands)  
Button.grid(row=8, column=0, pady=(0,30))

root.mainloop()
