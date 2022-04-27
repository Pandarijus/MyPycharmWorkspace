from tkinter import *

from tkinter.filedialog import asksaveasfile

ws = Tk()
ws.title("Python Guides")
ws.geometry('200x150')

def save_button():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)

btn = Button(ws, text = 'Save', command = lambda : save_button())
btn.pack(side = TOP, pady = 20)

ws.mainloop()