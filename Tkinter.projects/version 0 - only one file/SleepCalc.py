from tkinter import *
from tkinter import ttk

root = Tk()
root.title("SleepCalc")

root.configure(background="Light blue")

image = PhotoImage(file=r"C:\Users\User\Desktop\Tkinter.projects\ddtimages\SleepCalcLogo.png")
image= image.subsample(7)
Label1 = ttk.Label(root, image=image, background="Light Blue")
Label1.grid(row=1, column=0)

Label2 = ttk.Label(root, text="Select your age range")
Label2.grid(row=2, column=0,)

chosen_option = StringVar()

options = ['2-7 Years', '6-13 Years', '14-17 Years', '18-25 Years', '26-35 Years', '46-55 Years', '56-64 Years', '65+ Years']

OptionMenu = ttk.OptionMenu(root, chosen_option, options[0], *options)
OptionMenu.grid(row=3, column=0, pady=(0,30))

Label3 = ttk.Label(root, text="What time do you want to wake up?")
Label3.grid(row=4, column=0,)

chosen_option = StringVar()

options2 = ['5:15 AM', '5:30 AM', '5:45 AM', '6:00 AM', '6:15 AM', '6:30 AM', '6:45 AM', '7:00 AM']

OptionMenu2 = ttk.OptionMenu(root, chosen_option, options2[0], *options2)
OptionMenu2.grid(row=5, column=0, pady=(0,30))

Label3 = ttk.Label(root, text="Roughly how long did you sleep last night?")
Label3.grid(row=6, column=0,)

chosen_option = StringVar()

options3 = ['4 Hours', '5 Hours', '6 hours', '7 hours', '8 Hours', '9 Hours', '10 hours']

OptionMenu3 = ttk.OptionMenu(root, chosen_option, options3[0], *options3)
OptionMenu3.grid(row=7, column=0, pady=(0,30))

Button = ttk.Button(root, text="Calculate")
Button.grid(row=8, column=0)

root.mainloop()