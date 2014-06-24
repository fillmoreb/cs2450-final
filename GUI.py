import library
from Tkinter import *



def donothing():
    pass

root = Tk()
root.title("Books Read Good")

menu = Menu(root, tearoff = 0)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)







root.mainloop()

