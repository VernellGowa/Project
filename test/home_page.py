import tkinter as tk
from tkinter import ttk
import database
from PIL import Image, ImageTk
from booking import Booking
import service_page
from tkinter import messagebox
import booking_page

class HomePage(tk.Frame): 
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

        # Add a label for the app title
        self.app_title = ttk.Label(self.app_bar, text="Stylez", style="White.TLabel")
        self.app_title.pack(side="left", padx=40, pady=10)

        menu_icon = Image.open("menu.png")
        menu_icon = menu_icon.resize((35, 35))
        menu_icon = ImageTk.PhotoImage(menu_icon)

        self.bookings_button = ttk.Button(self.app_bar, image=menu_icon, command=self.show_booking_page)
        self.bookings_button.image = menu_icon  # Keep a reference to prevent garbage collection
        self.bookings_button.pack(side="right", padx=15)

        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self, bg=self.controller.COLOUR)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="Blue.TFrame")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar and the canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a search bar
        self.search_bar = ttk.Entry(self.scrollable_frame, width=40)
        self.search_bar.bind("<Return>", self.on_enter_key)
        self.search_bar.grid(row=1, column=0, pady=10)

        # Create a search button
        self.search_button = ttk.Button(self.scrollable_frame, text="Search", command=self.search_services)
        self.search_button.grid(row=1, column=1, padx=10, pady=10)

        # Create a frame to contain the sort by label and dropdown
        self.sort_by_frame = ttk.Frame(self.scrollable_frame)
        self.sort_by_frame.grid(row=2, column=0, pady=10)

        # Create a sort by label
        self.sort_by_label = ttk.Label(self.sort_by_frame, text="Sort by:")
        self.sort_by_label.pack(side='left')

        # Create a sort by dropdown
        self.sort_by_options = ['Relevance', 'Price: Low to High', 'Price: High to Low']
        self.sort_by = ttk.Combobox(self.sort_by_frame, values=self.sort_by_options, state='readonly', height=5)
        self.sort_by.pack(side='left', padx=10)
        self.sort_by.set('Relevance')

        # Bind the sort_services method to the <<ComboboxSelected>> event
        self.sort_by.bind('<<ComboboxSelected>>', self.sort_services)

        # Create a new frame for the search results
        self.results_frame = ttk.Frame(self.scrollable_frame, style="Blue.TFrame")
        self.results_frame.grid(row=3, column=0, padx=10, pady=10)

        # Open the heart icon image file
        like_icon = Image.open("like.png")
        unlike_icon = Image.open("unlike.png")

        like_icon = like_icon.resize((20, 20))
        unlike_icon = unlike_icon.resize((20, 20))

        # Create a PhotoImage object from the image
        self.like_icon = ImageTk.PhotoImage(like_icon)
        self.unlike_icon = ImageTk.PhotoImage(unlike_icon)

    def display_services(self, services):
        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((self.controller.WIDTH//2, len(services)*225), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for i, result in enumerate(services):
            result = list(result)
            card = tk.Frame(self.results_frame, relief=tk.RAISED, borderwidth=3)

            heart_button = ttk.Button(card, image=self.unlike_icon if result[6] is None else self.like_icon)
            # heart_button.bind("<Button-1>", lambda e, service=result: self.like_service(service, heart_button))
            heart_button.bind("<Button-1>", lambda e, service=result, button=heart_button: self.like_service(service, button))
            heart_button.grid(row=0, column=0, pady=10)

            img = Image.open(result[5])
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=img)
            img_label.image = img
            img_label.grid(row=1, column=0, padx=30, pady=10)

            name_label = ttk.Label(card, text=result[1], font=("Helvetica", 12, "bold"))
            name_label.grid(row=2, column=0)

            desc_label = ttk.Label(card, text=result[2], wraplength=300)
            desc_label.grid(row=3, column=0)

            price_label = ttk.Label(card, text=f'£{result[3]}')
            price_label.grid(row=4, column=0)

            duration_label = ttk.Label(card, text=f"Duration: {result[4]} mins")
            duration_label.grid(row=5, column=0, pady=(0, 10))

            for child in card.winfo_children()[1:]:
                child.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))

            card.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))
            card.grid(row=i+3, column=0, pady=10)

    def like_service(self, service, button):
        if service[6] is None:
            # If the service is not liked yet insert a new like into the database
            query = "INSERT INTO likes (customer_id, service_id) VALUES (%s, %s)"
            database.Database.cursor.execute(query, (self.customer_id, service[0]))
            like_id = database.Database.cursor.lastrowid
            database.Database.conn.commit()
            # Update the button image to 'liked'
            button.config(image=self.like_icon)
            # Update the service status to 'liked'
            service[6] = like_id

        else:
            # If the service is already liked, remove the like from the database
            query = "DELETE FROM likes WHERE id = %s"
            database.Database.cursor.execute(query, (service[6],))
            database.Database.conn.commit()
            # Update the button image to 'unliked'
            button.config(image=self.unlike_icon)
            # Update the service status to 'unliked'
            service[6] = None

    def search_services(self):
        # Get the text from the search bar
        search_text = self.search_bar.get().lower()

        filtered_results = [result for result in self.results if search_text in result[1].lower() or search_text in result[2].lower()]

        # Clear the scrollable frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not filtered_results:
            messagebox.showwarning("No Results", "No items found in search.")
        else:
            # Display the results
            self.display_services(filtered_results)

    def sort_services(self, event):
        selected_option = self.sort_by.get()
        print(selected_option)

        if selected_option == 'Price: Low to High':
            sorted_results = self.quicksort_services(self.results, asc=True)
        elif selected_option == 'Price: High to Low':
            sorted_results = self.quicksort_services(self.results, asc=False)
        else:
            sorted_results = self.results

        # Clear the scrollable frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Display the results
        self.display_services(sorted_results)

    def quicksort_services(self, services, asc=True):
        if len(services) <= 1:
            return services
        else:
            pivot = services[0]
            less_than_pivot = [s for s in services[1:] if s[3] < pivot[3]]
            greater_than_pivot = [s for s in services[1:] if s[3] >= pivot[3]]
            if asc:
                return self.quicksort_services(less_than_pivot, asc) + [pivot] + self.quicksort_services(greater_than_pivot, asc)
            else:
                return self.quicksort_services(greater_than_pivot, asc) + [pivot] + self.quicksort_services(less_than_pivot, asc)

    def show_booking_page(self):
        self.controller.show_frame(booking_page.BookingPage, self.customer_id)
        # Code to navigate to the bookings page goes here

    def show_service_page(self, service):
        # Show the ServicePage with the details of the selected service
        Booking.service = service
        self.controller.show_frame(service_page.ServicePage, self.customer_id)

    def set_data(self, customer_id):
        self.customer_id = customer_id[0]

        query = """
            SELECT sv.id, name, description, price, duration, image, lk.id FROM services sv
            LEFT JOIN likes lk ON sv.id = lk.service_id AND lk.customer_id = %s
            ORDER BY lk.id DESC
        """
        database.Database.cursor.execute(query, (self.customer_id,))
        self.results = database.Database.cursor.fetchall()

        self.display_services(self.results)

    def on_enter_key(self, event):
        self.search_services()