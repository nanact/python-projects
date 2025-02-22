from tkinter import *
from tkinter import filedialog, messagebox



def new_file():
    text_area.delete(1.0, END)
    
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text doc", "*.txt"), ("python", "*py")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, END)
            text_area.insert(END, file.read())
            root.title(f"My text editor -- {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text doc")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))
            root.title(f"My text editor -- {file_path}")

root = Tk()
root.title("Text Editor")
root.geometry("600x400")

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
menu_bar.add_cascade(label = "file", menu=file_menu)
root.config(menu = menu_bar)

text_area = Text()
text_area.pack(expand = True, fill=BOTH)
root.mainloop()