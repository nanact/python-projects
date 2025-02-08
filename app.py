import tkinter as tk  
import tkinter as tkk
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

full_name_input = tkk.Entry()

submit = tkk.Button(text = "submit", command=result)

text_box = tkk.Text(state="normal")

ina.pack()

name.pack()

full_name_input.pack()

submit.pack()

text_box.pack()

window.mainloop()
