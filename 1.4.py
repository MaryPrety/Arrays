import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def create_mandelbrot():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        max_iter = int(iter_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для ширины, высоты и максимального количества итераций.")
        return

    x = np.linspace(-2, 1, width)
    y = np.linspace(-1.5, 1.5, height)
    mandelbrot_set = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            mandelbrot_set[j, i] = mandelbrot(x[i] + 1j*y[j], max_iter)

    fig, ax = plt.subplots(figsize=(width/100, height/100))  # Устанавливаем размеры изображения
    ax.imshow(mandelbrot_set, cmap='hot', extent=[-2, 1, -1.5, 1.5])
    ax.set_title('Множество Мандельброта')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, columnspan=2)

    # Добавляем кнопку для сохранения изображения
    save_button = tk.Button(root, text="Сохранить изображение", command=lambda: save_image(fig))
    save_button.grid(row=4, columnspan=2)

def save_image(fig):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        fig.savefig(file_path)
        messagebox.showinfo("Сохранение", "Изображение успешно сохранено.")

root = tk.Tk()
root.title("Создание множества Мандельброта")

tk.Label(root, text="Ширина изображения:").grid(row=0, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=0, column=1)

tk.Label(root, text="Высота изображения:").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="Максимальное количество итераций:").grid(row=2, column=0)
iter_entry = tk.Entry(root)
iter_entry.grid(row=2, column=1)

create_button = tk.Button(root, text="Создать фрактал", command=create_mandelbrot)
create_button.grid(row=4, columnspan=2)

root.mainloop()
