import random
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


def fitness(chromosome):
    n = len(chromosome)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(chromosome[i] - chromosome[j]):
                conflicts += 1
    return -conflicts

def mutate(chromosome):
    a, b = random.sample(range(len(chromosome)), 2)
    chromosome[a], chromosome[b] = chromosome[b], chromosome[a]
    return chromosome

def crossover(p1, p2):
    n = len(p1)
    idx = random.randint(0, n - 1)
    child = p1[:idx] + [gene for gene in p2 if gene not in p1[:idx]]
    return child

def run_genetic(n, generations=500):
    population = [random.sample(range(n), n) for _ in range(100)]
    for _ in range(generations):
        population.sort(key=lambda c: fitness(c), reverse=True)
        if fitness(population[0]) == 0:
            break
        next_gen = population[:20]
        while len(next_gen) < 100:
            p1, p2 = random.sample(population[:50], 2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)
        population = next_gen
    final = population[0]
    board = [[0]*n for _ in range(n)]
    for row, col in enumerate(final):
        board[row][col] = 1
    return board



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