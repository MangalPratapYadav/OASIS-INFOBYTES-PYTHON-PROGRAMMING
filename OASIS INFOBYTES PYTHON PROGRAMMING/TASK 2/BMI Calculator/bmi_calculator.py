import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os

def calculate_bmi(weight, height_cm):
    try:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return None

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_to_file(weight, height_cm, bmi, category):
    try:
        csv_file_path = os.path.join(os.path.dirname(__file__), "bmi_results.csv")
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Weight", "Height", "BMI", "Category"])
        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([weight, height_cm, f"{bmi:.2f}", category])
        load_csv_data()
    except IOError as e:
        messagebox.showerror("File Error", f"Error saving to file: {e}")

def load_csv_data():
    try:
        csv_file_path = os.path.join(os.path.dirname(__file__), "bmi_results.csv")
        for row in treeview.get_children():
            treeview.delete(row)
        if os.path.exists(csv_file_path):
            with open(csv_file_path, mode="r") as file:
                csv_reader = csv.reader(file)
                next(csv_reader, None)
                rows = list(csv_reader)
                for row in rows:
                    treeview.insert("", "end", values=row)
                treeview.config(height=min(len(rows), 10))
    except IOError as e:
        messagebox.showerror("File Error", f"Error loading file: {e}")

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive values for weight and height.")
            return
        bmi = calculate_bmi(weight, height_cm)
        if bmi is not None:
            category = classify_bmi(bmi)
            result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
            save_to_file(weight, height_cm, bmi, category)
            messagebox.showinfo("Result", "Your result has been saved!")
        else:
            messagebox.showerror("Error", "Height cannot be zero.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

def on_reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="Your BMI will appear here.")

def on_exit():
    window.destroy()

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("700x500")

font_large = ('Arial', 14)
font_button = ('Arial', 12, 'bold')

tk.Label(window, text="Enter your weight (kg):", font=font_large).grid(row=0, column=0, padx=20, pady=20)
weight_entry = tk.Entry(window, font=font_large)
weight_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(window, text="Enter your height (cm):", font=font_large).grid(row=1, column=0, padx=20, pady=20)
height_entry = tk.Entry(window, font=font_large)
height_entry.grid(row=1, column=1, padx=20, pady=20)

calculate_button = tk.Button(window, text="Calculate BMI", command=on_calculate, font=font_button, bg="#4CAF50", fg="white", padx=20, pady=10)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

reset_button = tk.Button(window, text="Reset", command=on_reset, font=font_button, bg="#f44336", fg="white", padx=20, pady=10)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

exit_button = tk.Button(window, text="Exit", command=on_exit, font=font_button, bg="#555555", fg="white", padx=20, pady=10)
exit_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Your BMI will appear here.", font=font_large)
result_label.grid(row=4, column=0, columnspan=2, pady=30)

treeview = ttk.Treeview(window, columns=("Weight", "Height", "BMI", "Category"), show="headings", height=5)
treeview.grid(row=5, column=0, columnspan=2, pady=20)

treeview.heading("Weight", text="Weight (kg)")
treeview.heading("Height", text="Height (cm)")
treeview.heading("BMI", text="BMI")
treeview.heading("Category", text="Category")

treeview.column("Weight", width=120, anchor="center")
treeview.column("Height", width=120, anchor="center")
treeview.column("BMI", width=120, anchor="center")
treeview.column("Category", width=180, anchor="center")

scrollbar_y = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
scrollbar_y.grid(row=5, column=2, sticky="ns")

treeview.configure(yscrollcommand=scrollbar_y.set)

load_csv_data()

window.mainloop()
