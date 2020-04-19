from tkinter import *
from tkinter import messagebox as msgb

oper_list = [["+","-"], ["%", "x"], ["0", "c"]]

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "x":
        text = "*"
    if text == "  =  ":
        if scvalue.get().isdigit():
            value = int(entry1.get())
        else:
            try:
                value = eval(entry1.get())
                scvalue.set(value)
            except:
                msgb.showinfo("Warning", "Alphabet cannot calculate, please enter Number and Operators only")
    elif text == " exit ":
        root.destroy()
    elif text == "c":
        scvalue.set("")
        entry1.update()
    else:
        scvalue.set(scvalue.get() + text)
        entry1.update()


lil = ["  =  ", " exit "]
op = 0
root = Tk()
root.minsize(330,380)
root.maxsize(330,380)
root.title("Calculator by Shaheer")
root.wm_iconbitmap("1.ico")
root.configure(bg="black", relief=SUNKEN, border=6)
root.geometry("330x380")



scvalue = StringVar()
scvalue.set("")


entry1 = Entry(root, textvar=scvalue, font="lucida 20 bold", relief=SUNKEN, border=3)
entry1.pack(pady=20)





for ixo in range(10, 3, -3):
    frame1 = Frame(root, bg="white")
    for ixox in range(1, 4):
        b = Button(frame1, text=str(ixo-ixox), font="lucida 18", bg="black", fg="white")
        b.pack(padx=10, pady=10, side=LEFT)
        b.bind("<Button-1>", click)
    for ni in oper_list[op]:
        b = Button(frame1, text=ni, font="lucida 18", bg="black", fg="white")
        b.pack(padx=10, pady=10, side=LEFT)
        b.bind("<Button-1>", click)
        if oper_list[op].index(ni) == 1:
            op += 1
    frame1.pack(padx=10, fill=X)

    
    
frame1 = Frame(root, bg="white")
for iii in range(2):
    b = Button(frame1, text=lil[iii], font="lucida 18", bg="black", fg="white")
    if lil[iii] == "  =  ":
        b.pack(padx=10, pady=10, side=LEFT)
    else:
        b.pack(padx=10, pady=10, side=RIGHT)
    b.bind("<Button-1>", click) 
frame1.pack(padx=50, fill=X)




root.mainloop()


