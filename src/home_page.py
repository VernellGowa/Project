import tkinter as tk
from tkinter import ttk
import database
from PIL import Image, ImageTk
# import booking
from booking import Booking
import service_page

class HomePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer_id = None

        query = "SELECT id, name, description, price, duration, image FROM services"
        database.Database.cursor.execute(query, ())
        self.results = database.Database.cursor.fetchall()

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

        self.display_services(self.results)

        label = ttk.Label(self.scrollable_frame, text ="Home", background="light blue", font=("Verdana", 35))
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Create a search bar
        self.search_bar = ttk.Entry(self.scrollable_frame, width=50)
        self.search_bar.grid(row=1, column=0, padx=10, pady=10)

        # Create a search button
        self.search_button = ttk.Button(self.scrollable_frame, text="Search", command=self.search_services)
        self.search_button.grid(row=1, column=1, padx=10, pady=10)



    def set_data(self, customer_id):
        self.customer_id = customer_id[0]

    def display_services(self, services):
        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((self.controller.WIDTH//2, len(services)*200), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Remove all the children widgets from the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.grid_forget()

        for i, result in enumerate(services):
            card = tk.Frame(self.scrollable_frame, relief=tk.RAISED, borderwidth=3)

            img = Image.open(result[5])
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=img)
            img_label.image = img
            img_label.grid(row=0, column=0, padx=30, pady=10)

            name_label = ttk.Label(card, text=result[1])
            name_label.grid(row=1, column=0)

            desc_label = ttk.Label(card, text=result[2], wraplength=300)
            desc_label.grid(row=2, column=0)

            price_label = ttk.Label(card, text=result[3])
            price_label.grid(row=3, column=0)

            duration_label = ttk.Label(card, text=result[4])
            duration_label.grid(row=4, column=0, pady=10)

            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))

            card.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))
            card.grid(row=i+2, column=0, pady=10)

    def search_services(self):
        # Get the text from the search bar
        search_text = self.search_bar.get().lower()

        filtered_results = [result for result in self.results if search_text in result[1].lower() or search_text in result[2].lower()]
        print(filtered_results)
        self.display_services(filtered_results)

    def show_service_page(self, service):
        # Show the ServicePage with the details of the selected service
        Booking.service = service
        self.controller.show_frame(service_page.ServicePage, self.customer_id)