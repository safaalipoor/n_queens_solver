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

def is_safe_bt(board, row, col, n):
    for i in range(row):
        if board[i][col] or \
           (col - (row - i) >= 0 and board[i][col - (row - i)]) or \
           (col + (row - i) < n and board[i][col + (row - i)]):
            return False
    return True

def solve_bt(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe_bt(board, row, col, n):
            board[row][col] = 1
            if solve_bt(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def run_backtracking(n):
    board = [[0]*n for _ in range(n)]
    if solve_bt(board, 0, n):
        return board
    return None