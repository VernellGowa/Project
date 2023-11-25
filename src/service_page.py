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

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back)
        self.back_button.grid(row=0, column=0, padx=10, pady=10,)

        self.image_label = tk.Label(self, bg=self.controller.COLOUR)
        self.image_label.grid(row=1, column=0, )

        self.name_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR)
        self.name_label.grid(row=2, column=0,)

        self.desc_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR)
        self.desc_label.grid(row=3, column=0)

        self.price_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR)
        self.price_label.grid(row=4, column=0, )

        self.duration_label = ttk.Label(self, anchor='center', background=self.controller.COLOUR)
        self.duration_label.grid(row=5, column=0, )

        self.book_button = ttk.Button(self, text="Book Appointment", command=self.book_appointment)
        self.book_button.grid(row=6, column=0,)

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
        self.price_label.config(text=self.service[3])
        self.duration_label.config(text=self.service[4])

    def book_appointment(self):
        # Code to book an appointment
        Booking.service = self.service
        self.controller.show_frame(date_picker_page.DatePicker, self.customer_id)