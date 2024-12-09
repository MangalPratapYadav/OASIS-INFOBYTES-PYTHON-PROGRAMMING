import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    character_set = ''
    if uppercase_var.get():
        character_set += string.ascii_uppercase
    if lowercase_var.get():
        character_set += string.ascii_lowercase
    if digits_var.get():
        character_set += string.digits
    if symbols_var.get():
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert('end', password)

def reset_fields():
    length_var.set("")
    uppercase_var.set(False)
    lowercase_var.set(False)
    digits_var.set(False)
    symbols_var.set(False)
    password_entry.delete(0, 'end')

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

length_label = tk.Label(root, text="Password Length:", bg="#f0f0f0", font=("Helvetica", 12))
length_label.pack(pady=5)

length_var = tk.IntVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Helvetica", 12))
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, bg="#f0f0f0", font=("Helvetica", 10))
uppercase_checkbox.pack(pady=2)

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var, bg="#f0f0f0", font=("Helvetica", 10))
lowercase_checkbox.pack(pady=2)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#f0f0f0", font=("Helvetica", 10))
digits_checkbox.pack(pady=2)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0", font=("Helvetica", 10))
symbols_checkbox.pack(pady=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
password_entry.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="#FF5722", fg="white", font=("Helvetica", 12, "bold"))
reset_button.pack(pady=5)

root.mainloop()
