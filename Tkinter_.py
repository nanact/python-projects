
from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry("600x400")

bu = Button(text = "Click me")
bu.pack()

def Bind_Hander(event):
    print(event.char)

root.bind("<Key>",Bind_Hander)

def Hander_Button(event):
    print("Button is clicked")

bu.bind("<Button-1>",Hander_Button)
root.mainloop()