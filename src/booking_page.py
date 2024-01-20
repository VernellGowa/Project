from datetime import datetime
import tkinter as tk
from tkinter import StringVar, ttk
import database
from PIL import Image, ImageTk
from booking import Booking
import service_page
from tkinter import messagebox
import home_page

class BookingPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer_id = None

        style = ttk.Style()
        style.configure("Grey.TFrame", background="dark grey")
        style.configure("White.TLabel", foreground="white", background="dark grey", font=("Verdana", 30))
        style.configure("Blue.TFrame", background="light blue")

        # Create an app bar at the top
        self.app_bar = ttk.Frame(self, width=self.controller.WIDTH, style="Grey.TFrame")
        self.app_bar.pack(side="top", fill="x")

        back_icon = Image.open("back.png")
        back_icon = back_icon.resize((35, 35))
        back_icon = ImageTk.PhotoImage(back_icon)

        self.back_button = ttk.Button(self.app_bar, image=back_icon, command=self.handle_back)
        self.back_button.image = back_icon  # Keep a reference to prevent garbage collection
        self.back_button.pack(side="left", padx=15)

        self.app_title = ttk.Label(self.app_bar, text="Bookings", style="White.TLabel")
        self.app_title.pack(side="left", padx=40, pady=10)

        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self, bg=self.controller.COLOUR)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="Blue.TFrame")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar and the canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a new frame for the search results
        self.results_frame = ttk.Frame(self.scrollable_frame, style="Blue.TFrame")
        self.results_frame.grid(row=3, column=0, padx=10.)

    def display_services(self, services):
        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((self.controller.WIDTH//2, len(services)*225), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for i, result in enumerate(services):
            card = tk.Frame(self.results_frame, relief=tk.RAISED, borderwidth=3, padx=20)

            font_style = ("Helvetica", 14)

            name_label = ttk.Label(card, text=result[2], font=font_style)
            name_label.grid(row=0, column=0)

            price_label = ttk.Label(card, text=f'£{result[3]}', font=font_style)
            price_label.grid(row=1, column=0)

            duration_label = ttk.Label(card, text=f"Duration: {result[4]} mins", font=font_style)
            duration_label.grid(row=2, column=0, pady=(0, 10))

            booking_time_label = ttk.Label(card, text=f"Booking Time: {result[5].strftime('%H:%M %d-%m-%Y')}", font=font_style)
            booking_time_label.grid(row=3, column=0, pady=(0, 10))

            contacts_label = ttk.Label(card, text=f"Stylist: {result[6]} {result[7]}", font=font_style)
            contacts_label.grid(row=4, column=0, pady=(0, 10))

            email_label = ttk.Label(card, text=f"Email: {result[8]}", font=font_style)
            email_label.grid(row=5, column=0, pady=(0, 10))

            number_label = ttk.Label(card, text=f"Phone Number: {result[9]}", font=font_style)
            number_label.grid(row=6, column=0, pady=(0, 10))

            for child in card.winfo_children()[1:]:
                child.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))

            button_frame = ttk.Frame(card)
            button_frame.grid(row=7, column=0, pady=(0, 10))

            # # Create a "View Service" button inside the frame
            # view_service_button = ttk.Button(button_frame, text="View Service")
            # view_service_button.pack(side='left', padx=10)

            rating_var = StringVar()

            # Create a list of possible ratings
            ratings = [str(i) for i in range(6)]

            # Create a combobox for selecting the rating
            rating_combobox = ttk.Combobox(button_frame, textvariable=rating_var, values=ratings, state='readonly', width=5)
            rating_combobox.pack(side='left', padx=10)

            # Set the default rating to 0
            rating_combobox.current(0)

            # Create a "Cancel Booking" button inside the frame
            cancel_or_rate_button = ttk.Button(button_frame, text="Cancel Booking" if result[5] > datetime.now() else "Rate Service",
                    command=lambda: self.cancel_booking(result[0]) if result[5] > datetime.now() else self.rate_service(result[0], rating_var.get()))
            cancel_or_rate_button.pack(side='left', padx=10)

            card.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))
            card.grid(row=i+3, column=0, pady=10)

    def set_data(self, customer_id):
        self.customer_id = customer_id[0]
        query = """
            SELECT bk.id, sv.id, name, price, duration, bk.booking_date, st.first_name,
            st.last_name, st.email, st.phone_number
            FROM bookings bk
            INNER JOIN services sv ON bk.service_id = sv.id
            INNER JOIN stylists st ON bk.stylist_id = st.id
            WHERE bk.customer_id = %s AND bk.cancelled_at IS NULL
        """
        database.Database.cursor.execute(query, (self.customer_id,))
        self.results = database.Database.cursor.fetchall()

        # Display the services in the results frame
        self.display_services(self.results)

    def cancel_booking(self, booking_id):
        query = """
            UPDATE bookings SET cancelled_at = NOW() WHERE id = %s
        """
        database.Database.cursor.execute(query, (booking_id,))
        database.Database.conn.commit()

        # Refresh the page
        self.set_data(self.customer_id)

    def show_service_page(self, service):

        query = """
            SELECT sv.id, name, description, price, duration, image, lk.id FROM services sv
            LEFT JOIN likes lk ON sv.id = lk.service_id AND lk.customer_id = 9
            WHERE sv.id = %s
        """
        database.Database.cursor.execute(query, (service[1]))
        service = database.Database.cursor.fetchone()
        print(service)

        # Show the ServicePage with the details of the selected service
        Booking.service = service
        self.controller.show_frame(service_page.ServicePage, self.customer_id)
        
    def rate_service(self, booking_id, score):
        print((self.customer_id, booking_id, score))
        query = """
            INSERT INTO ratings (customer_id, booking_id, score) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE score = VALUES(score)
        """
        database.Database.cursor.execute(query, (self.customer_id, booking_id, score))
        database.Database.conn.commit()

    def handle_back(self):
        self.controller.show_frame(home_page.HomePage, self.customer_id)