import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3


def categorize_bmi(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    messagebox.showinfo("BMI Category", category)


class BMICalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BMI Calculator")

        # Create input fields
        self.weight_label = tk.Label(self.window, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.pack()

        self.height_label = tk.Label(self.window, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.window)
        self.height_entry.pack()

        # Create calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        # Create result label
        self.result_label = tk.Label(self.window, text="BMI: ")
        self.result_label.pack()

        # Create plot button
        self.plot_button = tk.Button(self.window, text="Plot BMI Trend", command=self.plot_bmi_trend)
        self.plot_button.pack()

        # Create user input field
        self.user_label = tk.Label(self.window, text="User:")
        self.user_label.pack()
        self.user_entry = tk.Entry(self.window)
        self.user_entry.pack()

        # Create save button
        self.save_button = tk.Button(self.window, text="Save Data", command=self.save_data)
        self.save_button.pack()

        # Create load button
        self.load_button = tk.Button(self.window, text="Load Data", command=self.load_data)
        self.load_button.pack()

        # Connect to SQLite database
        self.conn = sqlite3.connect('bmi_data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS bmi_data (user TEXT, weight REAL, height REAL, bmi REAL)')

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / (height ** 2)
            self.result_label['text'] = f"BMI: {bmi:.2f}"
            categorize_bmi(bmi)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def plot_bmi_trend(self):
        self.cursor.execute('SELECT bmi FROM bmi_data WHERE user=?', (self.user_entry.get(),))
        bmi_values = self.cursor.fetchall()
        plt.plot([value[0] for value in bmi_values])
        plt.xlabel("Time")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.show()

    def save_data(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / (height ** 2)
            self.cursor.execute('INSERT INTO bmi_data VALUES (?, ?, ?, ?)',
                                (self.user_entry.get(), weight, height, bmi))
            self.conn.commit()
            messagebox.showinfo("Success", "Data saved successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def load_data(self):
        self.cursor.execute('SELECT * FROM bmi_data WHERE user=?', (self.user_entry.get(),))
        data = self.cursor.fetchall()
        if data:
            messagebox.showinfo("Data Loaded", str(data))
        else:
            messagebox.showinfo("No Data", "No data found for the user")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.run()
