import tkinter as tk
from tkinter import ttk
import database
from PIL import Image, ImageTk
from booking import Booking
import service_page
from tkinter import messagebox

class BookingPage(tk.Frame): 
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

        # Create a new frame for the search results
        self.results_frame = ttk.Frame(self.scrollable_frame, style="Blue.TFrame")
        self.results_frame.grid(row=0, column=0, padx=10, pady=10)

        # Display the services in the results frame
        self.display_services(self.results)

    def display_services(self, services):
        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((self.controller.WIDTH//2, len(services)*225), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for i, result in enumerate(services):
            card = tk.Frame(self.results_frame, relief=tk.RAISED, borderwidth=3)

            heart_button = ttk.Button(card, image=self.unlike_icon if result[6] is None else self.like_icon)
            # heart_button.bind("<Button-1>", lambda e, service=result: self.like_service(service, heart_button))
            heart_button.bind("<Button-1>", lambda e, service=result, button=heart_button: self.like_service(service, button))
            heart_button.grid(row=0, column=0, pady=10)


            name_label = ttk.Label(card, text=result[1])
            name_label.grid(row=0, column=0)

            price_label = ttk.Label(card, text=f'£{result[2]}')
            price_label.grid(row=1, column=0)

            duration_label = ttk.Label(card, text=result[3])
            duration_label.grid(row=2, column=0, pady=(0, 10))

            booking_time_label = ttk.Label(card, text=f"{result[5]} {result[6]}")
            booking_time_label.grid(row=2, column=0, pady=(0, 10))

            for child in card.winfo_children()[1:]:
                child.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))

            card.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))
            card.grid(row=i+3, column=0, pady=10)

    def set_data(self, customer_id):
        self.customer_id = customer_id
        query = """
            SELECT bk.id, name, price, duration, DATE(bk.booking_date), TIME(bk.booking_date), st.first_name, st.last_name, st.email
            FROM bookings bk
            INNER JOIN services sv ON bk.service_id = sv.id
            INNER JOIN stylist st ON bk.stylist_id = st.id
            WHERE bk.customer_id = %s AND bk.cancelled_at IS NULL
        """
        database.Database.cursor.execute(query, (self.customer_id))
        self.results = database.Database.cursor.fetchall()

    def modify_booking(self, booking_id):
        # Implement the functionality to modify a booking
        pass

    def cancel_booking(self, booking_id):
        # Implement the functionality to cancel a booking
        pass
