import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nelldestroyer25",
    database="salon"
)


# Create a cursor to execute SQL queries
cursor = db.cursor()


def login():
    email = email_entry.get()
    password = password_entry.get()

    # Check if the email and password match a customer in the database
    query = "SELECT customer_id FROM customers WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        customer_id = result[0]
        show_home_screen(customer_id)
    else:
        login_status_label.config(text="Invalid email or password", fg="red")


def show_home_screen(customer_id):
    # Destroy the login screen
    login_screen.destroy()

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


def sign_up():
    sign_up_screen = tk.Toplevel(login_screen)
    sign_up_screen.title("Salon - Sign Up")
    sign_up_screen.geometry("500x500")

    # Add sign-up UI elements here

    sign_up_screen.mainloop()


# Create the login screen
login_screen = tk.Tk()
login_screen.title("Salon - Login")
login_screen.geometry("500x500")

# Email entry
email_label = tk.Label(login_screen, text="Email:")
email_label.pack()
email_entry = tk.Entry(login_screen)
email_entry.pack()

# Password entry
password_label = tk.Label(login_screen, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_screen, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(login_screen, text="Login", command=login)
login_button.pack()

# Sign-up button
sign_up_button = tk.Button(login_screen, text="Sign Up", command=sign_up)
sign_up_button.pack()

# Login status label
login_status_label = tk.Label(login_screen, text="")
login_status_label.pack()

login_screen.mainloop()