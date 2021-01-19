import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

os.system('cls')

window = Tk()
window.title("Bulk Files Rename")
window.iconbitmap("./icon.ico")
window.resizable(width=False, height=False)
window.geometry("800x380")

def open_dir():
    e1.delete(0, END)
    global path
    global file_list
    path = filedialog.askdirectory() + "/"
    e1.insert(0,path)
    file_list = sorted(os.listdir(path))

count = 1

def rename():
    if e1.get() == '' or e3.get() == '':
        messagebox.showerror("Error","One or both fields are empty!")
        return
    if not os.path.exists(e1.get()):
        messagebox.showerror("Error","Invalid Path!")
        return
    if not file_list:
        messagebox.showerror("Error","No files in the selected folder!")
        return

    global count
    for file in file_list:
        if not os.path.isdir(path + file):
            fname, ext = os.path.splitext(file)
            os.rename(path + file, path + e3.get() + "-" + str(count) + ext)
            count += 1

    e1.delete(0, END)
    e3.delete(0, END)
    count = 1
    messagebox.showinfo(title="Success", message="Files Renamed Successfully!",)

label = Label(window, text="Bulk Files Rename", font="Bold, 24")
label.grid(row=0, column=1, padx=5, pady=20)

label1 = Label(window, text="Files Path: ", font="Bold, 10")
label1.grid(row=1, column=0, padx=10, pady=25)
e1 = Entry(width=100, borderwidth=1)
e1.grid(row=1, column=1)
btn1 = Button(window, text="Browse", font="Bold, 10", command=open_dir)
btn1.grid(row=1, column=2, padx=10, pady=25)

label3 = Label(window, text="Rename to: ", font="Bold, 10")
label3.grid(row=2, column=0, padx=10, pady=25)
e3 = Entry(width=100, borderwidth=1)
e3.grid(row=2, column=1)

btn3 = Button(window, text="Rename", font="Bold, 16", padx=20, pady=10, command=rename)
btn3.grid(row=3, column=1)

label4 = Label(window, text="AUTHOR: SEKTION", font="Bold")
label4.grid(row=4, column=1, padx=10, pady=40)

window.mainloop()