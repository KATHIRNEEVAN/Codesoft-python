import tkinter as tk
import random
import string



def generate_password(length):
    if length.isdigit():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(int(length)))
        return password
    else:
        return 'Invalid Input'

def validate_length(text):
    if text == '':
        return True
    elif text.isdigit():
        return int(text) > 0
    else:
        return False


def invalid_length():
    label.config(text='Invalid Input', fg='red')

window = tk.Tk()
window.title('Password Generator')
window.geometry('400x400')
window.configure(bg='orange', padx=20, pady=20)

entry_label = tk.Label(window, text='Enter password length:', font=('serif', 20), bg='light blue', fg='black')
entry_label.pack(side=tk.TOP, pady=10)

pass_entry = tk.Entry(window, width=20, font=('Fantasy', 20), bg='light blue', fg='black', textvariable="")
pass_entry.pack(side=tk.TOP, pady=10)

pass_entry.config(validate='focusout', validatecommand=(window.register(validate_length), '%P'), invalidcommand=invalid_length)

label = tk.Label(window, text='Password', font=('serif', 20), bg='light blue', fg='black')
label.pack(side=tk.TOP, pady=10)

button = tk.Button(window, text='Generate Password', font=('serif', 20), bg='light blue', fg='black', command=lambda: label.config(text=generate_password(pass_entry.get()), fg='dark green'))
button.pack(side=tk.TOP, pady=10)

window.mainloop()
