"""Python Tkinter GUI Tutorial #98
Spinboxes with Tkinter"""
import calendar
from tkinter import *


class Spinner(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        self.months = list(calendar.month_name[1:])

        # self.spinbox = Spinbox(master, from_=0, to=10, increment=2)
        self.spinbox = Spinbox(master, values=self.months)
        self.spinbox.pack(pady=10, padx=10)

        self.btn = Button(master, text="Submit", command=self.submit)
        self.btn.pack(pady=10, padx=10)
        self.lbl = Label(master, text="")
        self.lbl.pack(pady=10, padx=10)

    def submit(self):
        """Print spinbox value on screen"""
        spinbox_value = self.spinbox.get()
        self.lbl.config(text=f"You have chosen: {spinbox_value}")


if __name__ == '__main__':
    root = Tk()
    app = Spinner(master=root)
    app.mainloop()
