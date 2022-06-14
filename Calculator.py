from tkinter import*

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("544x744")
root.title("Calculator App")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(ipadx=8, padx=10, pady=10, fill=X)

f1 = Frame(root, bg="grey")
f1.pack()

nine = Button(f1, text="9", padx=28, pady=5, font="lucida 35 bold")
nine.pack(side=LEFT, padx=10, pady=5)
nine.bind("<Button-1>", click)
eight = Button(f1, text="8", padx=28, pady=5, font="lucida 35 bold")
eight.pack(side=LEFT, padx=10, pady=5)
eight.bind("<Button-1>", click)
seven = Button(f1, text="7", padx=28, pady=5, font="lucida 35 bold")
seven.pack(side=LEFT, padx=10, pady=5)
seven.bind("<Button-1>", click)

f2 = Frame(root, bg="grey")
f2.pack()

six = Button(f2, text="6", padx=28, pady=5, font="lucida 35 bold")
six.pack(side=LEFT, padx=10, pady=5)
six.bind("<Button-1>", click)
five = Button(f2, text="5", padx=28, pady=5, font="lucida 35 bold")
five.pack(side=LEFT, padx=10, pady=5)
five.bind("<Button-1>", click)
four = Button(f2, text="4", padx=28, pady=5, font="lucida 35 bold")
four.pack(side=LEFT, padx=10, pady=5)
four.bind("<Button-1>", click)

f3 = Frame(root, bg="grey")
f3.pack()

one = Button(f3, text="3", padx=28, pady=5, font="lucida 35 bold")
one.pack(side=LEFT, padx=10, pady=5)
one.bind("<Button-1>", click)
two = Button(f3, text="2", padx=28, pady=5, font="lucida 35 bold")
two.pack(side=LEFT, padx=10, pady=5)
two.bind("<Button-1>", click)
one = Button(f3, text="1", padx=28, pady=5, font="lucida 35 bold")
one.pack(side=LEFT, padx=10, pady=5)
one.bind("<Button-1>", click)

f4 = Frame(root, bg="grey")
f4.pack()

zero = Button(f4, text="0", padx=30, pady=5, font="lucida 35 bold")
zero.pack(side=LEFT, padx=10, pady=5)
zero.bind("<Button-1>", click)
add = Button(f4, text="+", padx=30, pady=5, font="lucida 35 bold")
add.pack(side=LEFT, padx=10, pady=5)
add.bind("<Button-1>", click)
subract = Button(f4, text="-", padx=29, pady=5, font="lucida 35 bold")
subract.pack(side=LEFT, padx=10, pady=5)
subract.bind("<Button-1>", click)

f5 = Frame(root, bg="grey")
f5.pack()

div = Button(f5, text="/", padx=30, pady=5, font="lucida 35 bold")
div.pack(side=LEFT, padx=10, pady=5)
div.bind("<Button-1>", click)
multiply = Button(f5, text = "*", padx=30, pady=5, font="lucida 35 bold")
multiply.pack(side=LEFT, padx=10, pady=5)
multiply.bind("<Button-1>", click)
equal = Button(f5, text="=", padx=30, pady=5, font="lucida 35 bold")
equal.pack(side=LEFT, padx=10, pady=5)
equal.bind("<Button-1>", click)

f6 = Frame(root, bg='grey')
f6.pack()

clear = Button(f6, text="C", padx=31, pady=5, font="lucida 35 bold")
clear.pack(side=LEFT, padx=10, pady=5)
clear.bind("<Button-1>", click)
dot = Button(f6, text=".", padx=31, pady=5, font="lucida 35 bold")
dot.pack(side=LEFT, padx=10, pady=5)
dot.bind("<Button-1>", click)
zeros = Button(f6, text="00", padx=31, pady=5, font="lucida 35 bold")
zeros.pack(side=LEFT, padx=10, pady=5)
zeros.bind("<Button-1>", click)


root.mainloop()