from tkinter import *
from tkinter import filedialog


def get_file_path():
    global file_path1

    file_path1 = filedialog.askopenfilename(title="Select A File", filetypes=(
    ("Python files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    l1 = Label(ws, text="File path: " + file_path1).pack()


ws = Tk()
ws.title("Python Guides")
ws.geometry("200x200")

button = Button(ws, text="openfile", command=get_file_path).pack(pady=10)
ws.mainloop()
print(file_path1)