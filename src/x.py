# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
 
# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = currentYear, month = currentMonth,
               day = currentDay,)


cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)
 
# Execute Tkinter
root.mainloop()