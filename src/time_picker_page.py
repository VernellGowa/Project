import tkinter as tk
from tkinter import ttk
# import booking
from booking import Booking
from datetime import datetime
import stylist_page
from tktimepicker import AnalogPicker, AnalogThemes
import date_picker_page

class TimePicker(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None

        self.configure(bg=self.controller.COLOUR)

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back).pack(pady = 20)

        self.time_picker = AnalogPicker(self)
        self.time_picker.pack(expand=True, fill="both")

        theme = AnalogThemes(self.time_picker)
        theme.setNavyBlue()

        tk.Button(self, text = "Select Time",
                    command = self.send_time).pack(pady = 20)


    def handle_back(self):
        self.controller.show_frame(date_picker_page.DatePicker,  self.customer_id)

    def set_data(self, args):
        self.service = Booking.service
        self.customer_id = args[0]

    def send_time(self):
        hour, minute, period = self.time_picker.time()
        Booking.time = datetime.strptime(f"{hour}:{minute} {period}", '%I:%M %p').time()
        print(f"{Booking.date} {Booking.time}")
        self.controller.show_frame(stylist_page.StylistPage, self.customer_id)