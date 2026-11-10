from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
import pyperclip

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [
        random.choice(letters) for _ in range(random.randint(8, 10))
    ]

    password_symbols = [
        random.choice(symbols) for _ in range(random.randint(2, 4))
    ]

    password_numbers = [
        random.choice(numbers) for _ in range(random.randint(2, 4))
    ]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def delete_entry():
    website_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()

def save ():
    website = website_input.get().strip()
    email = email_input.get()
    password = password_input.get()

    if "" in (website, password, email):
        messagebox.showerror(title="Oops", message="please don't leave any fields empty! ")

        return

    is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered \nEmail:{email} " f"\n {password} \n is it ok to save? ")

    if is_ok:

        with open("data.txt") as content:
            if website not in content.read():
                with open("data.txt", mode="a") as file:
                        content = f"{website}  | {email} | {password} \n"
                        file.write(content)
                delete_entry()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Website Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, padx=3, pady=3)

# Website Entry
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew", padx=3, pady=3)
website_input.focus()

# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=3, pady=3)


# Email Entry
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew", padx=3, pady=3)
email_input.insert(0, "yemi@gmail.com")

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, padx=3, pady=3)

# Password Entry
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew", padx=3, pady=3)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew", padx=3, pady=3)

# Add Button
add_button = Button(text="Add", width=36, command=save )
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=3, pady=3)

window.mainloop()
