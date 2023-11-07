import tkinter as tk
from tkinter import ttk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Email Address
        label_email = tk.Label(self, text="Email Address:")
        label_email.pack()
        entry_email = tk.Entry(self)
        entry_email.pack(pady=5)

        # Password
        label_password = tk.Label(self, text="Password:")
        label_password.pack()
        entry_password = tk.Entry(self, show="*")
        entry_password.pack(pady=5)

        # Login Button
        login_button = tk.Button(self, text="Login", command=lambda: login(entry_email.get(), entry_password.get()))
        login_button.pack(pady=10)

        self.login_status_label = tk.Label(self, text="")
        self.login_status_label.pack()

        # Navigate to Sign Up Page Button
        sign_up_button = tk.Button(self, text="Go to Sign Up", command=lambda: controller.show_frame(Page1))
        sign_up_button.pack(pady=5)

    def login(self, email, password):
        # Check if the email and password match a customer in the database
        query = "SELECT customer_id FROM customers WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        if result:
            customer_id = result[0]
            self.controller.show_frame(HomePage(customer_id))
        else:
            self.login_status_label.config(text="Invalid email or password", fg="red")