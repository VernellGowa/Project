import tkinter as tk
from tkinter import ttk
import database
from PIL import Image, ImageTk
# import booking
from booking import Booking
import home_page
import date_picker_page

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

        home_icon = Image.open("home.png")
        home_icon = home_icon.resize((35, 35))
        home_icon = ImageTk.PhotoImage(home_icon)

        self.home_button = ttk.Button(self.app_bar, image=home_icon, command=self.handle_back)
        self.home_button.image = home_icon  # Keep a reference to prevent garbage collection
        self.home_button.pack(side="left", padx=15)

        self.app_title = ttk.Label(self.app_bar, text="Bookings", style="White.TLabel")
        self.app_title.pack(anchor="center", padx=40, pady=10)

        font_style = ("Helvetica", 14)

        self.image_label = tk.Label(self, bg=self.controller.COLOUR)
        self.image_label.grid(row=1, column=0, pady=(20, 0))

        self.name_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR, font=font_style)
        self.name_label.grid(row=2, column=0)

        self.desc_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR, font=font_style)
        self.desc_label.grid(row=3, column=0)

        self.price_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR, font=font_style)
        self.price_label.grid(row=4, column=0)

        self.duration_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR, font=font_style)
        self.duration_label.grid(row=5, column=0)

        self.book_button = ttk.Button(self, text="Book Appointment", command=self.book_appointment)
        self.book_button.grid(row=6, column=0)

    def handle_back(self):
        self.controller.show_frame(home_page.HomePage, self.customer_id)

    def set_data(self, args):
        self.service = Booking.service
        self.customer_id = args[0]

        # Load the image
        img = Image.open(self.service[5])
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

        # Update the labels with the service details
        self.name_label.config(text=self.service[1])
        self.desc_label.config(text=self.service[2])
        self.price_label.config(text=f'£{self.service[3]}')
        self.duration_label.config(text=f"Duration: {self.service[4]} mins")

    def book_appointment(self):
        # Code to book an appointment
        Booking.service = self.service
        self.controller.show_frame(date_picker_page.DatePicker, self.customer_id)