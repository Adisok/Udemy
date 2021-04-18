from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()

    new_data = {website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Ooopsie", message="Fill all the places, onii-chan!")
    else:
        try:
            with open("passwords.json", "r") as f:
                # Reading data
                data = json.load(f)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                # Saving updated data
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("passwords.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH OPTION ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Username: {data[website]['email']}\nPassword: "
                                                           f"{data[website]['password']}")
        else:
            messagebox.showinfo(title="ERROR", message="No details for the website")

                                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")

picture_window = Canvas(width=200, height=200)
picture_window.create_image(50, 100, image=logo)
picture_window.grid(row=0, column=1, sticky="E")

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="E")

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="E")

# Buttons
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="E")

generate_password_button = Button(text="Generate Password", width=17, command=generate_password)
generate_password_button.grid(row=3, column=1, columnspan=2, sticky="E")

search_button = Button(text="Search", width=17, command=find_password)
search_button.grid(row=1, column=1, sticky="E", columnspan=2)

# Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

username_entry = Entry(width=43)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")
username_entry.insert(0, "adisok@wp.pl")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

window.mainloop()
