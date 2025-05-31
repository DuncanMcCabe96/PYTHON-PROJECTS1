import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label above entry
        self.label = Label(self.master, text="Enter your custom text below")
        self.label.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(20, 0))

        # Entry field for custom text
        self.custom_txt = Entry(width=90)
        self.custom_txt.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(5, 0))

        # Default HTML page button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(50, 5), pady=(30, 0))

        # Submit Custom Text button (linked to customHTML method)
        self.Submitbtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.Submitbtn.grid(row=2, column=2, padx=(50, 5), pady=(30, 0))

    def defaultHTML(self):
        htmlText = "Stay tuned for our AMAZING summer sale!"
        self.createHTML(htmlText)

    def customHTML(self):
        # Get text from entry field
        htmlText = self.custom_txt.get()
        if htmlText.strip() == "":
            htmlText = "You submitted an empty field."
        self.createHTML(htmlText)

    def createHTML(self, htmlText):
        # Writes HTML and opens in browser
        with open("index.html", "w") as htmlFile:
            htmlContent = f"<html>\n<body>\n<h1>{htmlText}</h1>\n</body>\n</html>"
            htmlFile.write(htmlContent)
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
