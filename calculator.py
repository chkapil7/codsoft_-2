import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.num1_label = tk.Label(root, text="Number 1:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(root, text="Number 2:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack()

        self.operation_label = tk.Label(root, text="Operation:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar(value="Addition")
        self.operations = ["Addition", "Subtraction", "Multiplication", "Division"]

        for operation in self.operations:
            tk.Radiobutton(root, text=operation, variable=self.operation_var, value=operation).pack(anchor=tk.W)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.result_var = tk.StringVar()
        self.result_display = tk.Label(root, textvariable=self.result_var)
        self.result_display.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                result = num1 / num2

            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
