import library
from Tkinter import *




def donothing():
    pass

def buildwindow():
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

    return root

def adddropdowns(window):
    global lib
    Label(window, text="Patron Name").grid(row=1)
    cust = StringVar()
    try:
        cust.set(lib.getPatrons()[0])
        OptionMenu(window, cust, *lib.getPatrons(), command=donothing()).grid(row=1, column=1)
    except:
        cust.set("You have no Patrons")
        OptionMenu(window, cust, "You have no Patrons", *lib.getPatrons(), command=donothing()).grid(row=1, column=1)
       
    Label(window, text="Action").grid(row=2)
    global act
    act.set(actions()[1])
    Button(window, text="-", command=takeAction(act.get())).grid(row=3)
    
    OptionMenu(window, act, *actions(), command=namebutton).grid(row=2, column=1)
    global bookType
    try:
        bookType.set(books()[0])
        OptionMenu(window, bookType, *books(), command=selectbook).grid(row=1,column=2)
    except:
        bookType.set("Great library...no books")
        OptionMenu(window, bookType, "Great library...no books", *books(), command=selectbook).grid(row=1,column=2)
    
    

def namebutton(event):
    global act, root
    root.grid_slaves(row=3, column=0)[0]["text"]=act.get()
    return 

def actions():
    varlist = []
    varlist.append("Check In")
    varlist.append("Check Out")
    return varlist

def books():
    varlist =[]
    varlist.append("All Overdue")
    varlist.append("Overdue Patrons")
    varlist.append("Checked out Items")
    varlist.append("All Items")
    return varlist

def takeAction(stringer):
    pass

def selectbook(event):
    pass
    

lib = library.Library()
lib.loadCatalog('filename')
lib.loadPatrons('filename2')
root = buildwindow()
act = StringVar()
bookType = StringVar()
adddropdowns(root)
root.mainloop()

