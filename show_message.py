from tkinter import *   

from tkinter import messagebox
def show_warning():
    messagebox.showwarning("Alert", "Virus found on your computer")
root = Tk()
root.geometry("600x400")
root.title("Message")

bu = Button(root,text = "Click me", command=show_warning)
bu.pack()
root.mainloop()