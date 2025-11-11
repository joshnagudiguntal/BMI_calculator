import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter positive numbers only!")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.configure(bg="#e0f7fa")

title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#e0f7fa")
title_label.pack(pady=10)

tk.Label(root, text="Weight (kg):", bg="#e0f7fa").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (m):", bg="#e0f7fa").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#00796b", fg="white")
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#e0f7fa", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()