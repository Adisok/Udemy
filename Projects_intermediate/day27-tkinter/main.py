from tkinter import *

def button_clicked():
    text = input.get()
    my_label.config(text=text)
    print("I got Clicked")


window = Tk()
window.title("First GUI")
window.minsize(width=500, height= 300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

my_label.config(text="Newer texgt")
my_label.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)

# Button
button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="2Click me2", command=button_clicked)
button2.grid(column=2, row=0)
window.mainloop()

