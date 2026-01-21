import tkinter as tk

class Calc():
    def __init__(self, x):
        self.x = x
    def __add__(self, add):
        return self.x + add.x
    def __mul__(self, add):
        return self.x * add.x
    def __truediv__(self, add):
        return self.x / add.x
    def __sub__(self, add):
        return self.x - add.x
    def __pow__(self, add):
        return self.x**add.x

def calculator():
    a = int(entry1.get())
    b = str(entry2.get())
    c = int(entry3.get())
    x = Calc(a)
    y = Calc(c)

    if b == "+":
        result = x + y
    elif b == "-":
        result = x - y
    elif b == "*":
        result = x * y
    elif b == "/":
        result = x / y

    else:
        result = "Invalid operator"


    result_label.config(text=f"Result: {result}")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
root = tk.Tk()
root.geometry("400x400")
root.configure(bg="white")

tk.Label(root, text="CALCULATOR", font=("Bold", 17), bg="white", fg="red").pack(pady=5)

tk.Label(root, text="Number 1:", bg="white", fg="green", font=("Arial", 14)).pack()
entry1 = tk.Entry(root, bg="white", fg="black", width=30, font=("Arial", 10))
entry1.pack(ipady=4, ipadx=3)

tk.Label(root, text="Operator (+ - * /):", bg="white", fg="green", font=("Arial", 14)).pack()
entry2 = tk.Entry(root, bg="white", fg="black", width=10, font=("Arial", 10))
entry2.pack()

tk.Label(root, text="Number 2:", bg="white", fg="green", font=("Arial", 14)).pack()
entry3 = tk.Entry(root, bg="white", fg="black", width=30, font=("Arial", 10))
entry3.pack(pady=5, ipady=4, ipadx=3)

tk.Button(root, text="Compute", bg="grey", fg="black", command=calculator, font=("Arial", 10)).pack(pady=6)

result_label = tk.Label(root, text="Result: ", bg="white", fg="blue", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

