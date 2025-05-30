import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
