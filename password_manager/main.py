from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def adding_email():
    new_website = website_input.get()
    new_email = email_input.get()
    new_password = password_input.get()
    new_data = {
        new_website: {
            'email': new_email,
            'password': new_password
        }
    }

    if new_website == '' or new_email == '' or new_password == '':
        messagebox.showerror(title='Did not save', message='One of the fields is missing')
        is_ok = False
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH SETUP ------------------------------- #
def search():
    to_search = website_input.get()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            website_results = data[to_search]
            messagebox.showinfo(title='Website Log in Details',
                                message=f'Email / Username: {website_results["email"]}\nPassword: {website_results["password"]}')
    except KeyError:
        messagebox.showerror(title='Error', message=f'No such website.')
    except FileNotFoundError:
        reply = messagebox.askokcancel(title='File error', message='No Data stored yet. Create new file?')
        if not reply:
            exit()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text='Website:')
website_label.grid(column=0, row=2)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=3)

password_label = Label(text='Password:')
password_label.grid(column=0, row=4)

status_label = Label()
status_label.grid(column=1, row=1)

# button

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=4)
#
add_button = Button(text='Add', command=adding_email, width=30)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text='Search', command=search, width=10)
search_button.grid(column=2, row=2)

# input

website_input = Entry(width=22)
website_input.focus()
website_input.grid(column=1, row=2)

email_input = Entry(width=40)
email_input.grid(column=1, row=3, columnspan=2)
email_input.insert(END, 'darrentu@engbeefood.com')

password_input = Entry(width=22)
password_input.grid(column=1, row=4)

window.mainloop()
