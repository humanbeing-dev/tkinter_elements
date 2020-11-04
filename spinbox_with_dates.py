"""Application of tkinter Spinbox widget for changing data"""
from tkinter import *
import datetime
import time


class SpinDate(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.up_or_down = self.master.register(self.add_day)
        self.dir_dict = {"up": 1, "down": -1}
        self.create_widgets()
        self.set_today_date()

    def create_widgets(self):
        self.spin = Spinbox(self.master, command=(self.up_or_down, '%d'))
        self.spin.pack(padx=10, pady=10)

    def set_today_date(self):
        self.today = time.strftime("%Y-%m-%d", time.gmtime())   # str
        self.spin.insert(0, self.today)

    def add_day(self, direction):
        self.cur_day = self.spin.get()
        date = datetime.datetime.strptime(self.cur_day, "%Y-%m-%d") + datetime.timedelta(self.dir_dict[direction])
        date_str = datetime.datetime.strftime(date, "%Y-%m-%d")
        self.spin.delete(0, END)
        self.spin.insert(0, date_str)


if __name__ == '__main__':
    root = Tk()
    app = SpinDate(master=root)
    app.mainloop()




