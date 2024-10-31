import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_function():
    try:
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        y_min = float(y_min_entry.get())
        y_max = float(y_max_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа для диапазонов x и y.")
        return

    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x, y)

    if function_var.get() == 1:
        Z = np.sin(X) * np.cos(Y)
        title = 'Трехмерный график функции z = sin(x) * cos(y)'
    elif function_var.get() == 2:
        Z = X**2 - Y**2
        title = 'Трехмерный график функции z = x^2 - y^2'
    elif function_var.get() == 3:
        Z = np.exp(-X**2 - Y**2)
        title = 'Трехмерный график функции z = exp(-x^2 - y^2)'
    elif function_var.get() == 4:
        Z = np.sin(X) + np.cos(Y)
        title = 'Трехмерный график функции z = sin(x) + cos(y)'
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите функцию.")
        return

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(title)

    # Включение интерактивного режима
    plt.ion()
    plt.show()

root = tk.Tk()
root.title("Построение трехмерного графика функции")

tk.Label(root, text="Минимум x:").grid(row=0, column=0)
x_min_entry = tk.Entry(root)
x_min_entry.grid(row=0, column=1)

tk.Label(root, text="Максимум x:").grid(row=1, column=0)
x_max_entry = tk.Entry(root)
x_max_entry.grid(row=1, column=1)

tk.Label(root, text="Минимум y:").grid(row=2, column=0)
y_min_entry = tk.Entry(root)
y_min_entry.grid(row=2, column=1)

tk.Label(root, text="Максимум y:").grid(row=3, column=0)
y_max_entry = tk.Entry(root)
y_max_entry.grid(row=3, column=1)

function_var = tk.IntVar()

tk.Label(root, text="Выберите функцию:").grid(row=4, column=0)
tk.Radiobutton(root, text="z = sin(x) * cos(y)", variable=function_var, value=1).grid(row=4, column=1)
tk.Radiobutton(root, text="z = x^2 - y^2", variable=function_var, value=2).grid(row=5, column=1)
tk.Radiobutton(root, text="z = exp(-x^2 - y^2)", variable=function_var, value=3).grid(row=6, column=1)
tk.Radiobutton(root, text="z = sin(x) + cos(y)", variable=function_var, value=4).grid(row=7, column=1)

create_button = tk.Button(root, text="Построить график", command=plot_3d_function)
create_button.grid(row=8, columnspan=2)

root.mainloop()
