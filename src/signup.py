import tkinter as tk

def submit():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    gender = gender_var.get()
    email = entry_email.get()
    password = entry_password.get()

    # You can perform further validation or processing here
    # For now, let's just print the entered values
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Phone Number:", phone_number)
    print("Gender:", gender)
    print("Email:", email)
    print("Password:", password)

def signup_screen():
    root = tk.Tk()
    root.title("Sign In")
    root.geometry("500x500")
    root.configure(padx=20, pady=20)

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
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=10)

    root.mainloop()

# Call the signup_screen function to display the signup screen
signup_screen()
