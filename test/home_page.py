import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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


    def set_data(self, customer_id):
        self.customer_id = customer_id[0]
