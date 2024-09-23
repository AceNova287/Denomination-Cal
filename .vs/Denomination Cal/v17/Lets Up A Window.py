from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")
def topwin():
    top = Toplevel()
    top.geometry("100x100")
    top.title("toplevel")
    l2 = Label(top, text = "this is the toplevel window")
    l2.pack

    top.mainloop()

l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window")
l.pack()
btn.pack()