import tkinter as tk
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

def submit(first_name,last_name,phone_number,gender,email,password):

    # You can perform further validation or processing here
    # For now, let's just print the entered values
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Phone Number:", phone_number)
    print("Gender:", gender)
    print("Email:", email)
    print("Password:", password)

def login(email, password):
    # Check if the email and password match a customer in the database
    query = "SELECT customer_id FROM customers WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        customer_id = result[0]
        show_home_screen(customer_id)
    else:
        login_status_label.config(text="Invalid email or password", fg="red")

def login_screen():
    root = tk.Tk()
    root.title("Login")
    root.geometry("500x500")
    root.configure(padx=20, pady=20)

    def navigate_to_sign_up():
        root.destroy()
        sign_up_screen()

    # Email Address
    label_email = tk.Label(root, text="Email Address:")
    label_email.pack()
    entry_email = tk.Entry(root)
    entry_email.pack(pady=5)

    # Password
    label_password = tk.Label(root, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Login Button
    login_button = tk.Button(root, text="Login", command=lambda: login(entry_email.get(), entry_password.get()))
    login_button.pack(pady=10)

    # Navigate to Sign Up Page Button
    sign_up_button = tk.Button(root, text="Go to Sign Up", command=navigate_to_sign_up)
    sign_up_button.pack(pady=5)

    root.mainloop()

def sign_up_screen():
    root = tk.Tk()
    root.title("Sign Up")
    root.geometry("500x500")
    root.configure(padx=20, pady=20)

    def navigate_to_login():
        root.destroy()
        login_screen()

    # First Name
    label_first_name = tk.Label(root, text="First Name:")
    label_first_name.pack()
    entry_first_name = tk.Entry(root)
    entry_first_name.pack(pady=5)

    # Last Name
    label_last_name = tk.Label(root, text="Last Name:")
    label_last_name.pack()
    entry_last_name = tk.Entry(root)
    entry_last_name.pack(pady=5)

    # Phone Number
    label_phone_number = tk.Label(root, text="Phone Number:")
    label_phone_number.pack()
    entry_phone_number = tk.Entry(root)
    entry_phone_number.pack(pady=5)

    # Gender
    label_gender = tk.Label(root, text="Gender:")
    label_gender.pack()
    gender_var = tk.StringVar()

    gender_frame = tk.Frame(root)
    gender_frame.pack(pady=5)

    gender_button_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
    gender_button_male.pack(side=tk.LEFT)

    gender_button_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
    gender_button_female.pack(side=tk.LEFT)

    gender_button_other = tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")
    gender_button_other.pack(side=tk.LEFT)

    # Email Address
    label_email = tk.Label(root, text="Email Address:")
    label_email.pack()
    entry_email = tk.Entry(root)
    entry_email.pack(pady=5)

    # Password
    label_password = tk.Label(root, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit(entry_first_name.get(),entry_last_name.get(),entry_phone_number.get(),
                                                                  gender_var.get(),entry_email.get(),entry_password.get()))
    submit_button.pack(pady=10)

    # Navigate to Login Page Button
    login_button = tk.Button(root, text="Go to Login", command=navigate_to_login)
    login_button.pack(pady=5)

    root.mainloop()

# Call the login_screen function to display the login screen
login_screen()
