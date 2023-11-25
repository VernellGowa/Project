import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# import booking
from booking import Booking
from datetime import datetime
from tktimepicker import AnalogPicker, AnalogThemes
import database
import home_page
import time_picker_page

class StylistPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer_id = None

        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self, bg=self.controller.COLOUR)
        style = ttk.Style()
        style.configure("Blue.TFrame", background="light blue")

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="Blue.TFrame")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar and the canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((self.controller.WIDTH//2, 0), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        back_button = ttk.Button(self.scrollable_frame, text="Back", command=self.handle_back)
        back_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        label = ttk.Label(self.scrollable_frame, text ="Choose Stylist", background="light blue", font=("Verdana", 35))
        label.grid(row = 1, column = 0, padx = 10, pady = 10)

        query = """SELECT st.id, first_name, last_name, email FROM stylists st
            LEFT JOIN bookings bk ON st.id = bk.stylist_id
            LEFT JOIN services sv ON sv.id = bk.service_id
            AND %s BETWEEN bk.booking_date AND ADDTIME(bk.booking_date, sv.duration)
            WHERE bk.stylist_id IS NULL
        """
        time = f"{Booking.date} {Booking.time}"
        database.Database.cursor.execute(query, (time,))
        results = database.Database.cursor.fetchall()

        for i, result in enumerate(results):
            card = tk.Frame(self.scrollable_frame, relief=tk.RAISED, borderwidth=2)

            name_label = ttk.Label(card, text=f"{result[1]} {result[2]}")
            name_label.grid(row=0, column=0, pady = 5)

            email_label = ttk.Label(card, text=result[3])
            email_label.grid(row=1, column=0, padx = 35, pady = 5)

            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, result: self.select_stylist(result[0]))

            card.bind("<Button-1>", lambda e, result: self.select_stylist(result[0]))
            card.grid(row=i+2, column=0, pady=5)

    def set_data(self, args):
        self.service = Booking.service
        self.customer_id = args[0]

    def handle_back(self):
        self.controller.show_frame(time_picker_page.TimePicker, self.customer_id)

    def select_stylist(self, stylist_id):
        Booking.stylist_id = stylist_id

        query = "INSERT INTO bookings (customer_id, service_id, stylist_id, booking_date) VALUES (%s, %s, %s, %s)"
        database.Database.cursor.execute(query, (self.customer_id, Booking.service[0], Booking.stylist_id, f"{Booking.date} {Booking.time}"))
        database.Database.conn.commit()
        
        messagebox.showerror("Success", "Booking successful!")
        
        self.controller.show_frame(home_page.HomePage, self.customer_id) 