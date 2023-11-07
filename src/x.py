import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector
import hashlib  # For password hashing

class SalonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salon - Login")
        self.root.geometry("500x500")

        self.create_login_screen()

    def create_login_screen(self):
        # Create a frame to group login elements
        login_frame = tk.Frame(self.root)
        login_frame.pack()

        # Email entry
        email_label = tk.Label(login_frame, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(login_frame)
        self.email_entry.pack()

        # Password entry
        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.pack()

        # Login button
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.pack()

        # Sign-up button
        sign_up_button = tk.Button(login_frame, text="Sign Up", command=self.create_signup_screen)
        sign_up_button.pack()

        # Login status label
        self.login_status_label = tk.Label(login_frame, text="")
        self.login_status_label.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check if the email and hashed password match a customer in the database
        query = "SELECT customer_id, password FROM customers WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result:
            customer_id, stored_password = result
            if hashlib.sha256(password.encode()).hexdigest() == stored_password:
                self.show_home_screen(customer_id)
            else:
                self.login_status_label.config(text="Invalid email or password", fg="red")
        else:
            self.login_status_label.config(text="Invalid email or password", fg="red")


    def create_signup_screen(self):
        # Create a frame to group sign-up elements
        self.root.destroy()
        signup_frame = tk.Frame(self.root)
        signup_frame.pack()

        # Full Name entry
        full_name_label = tk.Label(signup_frame, text="Full Name:")
        full_name_label.pack()
        self.full_name_entry = tk.Entry(signup_frame)
        self.full_name_entry.pack()

        # Email entry
        email_label = tk.Label(signup_frame, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(signup_frame)
        self.email_entry.pack()

        # Password entry
        password_label = tk.Label(signup_frame, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(signup_frame, show="*")
        self.password_entry.pack()

        # Sign-up button
        signup_button = tk.Button(signup_frame, text="Sign Up", command=self.register_user)
        signup_button.pack()

        # Sign-up status label
        self.signup_status_label = tk.Label(signup_frame, text="")
        self.signup_status_label.pack()

    def register_user(self):
        full_name = self.full_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not (full_name and email and password):
            self.signup_status_label.config(text="Please fill in all fields", fg="red")
            return

        # Check if the email is already registered
        query = "SELECT customer_id FROM customers WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result:
            self.signup_status_label.config(text="Email is already registered", fg="red")
        else:
            # Hash the password before storing it in the database
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Insert the new customer into the database
            query = "INSERT INTO customers (full_name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (full_name, email, hashed_password))
            db.commit()  # Commit the transaction

            self.signup_status_label.config(text="Registration successful!", fg="green")

    def show_home_screen(self, customer_id):
        # Destroy the login screen
        # login_screen.destroy()

        # Create the home screen
        home_screen = tk.Tk()
        home_screen.title("Salon - Home")
        home_screen.geometry("500x500")

        # Get all services from the database
        query = "SELECT service_id, name, price FROM services"
        cursor.execute(query)
        services = cursor.fetchall()

        # Display services
        services_label = tk.Label(home_screen, text="Services")
        services_label.pack()

        for service in services:
            service_label = tk.Label(
                home_screen,
                text=f"{service[1]} - ${service[2]:.2f}",
                padx=10,
                pady=5
            )
            service_label.pack()

        home_screen.mainloop()

if __name__ == "__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nelldestroyer25",
        database="salon"
    )

    # Use a context manager for the cursor
    with db.cursor() as cursor:
        app = SalonApp(tk.Tk())
        tk.mainloop()
