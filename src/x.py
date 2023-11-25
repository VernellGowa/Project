import tkinter as tk
from tkcalendar import Calendar, DateEntry
from datetime import datetime

root = tk.Tk()

def send_date():
    print(cal.get_date())
    print(datetime.strptime(cal.get_date(), '%m/%d/%y').strftime('%Y-%m-%d'))

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


# Add Calendar
cal = Calendar(root, selectmode = 'day',
            year = currentYear, month = currentMonth,
            day = currentDay,)


cal.pack(pady = 20)

# Add Button and Label
tk.Button(root, text = "Select Date",
    command = send_date).pack(pady = 20)

root.mainloop()

