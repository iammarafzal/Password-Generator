from tkinter import *
from tkinter import ttk
import string
import random

class Window():
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x235+60+60")
        self.root.title("Password Generator")
        self.root.resizable(False, False)

        self.plen = IntVar()

        lblEntry = Label(self.root, text="Enter Password length: ", font=("Arial", 12, "bold"), pady=10)
        lblEntry.pack(side=TOP, fill=X)
        lblEntry.place(x=15, y=5)

        self.TextBox = Entry(self.root, font=("Arial", 13), bg="white", width=13, textvariable=self.plen, validate="key", validatecommand=(self.root.register(self.validate_input), '%P'))
        self.TextBox.place(x=212, y=15)

        lblOutputTextHere = Label(self.root, text="Your Password Here:", font=("Arial", 12, "bold"))
        lblOutputTextHere.place(x=15, y=90)

        self.DataFrame_output = Frame(self.root, bg='white', width=330, height=110)
        self.DataFrame_output.place(x=10, y=120)

        self.OutputTextBox = Text(self.DataFrame_output, font=("Arial", 13), bg="white", width=37, height=4)
        self.OutputTextBox.place(x=0, y=0)

        # ------------------- Buttons -------------------
        btnGenerate = Button(self.root, text="Generate", font=("Arial", 11, "bold"), width=8, bg="green", fg="white", command=self.password_gen)
        btnGenerate.place(x=140, y=50)

        btnCopy = Button(self.DataFrame_output, text="Copy", font=("Arial", 9, "bold"), width=8, bg="black", fg="white", command=self.copy_output_text)
        btnCopy.place(x=260, y=83)


    # Function to validate the input (ensuring only integers)
    def validate_input(self, new_value):
        if new_value == "" or new_value.isdigit():  # Allow empty value or integer input
            return True
        return False


    # ------------------- Functionality -------------------
    def password_gen(self):
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation

        plen = self.plen.get()
        if plen == 0:
            self.OutputTextBox.delete("1.0", END)
            self.OutputTextBox.insert(END, "Enter a valid length!")
            return

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)

        if plen > len(s):
            self.OutputTextBox.delete("1.0", END)
            self.OutputTextBox.insert(END, "Length exceeds available characters!")
            return

        password = ("".join(random.sample(s, plen)))

        self.OutputTextBox.delete("1.0", END)
        self.OutputTextBox.insert(END, password)

    
    def copy_output_text(self):
        output_text = self.OutputTextBox.get("1.0", END).strip()
        if output_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_text)
            self.root.update()


if __name__ == '__main__':
    root = Tk()
    Window(root)
    root.mainloop()
