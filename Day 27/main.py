from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

def button_clicked():
    print("I got clicked")
    # label["text"] = "Button Got Clicked"
    new_text = input.get()
    label.config(text=new_text)

# Label

label = Label(text="I Am a Label")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me Too", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)






window.mainloop()