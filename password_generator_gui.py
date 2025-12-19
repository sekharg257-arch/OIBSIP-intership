# Random Password Generator - Advanced GUI Version
# Oasis Infobyte Internship Project
# Author: Nakka Gurusekhar

import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_password():
    password = result_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy")

# GUI Window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x350")
window.resizable(False, False)

# Heading
tk.Label(window, text="Random Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length Input
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window, width=20)
length_entry.pack(pady=5)

# Checkboxes
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(window, text="Include Letters (A-Z, a-z)", variable=letters_var).pack(anchor="w", padx=50)
tk.Checkbutton(window, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor="w", padx=50)
tk.Checkbutton(window, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor="w", padx=50)

# Generate Button
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=15)

# Result
tk.Label(window, text="Generated Password:").pack()
result_entry = tk.Entry(window, width=30, font=("Arial", 10))
result_entry.pack(pady=5)

# Copy Button
tk.Button(window, text="Copy to Clipboard", command=copy_password).pack(pady=10)

# Run App
window.mainloop()
