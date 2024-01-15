'''
made a converter to convert inches to cm. have problems converting 1/8 or 2/8 etc into cm.

made this converter so that conversion to cm will be easier with metric.
'''

from tkinter import *

# creating a new window and configs

window = Tk()
window.title('Inch to cm converter')
window.minsize(width=300, height=200)
window.config(padx=60, pady=60)


# functions

def calculate():

    inch = inch_input.get()
    # check for no value, and inputs 0
    if inch == '':
        inch = 0
    else:
        inch = int(inch)

    # check for no value, and inputs 0
    fen = fen_input.get()
    if fen == '':
        fen = 0
    else:
        fen = int(fen)

    inch *= 2.54
    fen *= 2.54 / 8
    total = inch + fen
    total = round(total, 2)
    converted_cm.config(text=total)

    return total

def clear_inputs(event):
    inch_input.delete(0, END)
    fen_input.delete(0, END)
    inch_input.insert(END, '0')
    fen_input.insert(END, '0')


# keyboard button press

window.bind('<Return>', calculate)
window.bind('<Escape>', clear_inputs)


# labels

inch_label = Label(text='寸')
inch_label.grid(column=1, row=0)

fen_label = Label(text='分')
fen_label.grid(column=3, row=0)

cm_label = Label(text='cm')
cm_label.grid(column=2, row=1)

is_equal_to_label = Label(text='is equal to:')
is_equal_to_label.grid(column=0, row=1)

converted_cm = Label(text='0')
converted_cm.grid(column=1, row=1)

# inputs

inch_input = Entry(width=10, justify=CENTER)
inch_input.grid(column=0, row=0)
inch_input.insert(END, '0')
inch_input.focus()

fen_input = Entry(width=10, justify=CENTER)
fen_input.grid(column=2, row=0)
fen_input.insert(END, '0')

# buttons

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
