"""Python Tkinter GUI Tutorial #100
Read And Write To text files"""
from tkinter import *
from tkinter import filedialog
import pathlib


class MultilineText(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")

        self.txtbox = Text(master, font="Arial")
        self.txtbox.grid(column=0, row=0, columnspan=2, pady=10, padx=10)

        self.btn_1 = Button(master, width=12, text="Clear", command=self.clear_text)
        self.btn_1.grid(column=0, row=1, pady=10, padx=10)
        self.btn_2 = Button(master, width=12, text="Get text", command=self.get_text)
        self.btn_2.grid(column=0, row=2, pady=10, padx=10)

        self.btn_3 = Button(
            master,
            width=12,
            text="Open file",
            command=lambda: FileHandler.load_data(FileHandler(), self.txtbox),
        )
        self.btn_3.grid(column=1, row=1, pady=10, padx=10)
        self.btn_4 = Button(
            master,
            width=12,
            text="Save to file",
            command=lambda: FileHandler.save_data(
                FileHandler(), self.txtbox.get(1.0, END)
            ),
        )
        self.btn_4.grid(column=1, row=2, pady=10, padx=10)

    def clear_text(self):
        """Clear whole textbox"""
        self.txtbox.delete(1.0, END)

    def get_text(self):
        """Get data from textbox"""
        data = self.txtbox.get(1.0, END)
        print(data)


class FileHandler:
    """Class to handle file loading and saving"""
    @staticmethod
    def get_file():
        options = dict(
            initialdir=pathlib.Path().absolute(),
            title="Choose files",
            filetypes=(("txt files", "*.txt"), ("all files", "*")),
        )
        return filedialog.askopenfilename(**options)

    def load_data(self, element):
        """Load data from a file"""
        file = self.get_file()
        with open(file, "r") as f:
            element.insert(1.0, f.read())

    def save_data(self, data):
        """Save data to a file"""
        file = self.get_file()
        with open(file, "w") as f:
            f.write(data)


if __name__ == "__main__":
    root = Tk()
    app = MultilineText(master=root)
    app.mainloop()
