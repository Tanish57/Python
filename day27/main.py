# import tkinter need to type tkinter.Label, tkinter.Button, instead use:
from tkinter import *

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    # window.mainloop(exit())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx= 30, pady=20)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="I'm New", command=print("Clicked Me"))
new_button.grid(column=0, row=3)

# Entry
input = Entry(width=10)
input.grid(column=3, row=4)
print(input.get())

window.mainloop()