from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate_button_clicked():
    mile = Miles_Input.get()
    km = float(mile) * 1.609344
    Markers_Label.config(text=int(km))


Miles_Input = Entry(width=7)
Miles_Input.grid(column=1, row=0)

Miles_Label = Label(text="Miles")
Miles_Label.grid(column=2, row=0)
Miles_Label.config(padx=50, pady=50)

Referencing_Label = Label(text="is equal to")
Referencing_Label.grid(column=0, row=1)
Referencing_Label.config(padx=30)

Markers_Label = Label(text="0")
Markers_Label.grid(column=1, row=1)

KM_Label = Label(text="Km")
KM_Label.grid(column=2, row=1)

Calculate_Button = Button(text="Calculate", command=calculate_button_clicked)
Calculate_Button.grid(column=1, row=2)

Markers_Label.config(text="0")







window.mainloop()
