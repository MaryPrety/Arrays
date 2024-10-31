import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def create_heatmap():
    try:
        size = int(size_entry.get())
        temp_min = float(temp_min_entry.get())
        temp_max = float(temp_max_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для размера и числа для температурных диапазонов.")
        return

    if size <= 0:
        messagebox.showerror("Ошибка", "Размер карты должен быть положительным числом.")
        return

    if temp_min >= temp_max:
        messagebox.showerror("Ошибка", "Минимальная температура должна быть меньше максимальной температуры.")
        return

    data = np.random.uniform(temp_min, temp_max, (size, size))
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title(f'Тепловая карта {size}x{size}')
    plt.ion()  # Включение интерактивного режима
    plt.show()

root = tk.Tk()
root.title("Создание тепловой карты")

tk.Label(root, text="Размер карты (NxN):").grid(row=0, column=0)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1)
size_entry.insert(0, "10")  # Предзаполненное значение

tk.Label(root, text="Минимальная температура:").grid(row=1, column=0)
temp_min_entry = tk.Entry(root)
temp_min_entry.grid(row=1, column=1)
temp_min_entry.insert(0, "-10")  # Предзаполненное значение

tk.Label(root, text="Максимальная температура:").grid(row=2, column=0)
temp_max_entry = tk.Entry(root)
temp_max_entry.grid(row=2, column=1)
temp_max_entry.insert(0, "40")  # Предзаполненное значение

create_button = tk.Button(root, text="Создать тепловую карту", command=create_heatmap)
create_button.grid(row=3, columnspan=2)

root.mainloop()
