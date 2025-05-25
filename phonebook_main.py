#Python Ver: 3.11.7
#
#Author: Duncan McCabe
#
#Purpose:   Phonebook Demo. Demostration OOP, Tkinter GUI module, using Tkinter Parent and Child relationship.,
#
#Tested OS:     This code was written and tested to wotk with Windows 11.,
from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from,
class ParentWindow(Frame):
    def init(self, master, *args, **kwargs):
        Frame.init(self,master,args, **kwargs)

        # define our msater frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#f0f0f0")
        # This protocol methor is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" con Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)


if name == "main":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
