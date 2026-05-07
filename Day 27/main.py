from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label

label = Label(text="I Am a Label")
label.pack()

# Button

def button_clicked():
    print("I got clicked")
    label["text"] = "Button Got Clicked"
    label.config(text="Button Got Clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()







window.mainloop()