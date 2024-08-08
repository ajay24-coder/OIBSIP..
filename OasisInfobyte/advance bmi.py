import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


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

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / (height ** 2)
            self.result_label['text'] = f"BMI: {bmi:.2f}"
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def plot_bmi_trend(self):
        # Assume we have a list of BMI values for the user
        bmi_values = [20, 22, 24, 26, 28]
        plt.plot(bmi_values)
        plt.xlabel("Time")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.show()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.run()
