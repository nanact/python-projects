import tkinter as tk  
from tkinter import ttk
from datetime import date

def result():
    name_for = full_name_input.get()
    
    text_box.insert(tk.END,"hi " + name_for)
    
    text_box.insert(tk.END,"\nwelcome to my application")
    
    text_box.insert(tk.END,"\nThe time is: "+str(date.today()))
    
    

window = tk.Tk()

window.title("application")

window.geometry("600x400")

ina = tk.Label(text = "Hi")

name = tk.Label(text="Your full name", bg = "blue", fg = "white")

full_name_input = ttk.Entry()

submit = ttk.Button(text = "submit", command=result)

text_box = tk.Text(state="normal")

ina.pack()

name.pack()

full_name_input.pack()

submit.pack()

text_box.pack()

window.mainloop()
