from tkinter import *

from tkinter.filedialog import asksaveasfile

window = Tk()
window.title("TEXT TO SPEACH")
window.rowconfigure(0, minsize=1000, weight=0)
window.columnconfigure(1, minsize=800, weight=0)


def save_button():
	file = asksaveasfile(filetypes = [('Mp3', '*.mp3')],defaultextension = [('Mp3', '*.mp3')])
	if file:
		print(file.name)


text = Label(window,text ="English")
text.grid(row=0,column=0)

sl = Scale(window, from_=0, to=1,orient=HORIZONTAL, length= 60)
sl.grid(row=0,column=1)


text2 = Label(window,text = "Deutsch")
text2.grid(row=0,column=2)

btn = Button(window, text = 'Save', command =save_button)
btn.grid(row=0,column=0)

txt_edit = Text(window)
txt_edit.grid(row=1,column=0,sticky="nsew")


window.mainloop()



