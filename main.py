from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    user_search = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")

    else:
        if user_search in data:
            info = data[user_search]
            email = info["email"]
            password = info["password"]
            messagebox.showinfo(title=user_search, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for this website exists")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pw_letters + pw_symbols + pw_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    empty_field = len(website) == 0 or len(username) == 0 or len(password) == 0

    if empty_field:
        messagebox.showinfo(title="oops", message="Do not leave any fields blank!")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# Creates canvas with the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Creates all of the labels of text fields
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

username_text = Label(text="Email/Username:")
username_text.grid(column=0, row=2)

Password_text = Label(text="Password:")
Password_text.grid(column=0, row=3)

# Creates all the entry boxes
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "lewishudson@me.com")


password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)


# Creates all the buttons
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# is_okay = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details entered : "
#                                                                          f"\n username: {username_entry.get()} "
#                                                                          f"\nPassword: {password_entry.get()}\n"
#                                                                          f"Is it okay to save?")
