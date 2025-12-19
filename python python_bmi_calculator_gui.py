import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

FILE_NAME = "bmi_data.csv"


# ---------------- BMI LOGIC ----------------
def calculate_bmi(weight, height):
    return round(weight / (height * height), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ---------------- SAVE DATA ----------------
def save_data(name, weight, height, bmi, category):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Weight", "Height", "BMI", "Category", "Date"])
        writer.writerow([name, weight, height, bmi, category,
                         datetime.now().strftime("%Y-%m-%d")])


# ---------------- LOAD HISTORY ----------------
def load_history(name):
    records = []
    if not os.path.exists(FILE_NAME):
        return records

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                records.append(row)
    return records


# ---------------- BUTTON ACTIONS ----------------
def calculate():
    try:
        name = entry_name.get().strip()
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if name == "":
            raise ValueError("Name cannot be empty")
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive")

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")
        save_data(name, weight, height, bmi, category)

        messagebox.showinfo("Success", "BMI calculated and saved")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def show_history():
    name = entry_name.get().strip()
    if name == "":
        messagebox.showerror("Error", "Enter name to view history")
        return

    data = load_history(name)
    if not data:
        messagebox.showinfo("No Data", "No records found")
        return

    history = ""
    for row in data:
        history += f"{row['Date']} → BMI: {row['BMI']} ({row['Category']})\n"

    messagebox.showinfo("BMI History", history)


# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Weight (kg)").grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame, text="Height (m)").grid(row=2, column=0, padx=5, pady=5)

entry_name = tk.Entry(frame)
entry_weight = tk.Entry(frame)
entry_height = tk.Entry(frame)

entry_name.grid(row=0, column=1)    
entry_weight.grid(row=1, column=1)
entry_height.grid(row=2, column=1)

tk.Button(root, text="Calculate BMI", command=calculate).pack(pady=5)
tk.Button(root, text="View History", command=show_history).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
