import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
from dataclasses import dataclass
from tkcalendar import Calendar
from datetime import datetime
from tktimepicker import AnalogPicker, AnalogThemes
from dataclasses import dataclass, field

HEIGHT = 600
WIDTH = 600


@dataclass
class Booking():
    service: any = field(default=None)
    date: any = field(default=None)
    time: any = field(default=None)

class Database():
    # def __init__(self):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nelldestroyer25",
        database="salon"
    )
    cursor = conn.cursor()

class SalonApp(tk.Tk):
    
    # __init__ function for class SalonApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(F"{HEIGHT}x{HEIGHT}")
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginPage, RegisterPage, HomePage, ServicePage, DatePicker, TimePicker):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(LoginPage)

    # to display the current frame passed as
    # parameter
    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

    def show_frame(self, cont, *arg):
        frame = self.frames[cont]
        if arg is not None and hasattr(frame, 'set_data'):
            frame.set_data(arg)
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
        # query = "SELECT customer_id FROM customers WHERE email = %s AND password = %s"
        # Database.cursor.execute(query, (email, password))
        # result = Database.cursor.fetchone()

        # if result:
        #     customer_id = result[0]
        #     self.controller.show_frame(HomePage, customer_id)
        # else:
        #     self.login_status_label.config(text="Invalid email or password", fg="red")
        self.controller.show_frame(HomePage, 9)


class RegisterPage(tk.Frame, Database):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent
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
        gender_var = tk.StringVar(value="")

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

        self.register_status_label = tk.Label(self, text="")
        self.register_status_label.pack()
        
    def submit(self, first_name,last_name,phone_number,gender,email,password):
        # Check if the email and password match a customer in the database
        query = "SELECT customer_id FROM customers WHERE email = %s"
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
            self.controller.show_frame(HomePage, customer_id)

class HomePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer_id = None

        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self, bg='light blue')
        style = ttk.Style()
        style.configure("Blue.TFrame", background="light blue")

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="Blue.TFrame")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar and the canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add the scrollable frame to the canvas at the center position
        self.canvas.create_window((WIDTH//2, HEIGHT), window=self.scrollable_frame, anchor="center")

        # Configure the scroll region of the canvas whenever its size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        label = ttk.Label(self.scrollable_frame, text ="Home", background="light blue", font=("Verdana", 35))
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        query = "SELECT service_id, name, description, price, duration, image FROM services"
        Database.cursor.execute(query, ())
        results = Database.cursor.fetchall()

        for i, result in enumerate(results):
            card = tk.Frame(self.scrollable_frame, relief=tk.RAISED, borderwidth=3)

            img = Image.open(result[5])
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=img)
            img_label.image = img
            img_label.grid(row=0, column=0, padx=30, pady=10)

            name_label = ttk.Label(card, text=result[1])
            name_label.grid(row=1, column=0)

            desc_label = ttk.Label(card, text=result[2], wraplength=300, background=card.cget('bg'))
            desc_label.grid(row=2, column=0)

            price_label = ttk.Label(card, text=result[3])
            price_label.grid(row=3, column=0)

            duration_label = ttk.Label(card, text=result[4])
            duration_label.grid(row=4, column=0, pady=10)

            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))

            card.bind("<Button-1>", lambda e, service=result: self.show_service_page(service))
            card.grid(row=i+1, column=0, pady=10)

    def set_data(self, customer_id):
        self.customer_id = customer_id[0]


    def show_service_page(self, service):
        # Show the ServicePage with the details of the selected service
        self.controller.show_frame(ServicePage, service, self.customer_id)

class ServicePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None

        # Configure the rows and columns to expand
        # for i in range(7):
        #     self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back)
        self.back_button.grid(row=0, column=0, padx=10, pady=10,)

        self.image_label = tk.Label(self)
        self.image_label.grid(row=1, column=0, )

        self.name_label = ttk.Label(self, anchor='center')
        self.name_label.grid(row=2, column=0,)

        self.desc_label = ttk.Label(self, anchor='center')
        self.desc_label.grid(row=3, column=0)

        self.price_label = ttk.Label(self, anchor='center')
        self.price_label.grid(row=4, column=0, )

        self.duration_label = ttk.Label(self, anchor='center')
        self.duration_label.grid(row=5, column=0, )

        self.book_button = ttk.Button(self, text="Book Appointment", command=self.book_appointment)
        self.book_button.grid(row=6, column=0,)

    def handle_back(self):
        self.controller.show_frame(HomePage, self.customer_id)

    def set_data(self, args):
        self.service = args[0]
        self.customer_id = args[1]

        # Load the image
        img = Image.open(self.service[5])
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

        # Update the labels with the service details
        self.name_label.config(text=self.service[1])
        self.desc_label.config(text=self.service[2])
        self.price_label.config(text=self.service[3])
        self.duration_label.config(text=self.service[4])

    def book_appointment(self):
        # Code to book an appointment
        self.controller.show_frame(DatePicker, self.service, self.customer_id)
        # query = "INSERT INTO bookings (customer_id, service_id) VALUES (%s, %s)"
        # Database.cursor.execute(query, (self.customer_id, self.service[0]))
        # Database.connection.commit()


class DatePicker(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None

        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back).pack(pady = 20)

        # Add Calendar
        self.cal = Calendar(self, selectmode = 'day',
                    year = currentYear, month = currentMonth,
                    day = currentDay,)


        self.cal.pack(pady = 20)
        
        # Add Button and Label
        tk.Button(self, text = "Get Date",
            command = self.send_date).pack(pady = 20)

    def handle_back(self):
        self.controller.show_frame(ServicePage, self.service, self.customer_id)

    def set_data(self, args):
        self.service = args[0]
        self.customer_id = args[1]

    def send_date(self):
        self.controller.show_frame(TimePicker, self.service, self.customer_id, self.cal.get_date())

class TimePicker(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None
        self.back_button = ttk.Button(self, text="Back", command=self.handle_back).pack(pady = 20)

        self.time_picker = AnalogPicker(self)
        self.time_picker.pack(expand=True, fill="both")

        theme = AnalogThemes(self.time_picker)
        theme.setNavyBlue()

        tk.Button(self, text = "Select Time",
                    command = self.send_time).pack(pady = 20)


    def handle_back(self):
        self.controller.show_frame(ServicePage, self.service, self.customer_id)

    def set_data(self, args):
        self.service = args[0]
        self.customer_id = args[1]
        self.date = args[2]

    def send_time(self):
        time = self.time_picker.time()
        print(self.time_picker.time())
        self.controller.show_frame(TimePicker, self.service, self.customer_id, self.date, self.time_picker.time())

        
class StylistPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.back_button = ttk.Button(self, text="Back", command=self.handle_back)
        self.back_button.pack(pady=10)

        self.stylists = ["Stylist 1", "Stylist 2", "Stylist 3"]  # replace with actual stylist names

        for stylist in self.stylists:
            button = ttk.Button(self, text=stylist, command=lambda stylist=stylist: self.select_stylist(stylist))
            button.pack(pady=10)

    def handle_back(self):
        self.controller.show_frame(TimePicker, self.service, self.customer_id, self.date)

    def select_stylist(self, stylist):
        # save the selected stylist and navigate to the booking page
        self.controller.selected_stylist = stylist
        self.controller.show_frame("BookingPage")  # replace with the name of the booking page    

app = SalonApp()
app.mainloop()

if __name__ == "__main__":
    app = SalonApp()
    app.mainloop()

# test@gmail.com
# pass