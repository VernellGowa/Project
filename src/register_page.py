import tkinter as tk
from tkinter import ttk
import re
from database import Database
import login_page

class RegisterPage(tk.Frame, Database):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.configure(bg='light blue')

        # First Name
        label_first_name = tk.Label(self, text="First Name:", bg=self.controller.COLOUR)
        label_first_name.pack()
        entry_first_name = tk.Entry(self)
        entry_first_name.pack(pady=5)

        # Last Name
        label_last_name = tk.Label(self, text="Last Name:", bg=self.controller.COLOUR)
        label_last_name.pack()
        entry_last_name = tk.Entry(self)
        entry_last_name.pack(pady=5)

        # Phone Number
        label_phone_number = tk.Label(self, text="Phone Number:", bg=self.controller.COLOUR)
        label_phone_number.pack()
        entry_phone_number = tk.Entry(self)
        entry_phone_number.pack(pady=5)

        # Gender
        label_gender = tk.Label(self, text="Gender:", bg=self.controller.COLOUR)
        label_gender.pack()
        gender_var = tk.StringVar(value="")

        gender_frame = tk.Frame(self, bg=self.controller.COLOUR)
        gender_frame.pack(pady=5)

        gender_button_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
        gender_button_male.pack(side=tk.LEFT)

        gender_button_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
        gender_button_female.pack(side=tk.LEFT)

        gender_button_other = tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")
        gender_button_other.pack(side=tk.LEFT)

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

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=lambda: self.submit(entry_first_name.get(), entry_last_name.get(), entry_phone_number.get(),
                                                                        gender_var.get(), entry_email.get(), entry_password.get()))
        submit_button.pack(pady=10)

        # Navigate to Login Page Button
        login_button = tk.Button(self, text="Go to Login", command=lambda: controller.show_frame(login_page.LoginPage))
        login_button.pack(pady=5)

        self.register_status_label = tk.Label(self, text="", bg=self.controller.COLOUR)
        self.register_status_label.pack()

        def submit(self, first_name, last_name, phone_number, gender, email, password):
            # Check if the fields are not empty
            if not first_name or not last_name or not phone_number or not gender or not email or not password:
                self.register_status_label.config(text="All fields are required!", fg="red")
                return

            # Check if the email is valid
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.register_status_label.config(text="Invalid email address!", fg="red")
                return

            # Check if the password is strong
            if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
                self.register_status_label.config(text="Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, and one digit!", fg="red")
                return

            # Check if the email and password match a customer in the database
            query = "SELECT id FROM customers WHERE email = %s"
            Database.cursor.execute(query, (email,))
            result = Database.cursor.fetchone()

            if result:
                self.register_status_label.config(text="Email already registered!", fg="red")
            else:
                # Insert a new customer into the database
                query = "INSERT INTO customers (first_name, last_name, phone_number, gender, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
                Database.cursor.execute(query, (first_name, last_name, phone_number, gender, email, password))
                Database.conn.commit()
                customer_id = Database.cursor.lastrowid
                self.controller.show_frame(login_page.LoginPage, customer_id)