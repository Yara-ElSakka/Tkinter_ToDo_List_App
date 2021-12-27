# Tkinter ToDo list App
# by yara elsakka
# 27.12.21
# https://docs.python.org/3/library/tk.html
# https://colorhunt.co/

from tkinter import *

programScreen = Tk()

programScreen.title("Yara TodoList app 2021")
programScreen.geometry("600x500")
programScreen.resizable(1, 1)
programScreen.config(bg="#DB6B97")

yaras_first_button_widget = Button(text="close program",
                                   command=programScreen.destroy)

yaras_first_button_widget.pack()


mainloop()