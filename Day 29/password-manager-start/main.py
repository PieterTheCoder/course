from tkinter import *
from tkinter import messagebox

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_output = website_entry.get()
    email_output = email_entry.get()
    password_output = password_entry.get()


    with open("data.txt", "a") as data:
        data.write(f"{website_output} | {email_output} | {password_output}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "pieter@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Button
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()