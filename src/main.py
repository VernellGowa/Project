import tkinter as tk
from tkinter import ttk
import mysql.connector

class SalonApp(tk.Tk):
	
	# __init__ function for class SalonApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		self.geometry("500x500")
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (LoginPage, RegisterPage, HomePage):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(LoginPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		
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
		login_button = tk.Button(self, text="Login", command=lambda: self.login(entry_email.get(), entry_password.get()))
		login_button.pack(pady=10)

		self.login_status_label = tk.Label(self, text="")
		self.login_status_label.pack()

		# Navigate to Sign Up Page Button
		sign_up_button = tk.Button(self, text="Go to Sign Up", command=lambda: controller.show_frame(RegisterPage))
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

class RegisterPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.controller = controller

		# First Name
		label_first_name = tk.Label(self, text="First Name:")
		label_first_name.pack()
		entry_first_name = tk.Entry(self)
		entry_first_name.pack(pady=5)

		# Last Name
		label_last_name = tk.Label(self, text="Last Name:")
		label_last_name.pack()
		entry_last_name = tk.Entry(self)
		entry_last_name.pack(pady=5)

		# Phone Number
		label_phone_number = tk.Label(self, text="Phone Number:")
		label_phone_number.pack()
		entry_phone_number = tk.Entry(self)
		entry_phone_number.pack(pady=5)

		# Gender
		label_gender = tk.Label(self, text="Gender:")
		label_gender.pack()
		gender_var = tk.StringVar()

		gender_frame = tk.Frame(self)
		gender_frame.pack(pady=5)

		gender_button_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
		gender_button_male.pack(side=tk.LEFT)

		gender_button_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
		gender_button_female.pack(side=tk.LEFT)

		gender_button_other = tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")
		gender_button_other.pack(side=tk.LEFT)

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

		# Submit Button
		submit_button = tk.Button(self, text="Submit", command=lambda: self.submit(entry_first_name.get(), entry_last_name.get(), entry_phone_number.get(),
																	gender_var.get(), entry_email.get(), entry_password.get()))
		submit_button.pack(pady=10)

		# Navigate to Login Page Button
		login_button = tk.Button(self, text="Go to Login", command=lambda: controller.show_frame(LoginPage))
		login_button.pack(pady=5)
		
	def submit(self, first_name,last_name,phone_number,gender,email,password):
		# Check if the email and password match a customer in the database
		query = "SELECT customer_id FROM customers WHERE email = %s AND password = %s"
		cursor.execute(query, (email, password))
		result = cursor.fetchone()

		if result:
			customer_id = result[0]
			self.controller.show_frame(HomePage(customer_id))
		else:
			self.login_status_label.config(text="Invalid email or password", fg="red")

class HomePage(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Home")
			
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# # button to show frame 2 with text
		# # layout2
		# button1 = ttk.Button(self, text ="Page 1",
		# 					command = lambda : controller.show_frame(Page1))
	
		# # putting the button in its place by 
		# # using grid
		# button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# # button to show frame 3 with text
		# # layout3
		# button2 = ttk.Button(self, text ="Startpage",
		# 					command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		# button2.grid(row = 2, column = 1, padx = 10, pady = 10)

app = SalonApp()
app.mainloop()

if __name__ == "__main__":
	db = mysql.connector.connect(
		host="localhost",
		user="self",
		password="Nelldestroyer25",
		database="salon"
	)

	with db.cursor() as cursor:
		app = SalonApp()
		app.mainloop()