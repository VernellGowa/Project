import tkinter as tk
from PIL import Image, ImageTk
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

        # Create an app bar at the top
        self.app_bar = ttk.Frame(self, width=self.controller.WIDTH, style="Grey.TFrame")
        self.app_bar.pack(side="top", fill="x")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((35, 35))
        back_icon = ImageTk.PhotoImage(back_icon)

        self.back_button = ttk.Button(self.app_bar, image=back_icon, command=self.handle_back)
        self.back_button.image = back_icon  # Keep a reference to prevent garbage collection
        self.back_button.pack(side="left", padx=(15, 0))

        self.app_title = ttk.Label(self.app_bar, text="Choose Date", style="White.TLabel")
        self.app_title.pack(anchor="center", padx=40, pady=10)

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