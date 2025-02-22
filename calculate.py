from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
amount = 0
ROOT = Tk()
ROOT.geometry("600x400")
Upload =  Image.open("Money.jpg")
Upload = Upload.resize((300, 300))
image = ImageTk.PhotoImage(Upload)
label = Label(ROOT, image = image)
label.place(x = 100, y = 200)

def msg():
    MagBox = messagebox.showinfo(
        "Alert", "Do you wanto to calculate the denomination count")
    if MagBox == "ok":
            topwin()
button = Button(ROOT, text = "Let's get started", command = msg)
button.place(x = 200, y = 200)
    
def topwin():
        top = Toplevel()
        top.title("Denominator calculator")
        top.geometry("600x350+50+50")
        label = Label(top, text="Enter Amount")
        entry  = Entry(top)
        lbl = Label(top, text = "Here are number of notes for each denominator")
        l1 = Label(top, text = "500")
        l2 = Label(top , text = "100")
        t1 = Entry(top)
        t2 = Entry(top)
        def calculator():
            try:
                global amount
                amount = int(entry.get())
                note500 = amount // 500
                amount %= 500
                note100 = amount // 100
                t1.delete(0, END)
                t2.delete(0, END)
                t1.insert(END, str(note500))
                t2.insert(END, str(note100))
            except ValueError:
                messagebox.showerror("Error", "There seem to be a problem")
        btn = Button(top , text = "calcukate", command=calculator) 
        label.place(x = 230, y = 15 )
        entry.place(x = 200, y = 80)
        btn.place(x = 240, y = 100)
        lbl.place(x = 140, y = 170)
        l1.place(x = 180, y = 200)
        l2.place(x = 180, y = 230)
        t1.place(x = 270, y = 200)
        t2.place(x = 270, y = 230)
        top.mainloop()
ROOT.mainloop()