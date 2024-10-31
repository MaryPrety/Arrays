import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def animate_wave_front():
    try:
        num_points = int(points_entry.get())
        wave_type = wave_type_var.get()
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число для количества точек.")
        return

    if num_points <= 0:
        messagebox.showerror("Ошибка", "Количество точек должно быть положительным числом.")
        return

    if wave_type == 1:
        animate_1d_sinusoidal(num_points)
    elif wave_type == 2:
        animate_2d_circular(num_points)
    elif wave_type == 3:
        animate_3d_spiral(num_points)
    elif wave_type == 4:
        animate_rectangular_wave(num_points)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите тип волны.")
        return

def animate_1d_sinusoidal(num_points):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    ax.set_title('1D волна, амплитуды меняются синусоидально')

    x = np.linspace(0, 10, num_points)
    line, = ax.plot(x, np.sin(x))

    def update(frame):
        line.set_ydata(np.sin(x + frame * 0.05))
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=30, blit=True)
    plt.show()

def animate_2d_circular(num_points):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title('2D волна, круговой фронт')

    x = np.linspace(0, 10, num_points)
    y = np.linspace(0, 10, num_points)
    X, Y = np.meshgrid(x, y)
    im = ax.imshow(np.sin(np.sqrt(X**2 + Y**2)), extent=[0, 10, 0, 10], cmap='viridis')

    def update(frame):
        Z = np.sin(np.sqrt(X**2 + Y**2) + frame * 0.05)
        im.set_array(Z)
        return im,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=30, blit=True)
    plt.show()

def animate_3d_spiral(num_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-2, 2)
    ax.set_title('3D волна, фронт распространяется спирально')

    t = np.linspace(0, 10, num_points)
    line, = ax.plot(t * np.cos(t), t * np.sin(t), np.sin(t))

    def update(frame):
        t = np.linspace(0, 10, num_points) + frame * 0.05
        line.set_data(t * np.cos(t), t * np.sin(t))
        line.set_3d_properties(np.sin(t))
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=30, blit=False)
    plt.show()

def animate_rectangular_wave(num_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(-1, 1)
    ax.set_title('Волна, проходящая через прямоугольную область')

    x = np.linspace(0, 10, num_points)
    y = np.linspace(0, 10, num_points)
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, np.sin(np.sqrt((X - 5)**2 + (Y - 5)**2)), cmap='viridis', alpha=0.8)

    def update(frame):
        Z = np.sin(np.sqrt((X - 5)**2 + (Y - 5)**2) - frame * 0.05)
        ax.clear()
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax.set_zlim(-1, 1)
        ax.set_title('Волна, проходящая через прямоугольную область')

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=30, blit=False)
    plt.show()

root = tk.Tk()
root.title("Визуализация волнового фронта")

tk.Label(root, text="Количество точек:").grid(row=0, column=0)
points_entry = tk.Entry(root)
points_entry.grid(row=0, column=1)
points_entry.insert(0, "50")

wave_type_var = tk.IntVar()

tk.Label(root, text="Выберите тип волны:").grid(row=1, column=0)
tk.Radiobutton(root, text="1D волна, амплитуды меняются синусоидально", variable=wave_type_var, value=1).grid(row=1, column=1)
tk.Radiobutton(root, text="2D волна, круговой фронт", variable=wave_type_var, value=2).grid(row=2, column=1)
tk.Radiobutton(root, text="3D волна, фронт распространяется спирально", variable=wave_type_var, value=3).grid(row=3, column=1)
tk.Radiobutton(root, text="Волна, проходящая через прямоугольную область", variable=wave_type_var, value=4).grid(row=4, column=1)

create_button = tk.Button(root, text="Запустить анимацию", command=animate_wave_front)
create_button.grid(row=5, columnspan=2)

root.mainloop()
