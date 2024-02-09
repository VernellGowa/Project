import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox
import bcrypt
import login_page
from database import Database
import home_page

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.configure(bg='light blue')

        # Define font styles
        text_font = tk.font.Font(family='Helvetica', size=12, weight='bold')

        label_title = tk.Label(self, text="Register Page", bg=self.controller.COLOUR, font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=(30,0))

        # First Name
        label_first_name = tk.Label(self, text="First Name:", bg=self.controller.COLOUR, font=text_font)
        label_first_name.pack(pady=(30,0))
        entry_first_name = tk.Entry(self, font=text_font)
        entry_first_name.pack(pady=5)

        # Last Name
        label_last_name = tk.Label(self, text="Last Name:", bg=self.controller.COLOUR, font=text_font)
        label_last_name.pack()
        entry_last_name = tk.Entry(self, font=text_font)
        entry_last_name.pack(pady=5)

        # Phone Number
        label_phone_number = tk.Label(self, text="Phone Number:", bg=self.controller.COLOUR, font=text_font)
        label_phone_number.pack()
        entry_phone_number = tk.Entry(self, font=text_font)
        entry_phone_number.pack(pady=5)

        # Gender
        label_gender = tk.Label(self, text="Gender:", bg=self.controller.COLOUR, font=text_font)
        label_gender.pack()
        gender_var = tk.StringVar(value="Male")  # Set to "Male" initially

        gender_frame = tk.Frame(self, bg=self.controller.COLOUR)
        gender_frame.pack(pady=5)

        gender_button_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg=self.controller.COLOUR, font=text_font)
        gender_button_male.pack(side=tk.LEFT)

        gender_button_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg=self.controller.COLOUR, font=text_font)
        gender_button_female.pack(side=tk.LEFT)

        gender_button_other = tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", bg=self.controller.COLOUR, font=text_font)
        gender_button_other.pack(side=tk.LEFT)

        # Email Address
        label_email = tk.Label(self, text="Email Address:", bg=self.controller.COLOUR, font=text_font)
        label_email.pack()
        entry_email = tk.Entry(self, font=text_font)
        entry_email.pack(pady=5)

        # Password
        label_password = tk.Label(self, text="Password:", bg=self.controller.COLOUR, font=text_font)
        label_password.pack()
        entry_password = tk.Entry(self, show="*", font=text_font)
        entry_password.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=lambda: self.submit(entry_first_name.get(), entry_last_name.get(), entry_phone_number.get(),
                                                                        gender_var.get(), entry_email.get(), entry_password.get()), font=text_font, width=18,)
        submit_button.pack(pady=10)

        # Navigate to Login Page Button
        login_button = tk.Button(self, text="Go to Login", command=lambda: controller.show_frame(login_page.LoginPage), font=text_font,  width=15,)
        login_button.pack(pady=5)

    def submit(self, first_name, last_name, phone_number, gender, email, password):
        # Check if the fields are not empty
        if not first_name or not last_name or not phone_number or not gender or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Check if the email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address!")
            return

        # Check if the password is strong
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, and one digit!")
            return

        # Check if the email and password match a customer in the database
        query = "SELECT id FROM customers WHERE email = %s"
        Database.cursor.execute(query, (email,))
        result = Database.cursor.fetchone()

        if result:
            messagebox.showerror("Error", "Email already registered!")
        else:
            # Insert a new customer into the database
            password = self.hash_password(password)
            query = "INSERT INTO customers (first_name, last_name, phone_number, gender, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
            Database.cursor.execute(query, (first_name, last_name, phone_number, gender, email, password))
            Database.conn.commit()
            customer_id = Database.cursor.lastrowid
            self.controller.show_frame(home_page.HomePage, customer_id)

    def hash_password(self, password):
        # Hash a password for the first time, with a randomly-generated salt
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')