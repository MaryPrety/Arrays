import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_particles():
    try:
        num_particles = int(particles_entry.get())
        max_speed = float(speed_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа для количества частиц и максимальной скорости.")
        return

    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title('Анимация расхождения частиц')

    particles = np.zeros((num_particles, 2))

    if speed_mode.get() == "Случайная скорость":
        speeds = np.random.uniform(0, max_speed, num_particles)
    elif speed_mode.get() == "Уменьшающаяся скорость":
        speeds = np.linspace(max_speed, 0, num_particles)
    elif speed_mode.get() == "Увеличивающаяся скорость":
        speeds = np.linspace(0, max_speed, num_particles)

    if direction_mode.get() == "Случайное направление":
        angles = np.random.uniform(0, 2 * np.pi, num_particles)
    elif direction_mode.get() == "По часовой стрелке":
        angles = np.linspace(0, 2 * np.pi, num_particles)
    elif direction_mode.get() == "Против часовой стрелки":
        angles = np.linspace(2 * np.pi, 0, num_particles)

    scat = ax.scatter(particles[:, 0], particles[:, 1], s=10)

    def update(frame):
        particles[:, 0] += speeds * np.cos(angles)
        particles[:, 1] += speeds * np.sin(angles)
        scat.set_offsets(particles)
        return scat,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)
    plt.show()

root = tk.Tk()
root.title("Анимация расхождения частиц")

tk.Label(root, text="Количество частиц:").grid(row=0, column=0)
particles_entry = tk.Entry(root)
particles_entry.grid(row=0, column=1)

tk.Label(root, text="Максимальная скорость:").grid(row=1, column=0)
speed_entry = tk.Entry(root)
speed_entry.grid(row=1, column=1)

tk.Label(root, text="Режим скорости:").grid(row=2, column=0)
speed_mode = tk.StringVar(value="Случайная скорость")
speed_menu = tk.OptionMenu(root, speed_mode, "Случайная скорость", "Уменьшающаяся скорость", "Увеличивающаяся скорость")
speed_menu.grid(row=2, column=1)

tk.Label(root, text="Режим направления:").grid(row=3, column=0)
direction_mode = tk.StringVar(value="Случайное направление")
direction_menu = tk.OptionMenu(root, direction_mode, "Случайное направление", "По часовой стрелке", "Против часовой стрелки")
direction_menu.grid(row=3, column=1)

create_button = tk.Button(root, text="Запустить анимацию", command=animate_particles)
create_button.grid(row=4, columnspan=2)

root.mainloop()
