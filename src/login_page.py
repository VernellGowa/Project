import tkinter as tk
from tkinter import ttk
import register_page
import home_page

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Set the background color to light blue
        self.configure(bg=self.controller.COLOUR)

        # Email Address
        label_email = tk.Label(self, text="Email Address:", bg=self.controller.COLOUR)
        label_email.pack()
        entry_email = tk.Entry(self)
        entry_email.pack(pady=5)

        # Password
        label_password = tk.Label(self, text="Password:", bg=self.controller.COLOUR)
        label_password.pack()
        entry_password = tk.Entry(self, show="*")
        entry_password.pack(pady=5)

        # Login Button
        login_button = tk.Button(self, text="Login", command=lambda: self.login(entry_email.get(), entry_password.get()))
        login_button.pack(pady=10)

        self.login_status_label = tk.Label(self, text="", bg=self.controller.COLOUR)
        self.login_status_label.pack()

        # Navigate to Sign Up Page Button
        sign_up_button = tk.Button(self, text="Go to Sign Up", command=lambda: controller.show_frame(register_page.RegisterPage))
        sign_up_button.pack(pady=5)

    def login(self, email, password):
        # Check if the email and password match a customer in the database
        # query = "SELECT id FROM customers WHERE email = %s AND password = %s"
        # Database.cursor.execute(query, (email, password))
        # result = Database.cursor.fetchone()

        # if result:
        #     customer_id = result[0]
        #     self.controller.show_frame(HomePage, customer_id)
        # else:
        #     self.login_status_label.config(text="Invalid email or password", fg="red")
        self.controller.show_frame(home_page.HomePage, 9)