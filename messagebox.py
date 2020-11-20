from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        self.master.geometry("400x400")
        self.btn = Button(master=self.master, text="popup", command=self.popup)
        self.btn.pack(pady=10)

        self.lbl = Label(master=self.master, text="")
        self.lbl.pack(pady=10)

    def popup(self):
        response = messagebox.askquestion("This is my popup", "Co tam?")
        if response == "yes":
            self.lbl.config(text="You clicked yes!")
        else:
            self.lbl.config(text="You clicked no!")


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
