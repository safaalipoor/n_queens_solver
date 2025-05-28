import tkinter as tk
from tkinter import messagebox

def start_solver():
    try:
        n = int(entry.get())
        if n < 4:
            raise ValueError
        messagebox.showinfo("ورودی صحیح", f"{n} وزیر وارد شد.")
    except ValueError:
        messagebox.showerror("خطا", "لطفاً عددی صحیح و بزرگ‌تر از ۳ وارد کنید.")

root = tk.Tk()
root.title("حل مسئله N وزیر")

label = tk.Label(root, text="تعداد n را وارد کنید:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="حل مسئله", command=start_solver)
button.pack(pady=10)

root.mainloop()