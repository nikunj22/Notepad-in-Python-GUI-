from tkinter import *
from tkinter import filedialog

win=Tk()
win.title("MY Notepad")
win.geometry("500x500")

def savefile():
    openfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if openfile is None:
        return
    text=str(entry.get(1.0,END))
    openfile.write(text)
    openfile.close()

def clear():
    entry.delete(1.0,END)


def openfile():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

    
bsavefile=Button(win,text="Save File",command=savefile)
bsavefile.place(x=10,y=10)

bclear=Button(win,text="Clear All",command=clear)
bclear.place(x=70,y=10)

bopenfile=Button(win,text="Open File",command=openfile)
bopenfile.place(x=130,y=10)

entry=Text(win,height=50,width=60,wrap=WORD)
entry.place(x=10,y=50)

win.mainloop()