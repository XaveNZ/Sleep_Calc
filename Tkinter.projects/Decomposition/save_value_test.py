"""
(for the SleepCalc page - for version 1) test to check if the age range option selected in the drop down menus will be saved to a text file called selected_options
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("save_value_test")

root.configure(background="Light blue")

# Displaying an image with an appropriate scale size
image = PhotoImage(file=r"ddtimages\SleepCalcLogo.png")
image = image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)


# Select age range label and dropdown menu
Label_age = ttk.Label(root, text="Select your age range", font=("Arial", 9, "bold"), background="Light Blue")
Label_age.grid(row=2, column=0)

chosen_option1 = StringVar()

options_age = ['less than 5 Years', '7-13 Years', '14-18 Years', '19-30 Years', '30 or more Years']

OptionMenu_age = ttk.OptionMenu(root, chosen_option1, options_age[0], *options_age)
OptionMenu_age.grid(row=3, column=0, pady=(0, 30))

# tesing .get() and saving values to a text file
def save_options():
    # Get the selected options from the drop-down menus
    age_range = chosen_option1.get()

    # Save the options to a text file
    with open('selected_options.txt', 'w') as file:
        file.write(f"Age Range: {age_range}\n")

###
def commands():
    save_options()

# Calculate button and testing the command to see if it will save the options #Function to destroy the root window
#tested it and it dosent work becuase: "SyntaxError: keyword argument repeated: command" so i will fix this
Button = ttk.Button(root, text="Calculate", command=commands)  
Button.grid(row=8, column=0, pady=(0,30))

root.mainloop()
