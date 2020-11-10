"""Python Tkinter GUI Tutorial #101 and #102
Add images to Text Box Widgets and
Text Widget Bold and Italics
"""
from tkinter import *
from tkinter import filedialog
from tkinter import font
import pathlib
from PIL import ImageTk, Image


class MultilineText(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")

        # Create Frame
        self.my_frame = Frame(self.master)
        self.my_frame.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        # Create scrollbar
        self.scroll = Scrollbar(self.my_frame)
        self.scroll.pack(side=RIGHT, fill=Y, expand=1)

        self.txtbox = Text(
            self.my_frame,
            font="Arial",
            selectbackground="yellow",
            selectforeground="black",
            yscrollcommand=self.scroll.set,
        )
        self.txtbox.pack()

        self.scroll.config(command=self.txtbox.yview)

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

        self.btn_5 = Button(
            master, width=12, text="Load Picture", command=self.load_image
        )
        self.btn_5.grid(column=2, row=1, pady=10, padx=10)

        self.edition_frame = Frame(master=master, width=12)
        self.edition_frame.grid(column=2, row=2, pady=10, padx=10)
        self.btn_b = Button(self.edition_frame, width=4, text="B", command=self.bold_text)
        self.btn_b.grid(column=0, row=0, pady=10)
        self.btn_i = Button(self.edition_frame, width=4, text="I", command=self.italic_text)
        self.btn_i.grid(column=1, row=0, pady=10)

    def clear_text(self):
        """Clear whole textbox"""
        self.txtbox.delete(1.0, END)

    def get_text(self):
        """Get data from textbox"""
        data = self.txtbox.get(1.0, END)
        test = self.txtbox.selection_get()

    def bold_text(self):
        """Make selected text bold"""
        bold_font = font.Font(self.txtbox, self.txtbox.cget("font"))
        bold_font.configure(weight="bold")

        self.txtbox.tag_config("bold", font=bold_font)

        current_tags = self.txtbox.tag_names("sel.first")

        if "bold" in current_tags:
            self.txtbox.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.txtbox.tag_add("bold", "sel.first", "sel.last")

    def italic_text(self):
        """Make selected text italic"""
        italic_font = font.Font(self.txtbox, self.txtbox.cget("font"))
        italic_font.configure(slant="italic")

        self.txtbox.tag_config("italic", font=italic_font)

        current_tags = self.txtbox.tag_names("sel.first")

        if "italic" in current_tags:
            self.txtbox.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.txtbox.tag_add("italic", "sel.first", "sel.last")

    def load_image(self):
        global img
        img = PhotoImage(file="img/volume5.png")
        position = self.txtbox.index(INSERT)
        print(position)
        self.txtbox.image_create(position, image=img)


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
