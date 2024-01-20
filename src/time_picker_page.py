import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
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

        # Create an app bar at the top
        self.app_bar = ttk.Frame(self, width=self.controller.WIDTH, style="Grey.TFrame")
        self.app_bar.pack(side="top", fill="x")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((35, 35))
        back_icon = ImageTk.PhotoImage(back_icon)

        self.back_button = ttk.Button(self.app_bar, image=back_icon, command=self.handle_back)
        self.back_button.image = back_icon  # Keep a reference to prevent garbage collection
        self.back_button.pack(side="left", padx=(15, 0))

        self.app_title = ttk.Label(self.app_bar, text="Choose Time", style="White.TLabel")
        self.app_title.pack(anchor="center", padx=40, pady=10)
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