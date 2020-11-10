"""Python Tkinter GUI Tutorial #99
Text Box Widgets in Tkinter"""
from tkinter import *


class MultilineText(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")

        self.txtbox = Text(master, font='Arial')
        self.txtbox.grid(column=0, row=0, columnspan=2, pady=10, padx=10)

        self.btn_1 = Button(master, text="Clear", command=self.clear)
        self.btn_1.grid(column=0, row=1, pady=10, padx=10)
        self.btn_2 = Button(master, text="Get text", command=self.get_text)
        self.btn_2.grid(column=1, row=1, pady=10, padx=10)

    def clear(self):
        """Clear whole textbox"""
        self.txtbox.delete(1.0, END)

    def get_text(self):
        """Get data from textbox and print them as list"""
        data = self.txtbox.get(1.0, END)
        print(data.split())


if __name__ == '__main__':
    root = Tk()
    app = MultilineText(master=root)
    app.mainloop()
