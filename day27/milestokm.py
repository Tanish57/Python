from tkinter import *

def button_clicked():
    user = input.get()
    calculation = float(user) * 1.609
    output.config(text=calculation)

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

is_equals = Label(text="is equal to")
is_equals.grid(column=0, row=1)

input = Entry(width=10)
# input.config(padx=100, pady = 20)
input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

output = Label(text="0")
output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1,row=2)

window.mainloop()