import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def create_mosaic():
    try:
        size = int(size_entry.get())
        colors = int(colors_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для размера и количества цветов.")
        return

    mosaic = np.random.randint(0, colors, (size, size))
    plt.imshow(mosaic, cmap='viridis', interpolation='none')
    plt.title(f'Мозаика {size}x{size} с {colors} цветами')
    plt.colorbar()
    plt.show()

root = tk.Tk()
root.title("Создание мозаичного изображения")

tk.Label(root, text="Размер мозаики (NxN):").grid(row=0, column=0)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1)

tk.Label(root, text="Количество цветов:").grid(row=1, column=0)
colors_entry = tk.Entry(root)
colors_entry.grid(row=1, column=1)

create_button = tk.Button(root, text="Создать мозаику", command=create_mosaic)
create_button.grid(row=2, columnspan=2)

root.mainloop()
