from tkinter import *


def calculate():
    label4.config(text=f"{int(miles.get())*1.6}")


window = Tk()
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="Km")
label2.grid(column=2, row=1)

label3 = Label(text="is equal to")
label3.grid(column=0, row=1)

miles = Entry(width=10)
miles.grid(column=1, row=0)

label4 = Label(text=0)
label4.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
