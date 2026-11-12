from tkinter import *
WHITE = "#FFFFFF"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg=WHITE)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.grid(column=1, row=0)

#Label
website_text = Label(text="Website:", bg=WHITE)
website_text.grid(column=0, row=1)
username_text = Label(text="Email/Username:", bg=WHITE)
username_text.grid(column=0, row=2)
password_text = Label(text="Password:", bg=WHITE)
password_text.grid(column=0, row=3)

#Entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)



logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
window.mainloop()
