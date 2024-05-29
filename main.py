from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_passowrd():
    pass_entry.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    we = web_entry.get()
    eme = email_entry.get()
    passe = pass_entry.get()

    if len(passe) == 0 or len(we) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any feilds empty")
    else:
        is_ok = messagebox.askokcancel(title=we, message=f"These are the details enetered: \nEmail: {eme} \nPassowrd: {passe}\n Is this okay?")

        if is_ok:
            with open("data.txt" , "a") as f:
                f.write(f"{we} | {eme} | {passe} \n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200 , height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)


#LABELS
website_name = Label(text="Website: " , font=("Arial", 12, "bold"))
email_label = Label(text="Email/Username: ", font=("Arial", 12, "bold"))
pass_l = Label(text="Password: ", font=("Arial", 12, "bold"))


#ENTRIES
web_entry = Entry(width=35)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, "sud@gmail.com")
pass_entry = Entry(width=21)

#BUTTONS
gen_b = Button(text="Generate password", font=("Arial", 12, "normal"), command=generate_passowrd)
add_b = Button(width=36, text="Add", command=save)

website_name.grid(column=0, row=1)
email_label.grid(column=0, row=2)
pass_l.grid(column=0, row=3)

web_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)

gen_b.grid(row=3, column=2)
add_b.grid(row=4, column=1, columnspan=2)

window.mainloop()