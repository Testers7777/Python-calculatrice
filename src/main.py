from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("by Testers7777")
root.iconbitmap("icon.ico")
root.config(background="#181028")

text = StringVar()
entry = Entry(root, width=30, borderwidth=5, state="readonly", textvariable=text)
entry.grid(row=0, column=1, columnspan=3)
entry.pack(pady=10)

def ajout(num):
    text.set(text.get() + str(num))

def clear():
    text.set('')

menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau calcul (esc)", command=clear)
menu1.add_separator()
menu1.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Fenêtre", menu=menu1)

root.config(menu=menubar)

import ast

def exp(expression):
    try:
        parsed_expression = ast.parse(expression, mode='eval')
        result = eval(compile(parsed_expression, '', 'eval'))
        return result
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        return "Erreur"

def evala():
    expression = text.get()
    result = exp(expression)
    text.set(result)

def type(num):
    text.set(text.get() + num)


root.geometry("300x275")

root.config(cursor="spider")

def clavier(event):
    bind = event.keysym

    if bind == "Return":
        evala()

    if bind == "BackSpace":
        oldtext = text.get()
        text.set(oldtext[:-1])

    if bind == "Escape":
        clear()

    if bind.isdigit() or bind == "plus" or bind == "minus" or bind == "asterisk" or bind == "x" or bind == "period" or bind == "comma" or bind == "slash":
            text.set(text.get() + bind.replace("plus", "+").replace("minus", "-").replace("slash", "/").replace("asterisk", "*").replace("x", "*").replace("comma", ".").replace("period", "."))


row1 = Frame(root)
row1.pack()
row2 = Frame(root)
row2.pack()
row3 = Frame(root)
row3.pack()
row4 = Frame(root)
row4.pack()
row5 = Frame(root)
row5.pack()

# Ligne 1 : Boutons 7, 8, 9
button7 = Button(row2, text='7', borderwidth=1, height=1, width=3, command=lambda: type("7"))
button8 = Button(row2, text='8', borderwidth=1, height=1, width=3, command=lambda: type("8"))
button9 = Button(row2, text='9', borderwidth=1, height=1, width=3, command=lambda: type("9"))
buttonx = Button(row2, text='*', borderwidth=1, height=1, width=3, command=lambda: type("*"))

button9.config(bg="#2c2446", fg="#fff")
button9.pack(side=LEFT, padx=5, pady=5)
button8.config(bg="#2c2446", fg="#fff")
button8.pack(side=LEFT, padx=5, pady=5)
button7.config(bg="#2c2446", fg="#fff")
button7.pack(side=LEFT, padx=5, pady=5)
buttonx.config(bg="#2c2446", fg="#fff")
buttonx.pack(side=LEFT, padx=5, pady=5)

# Ligne 2 : Boutons 4, 5, 6
button4 = Button(row3, text='4', borderwidth=1, height=1, width=3, command=lambda: type("4"))
button5 = Button(row3, text='5', borderwidth=1, height=1, width=3, command=lambda: type("5"))
button6 = Button(row3, text='6', borderwidth=1, height=1, width=3, command=lambda: type("6"))
buttonm = Button(row3, text='-', borderwidth=1, height=1, width=3, command=lambda: type("-"))

button4.config(bg="#2c2446", fg="#fff")
button4.pack(side=LEFT, padx=5, pady=5)
button5.config(bg="#2c2446", fg="#fff")
button5.pack(side=LEFT, padx=5, pady=5)
button6.config(bg="#2c2446", fg="#fff")
button6.pack(side=LEFT, padx=5, pady=5)
buttonm.pack(side=LEFT, padx=5, pady=5)
buttonm.config(bg="#2c2446", fg="#fff")

# Ligne 3 : Boutons 1, 2, 3
button1 = Button(row4, text='1', borderwidth=1, height=1, width=3, command=lambda: type("1"))
button2 = Button(row4, text='2', borderwidth=1, height=1, width=3, command=lambda: type("2"))
button3 = Button(row4, text='3', borderwidth=1, height=1, width=3, command=lambda: type("3"))
buttonp = Button(row4, text='+', borderwidth=1, height=1, width=3, command=lambda: type("+"))

button1.config(bg="#2c2446", fg="#fff")
button1.pack(side=LEFT, padx=5, pady=5)
button2.config(bg="#2c2446", fg="#fff")
button2.pack(side=LEFT, padx=5, pady=5)
button3.config(bg="#2c2446", fg="#fff")
button3.pack(side=LEFT, padx=5, pady=5)
buttonp.config(bg="#2c2446", fg="#fff")
buttonp.pack(side=LEFT, padx=5, pady=5)

buttoncom = Button(row5, text=',', borderwidth=1, height=1, width=3, command=lambda: type("."))
button0 = Button(row5, text='0', borderwidth=1, height=1, width=3, command=lambda: type("0"))
buttoneq = Button(row5, text='=', borderwidth=1, height=1, width=3, command=evala)
buttond = Button(row5, text='/', borderwidth=1, height=1, width=3, command=lambda: type("/"))

button0.config(bg="#2c2446", fg="#fff")
button0.pack(side=LEFT, padx=5, pady=5)
buttoncom.config(bg="#2c2446", fg="#fff")
buttoncom.pack(side=LEFT, padx=5, pady=5)
buttoneq.config(bg="#2c2446", fg="#fff")
buttoneq.pack(side=LEFT, padx=5, pady=5)
buttond.config(bg="#2c2446", fg="#fff")
buttond.pack(side=LEFT, padx=5, pady=5)

root.bind('<KeyPress>', clavier)

root.mainloop()