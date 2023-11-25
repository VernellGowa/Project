import tkinter as tk
from tkinter import ttk
# import booking
from booking import Booking
from datetime import datetime
import service_page
from tkcalendar import Calendar
import time_picker_page

class DatePicker(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None
        
        self.configure(bg=self.controller.COLOUR)

        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back).pack(pady = 20)

        # Add Calendar
        self.cal = Calendar(self, selectmode = 'day',
                    year = currentYear, month = currentMonth,
                    day = currentDay,)


        self.cal.pack(pady = 20)
        
        # Add Button and Label
        tk.Button(self, text = "Select Date",
            command = self.send_date).pack(pady = 20)

    def handle_back(self):
        self.controller.show_frame(service_page.ServicePage, self.customer_id)

    def set_data(self, args):
        self.service = Booking.service
        self.customer_id = args[0]

    def send_date(self):
        Booking.date = datetime.strptime(self.cal.get_date(), '%m/%d/%y').strftime('%Y-%m-%d')
        self.controller.show_frame(time_picker_page.TimePicker, self.customer_id)