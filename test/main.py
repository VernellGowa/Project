import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dataclasses import dataclass
from datetime import datetime
import register_page
import login_page
import home_page

class SalonApp(tk.Tk):
    COLOUR = 'light blue'
    HEIGHT = 600
    WIDTH = 600 

    # __init__ function for class SalonApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(F"{self.HEIGHT}x{self.WIDTH}")
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (login_page.LoginPage, register_page.RegisterPage, home_page.HomePage):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(login_page.LoginPage)

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

if __name__ == "__main__":
    app = SalonApp()
    app.mainloop()

# test@gmail.com
# pass