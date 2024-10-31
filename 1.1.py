import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def update_description(*args):
    if spiral_var.get() == "Спираль с увеличивающимся шагом":
        description_label.config(text="""
        Параметр a: Начальный радиус спирали
        Параметр b: Увеличение радиуса на каждом шаге
        """)
    elif spiral_var.get() == "Логарифмическая спираль":
        description_label.config(text="""
        Параметр a: Начальный радиус спирали
        Параметр b: Коэффициент, определяющий скорость роста
        """)
    elif spiral_var.get() == "Спираль Архимеда":
        description_label.config(text="""
        Параметр a: Начальный радиус спирали
        Параметр b: Увеличение радиуса на каждом шаге
        """)
    elif spiral_var.get() == "Спираль Ферма":
        description_label.config(text="""
        Параметр a: Не используется (оставьте 1)
        Параметр b: Не используется (оставьте 1)
        """)

def plot_spiral():
    try:
        num_points = int(points_entry.get())
        a = float(a_entry.get())
        b = float(b_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа для количества точек и параметров.")
        return

    theta = np.linspace(0, 10 * np.pi, num_points)

    if spiral_var.get() == "Спираль с увеличивающимся шагом":
        r = a + b * theta
    elif spiral_var.get() == "Логарифмическая спираль":
        r = a * np.exp(b * theta)
    elif spiral_var.get() == "Спираль Архимеда":
        r = a + b * theta
    elif spiral_var.get() == "Спираль Ферма":
        r = np.sqrt(theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color='blue')
    plt.title(spiral_var.get())
    plt.axis('equal')
    plt.show()

root = tk.Tk()
root.title("Выбор и кастомизация спирали")

tk.Label(root, text="Тип спирали:").grid(row=0, column=0)
spiral_var = tk.StringVar(value="Спираль с увеличивающимся шагом")
spiral_menu = tk.OptionMenu(root, spiral_var, "Спираль с увеличивающимся шагом", "Логарифмическая спираль", "Спираль Архимеда", "Спираль Ферма", command=update_description)
spiral_menu.grid(row=0, column=1)

tk.Label(root, text="Количество точек:").grid(row=1, column=0)
points_entry = tk.Entry(root)
points_entry.grid(row=1, column=1)

tk.Label(root, text="Параметр a:").grid(row=2, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=2, column=1)

tk.Label(root, text="Параметр b:").grid(row=3, column=0)
b_entry = tk.Entry(root)
b_entry.grid(row=3, column=1)

description_label = tk.Label(root, text="""
Параметр a: Начальный радиус спирали
Параметр b: Увеличение радиуса на каждом шаге
""")
description_label.grid(row=4, column=0, columnspan=2)

plot_button = tk.Button(root, text="Построить спираль", command=plot_spiral)
plot_button.grid(row=5, columnspan=2)

# Инициализация описания
update_description()

root.mainloop()
