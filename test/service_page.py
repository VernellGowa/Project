import tkinter as tk
from tkinter import ttk
import database
from PIL import Image, ImageTk
# import booking
from booking import Booking
import home_page

class ServicePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None

        # Configure the rows and columns to expand
        self.grid_columnconfigure(0, weight=1)

        self.configure(bg=self.controller.COLOUR)

        # Create an app bar at the top
        self.app_bar = ttk.Frame(self, width=self.controller.WIDTH, style="Grey.TFrame")
        self.app_bar.grid(row=0, column=0, sticky='ew')

        self.app_title = ttk.Label(self.app_bar, style="White.TLabel")
        self.app_title.pack(anchor="center", padx=40, pady=10)

        font_style = ("Helvetica", 14)

    def handle_back(self):
        self.controller.show_frame(home_page.HomePage, self.customer_id)

    def set_data(self, args):
        self.service = Booking.service
        self.customer_id = args[0]

        # Update the labels with the service details
        self.app_title.config(text=self.service[1])