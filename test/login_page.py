import tkinter as tk
from tkinter import ttk
from tkinter import font
from database import Database
from tkinter import messagebox
import home_page
import register_page
import bcrypt

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Set the background color to light blue
        self.configure(bg=self.controller.COLOUR)

        label_title = tk.Label(self, text="Login Page", bg=self.controller.COLOUR, font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=(30,0))

        # Define font styles
        text_font = font.Font(family='Helvetica', size=12, weight='bold')

        # Email Address
        label_email = tk.Label(self, text="Email Address:", bg=self.controller.COLOUR, font=text_font)
        label_email.pack(pady=(30,0))
        entry_email = tk.Entry(self, font=text_font)
        entry_email.pack(pady=(5,15))

        # Password
        label_password = tk.Label(self, text="Password:", bg=self.controller.COLOUR, font=text_font)
        label_password.pack()
        entry_password = tk.Entry(self, show="*", font=text_font)
        entry_password.pack(pady=5)

        # Login Button
        login_button = tk.Button(self, text="Login", command=lambda: self.login(entry_email.get(), entry_password.get()), width=18,font=text_font)
        login_button.pack(pady=(20, 10))

        # Navigate to Sign Up Page Button
        sign_up_button = tk.Button(self, text="Go to Sign Up", command=lambda: controller.show_frame(register_page.RegisterPage), width=15, font=text_font)
        sign_up_button.pack(pady=5)

    def login(self, email, password):

        # Check if the email and password match a customer in the database
        # query = "SELECT id, password FROM customers WHERE email = %s"
        # Database.cursor.execute(query, (email,))
        # result = Database.cursor.fetchone()

        # if result:
        #     customer_id = result[0]
        #     hashed_password = result[1]

        #     if self.check_password(password, hashed_password):
        #         self.controller.show_frame(home_page.HomePage, customer_id)
        #         return

        # messagebox.showerror("Error", "Invalid email or password")
        self.controller.show_frame(home_page.HomePage, 10)
        

    def check_password(self, password, hashed_password):
        # Check that a unhashed password matches one that has previously been hashed
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))