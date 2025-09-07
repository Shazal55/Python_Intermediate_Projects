#--------------------Password Generator------------#
import json
import random
def password_generator():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+']
    password_list = []
    for char in range(5):
        password_list.append(random.choice(letters))
    for char in range(random.randint(1, 5)):
        password_list.append(random.choice(numbers))
    for char in range(random.randint(1, 4)):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
#--------------------Save Password----------------#
def save_data():
    website_data = website_entry.get()
    email_data = mail_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if website_data and email_data and password_data:
        is_ok = messagebox.askokcancel(
            title=website_data,
            message=f"These are the details entered:\nEmail: {email_data}\nPassword: {password_data}"
        )

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Load existing data
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            mail_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

def find_password():
    web = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Errors", message="You don't have any data yet!")
    else:
        if web in data:
            messagebox.showinfo(f"{web} account Details",f"Email : {data[web]['email']}\nPassword : {data[web]['password']}")
        else:
            messagebox.showwarning(f"{web} account Details","There is no account with that website")
#--------------------UI Manager -----------------#
COLOR = "#a5f8ea"
from tkinter import *
from tkinter import messagebox
def move_to_email(event):
    mail_entry.focus()
def move_to_password(event):
    password_entry.focus()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=COLOR)

canvas = Canvas(width=200, height=200,bg=COLOR,highlightthickness=0)
image = PhotoImage(file="lock_image.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website : ", bg=COLOR)
website_label.grid(row=1,column=0)
mail_label = Label(text="Email/Username : ", bg=COLOR)
mail_label.grid(row=2,column=0)
password_label = Label(text="Password : ", bg=COLOR)
password_label.grid(row=3,column=0)

website_frame = Frame(bg=COLOR)
website_frame.grid(row=1,column=1,columnspan=2)
website_entry = Entry(website_frame, width=17)
website_entry.grid(row=0,column=0)
search = Button(website_frame,width=14,text="SEARCH",command=find_password)
search.grid(row=0,column=1)
website_entry.bind("<Return>", move_to_email)
website_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(row=2,column=1,columnspan=2)

#Button
password_frame = Frame(bg=COLOR)
password_frame.grid(row=3, column=1, columnspan=2)
password_entry = Entry(password_frame, width=17)
password_entry.grid(row=0, column=0)
mail_entry.bind("<Return>", move_to_password)
Generate_Password = Button(password_frame, text="Generate Password", width=14,command=password_generator)
Generate_Password.grid(row=0, column=1)
add_button = Button(text="ADD",width=29,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()