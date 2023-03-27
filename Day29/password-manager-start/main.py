from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) ==0 :
        messagebox.showerror(title="Oops!", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: "
                                               f"{password}\nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=36)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
website_input.focus()

email_input = Entry(width=36)
email_input.grid(row=2, column=1, columnspan=2, sticky=EW)
email_input.insert(0, "solanki.tanish57@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)

# Buttons
generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(row=3, column=2, sticky=EW)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()

"""
the EW part is the compass directions (E)ast and (W)est and the sticky basically "sticks" the widget to the edges of the
column.  Sweet.  So this instruction spans the widget to fill the whole width of the grid column/s. This means we don't 
need to experiment with absolute pixel values for the widgets except for the longest one (add), which determines the 
size of the last column.
"""