import tkinter as tk
from tkinter import ttk, colorchooser
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PlanetSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Моделирование планетарной системы")
        
        self.planet_entries = []  # Список для хранения параметров планет
        self.selected_planet_index = None  # Индекс выбранной планеты для слежения
        self.zoom_level = 2  # Начальный масштаб отображения
        self.trajectories = []  # Список для хранения траекторий планет
        self.create_widgets()

    def create_widgets(self):
        self.planet_frame = tk.Frame(self.root)
        self.planet_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(self.planet_frame, text="Параметры планет:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=8)

        self.add_planet_button = tk.Button(self.planet_frame, text="Добавить планету", command=self.add_planet_row)
        self.add_planet_button.grid(row=1, column=0, columnspan=8, pady=5)

        tk.Label(self.planet_frame, text="Режим просмотра:").grid(row=1, column=8)
        self.view_mode = ttk.Combobox(self.planet_frame, state="readonly", values=["Все планеты", "Слежка за планетой"])
        self.view_mode.grid(row=1, column=9, padx=5)
        self.view_mode.set("Все планеты")

        tk.Label(self.planet_frame, text="Выберите планету для слежения:").grid(row=2, column=8)
        self.planet_selector = ttk.Combobox(self.planet_frame, state="readonly", values=[""])
        self.planet_selector.grid(row=2, column=9, padx=5)

        tk.Label(self.planet_frame, text="Масштаб:").grid(row=3, column=8)
        self.zoom_slider = tk.Scale(self.planet_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.update_zoom)
        self.zoom_slider.set(self.zoom_level)
        self.zoom_slider.grid(row=3, column=9, padx=5)

        self.start_button = tk.Button(self.root, text="Запустить симуляцию", command=self.simulate_planetary_system)
        self.start_button.pack(pady=10)

    def add_planet_row(self):
        row = len(self.planet_entries) + 4

        eccentricity_label = tk.Label(self.planet_frame, text="Эксцентриситет:")
        eccentricity_label.grid(row=row, column=0, padx=5)
        eccentricity_entry = tk.Entry(self.planet_frame)
        eccentricity_entry.grid(row=row, column=1, padx=5)

        mass_label = tk.Label(self.planet_frame, text="Масса:")
        mass_label.grid(row=row, column=2, padx=5)
        mass_entry = tk.Entry(self.planet_frame)
        mass_entry.grid(row=row, column=3, padx=5)

        orbit_type_label = tk.Label(self.planet_frame, text="Тип орбиты:")
        orbit_type_label.grid(row=row, column=4, padx=5)
        orbit_type = ttk.Combobox(self.planet_frame, values=["круговая", "эллиптическая"], state="readonly")
        orbit_type.set("круговая")
        orbit_type.grid(row=row, column=5, padx=5)

        color_button = tk.Button(self.planet_frame, text="Выбрать цвет", command=lambda: self.choose_color(row - 4))
        color_button.grid(row=row, column=6, padx=5)
        color_label = tk.Label(self.planet_frame, text=" ", bg="gray", width=2)
        color_label.grid(row=row, column=7, padx=5)

        shape_label = tk.Label(self.planet_frame, text="Форма:")
        shape_label.grid(row=row, column=8, padx=5)
        shape_combo = ttk.Combobox(self.planet_frame, values=["круг", "квадрат", "треугольник"], state="readonly")
        shape_combo.set("круг")
        shape_combo.grid(row=row, column=9, padx=5)

        delete_button = tk.Button(self.planet_frame, text="Удалить", command=lambda: self.delete_planet_row(row - 4))
        delete_button.grid(row=row, column=10, padx=5)

        self.planet_entries.append((eccentricity_entry, mass_entry, orbit_type, color_label, shape_combo, delete_button))
        self.trajectories.append([])  # Инициализируем список для траектории новой планеты

        self.update_planet_selector()

    def choose_color(self, index):
        color = colorchooser.askcolor()[1]
        if color:
            self.planet_entries[index][3].config(bg=color)

    def delete_planet_row(self, index):
        for widget in self.planet_entries[index]:
            widget.destroy()
        del self.planet_entries[index]
        del self.trajectories[index]  # Удаляем траекторию соответствующей планеты

        for i, row in enumerate(self.planet_entries, start=4):
            for col, widget in enumerate(row[:-1]):
                widget.grid(row=i, column=col + 1)

        self.update_planet_selector()

    def update_planet_selector(self):
        planet_names = [f"Планета {i+1}" for i in range(len(self.planet_entries))]
        self.planet_selector['values'] = planet_names

    def update_zoom(self, value):
        self.zoom_level = int(value)

    def simulate_planetary_system(self):
        num_planets = len(self.planet_entries)
        fig, ax = plt.subplots()
        ax.set_xlim(-self.zoom_level, self.zoom_level)
        ax.set_ylim(-self.zoom_level, self.zoom_level)
        ax.set_title('Моделирование планетарной системы')

        # Звезда в центре
        ax.plot(0, 0, 'o', color='yellow', markersize=15)  # Звезда

        angles = np.linspace(0, 2 * np.pi, num_planets)
        radii = np.linspace(1.5, 3, num_planets)  # Начальные радиусы с учетом расстояния
        planets = np.zeros((num_planets, 2))

        view_mode = self.view_mode.get()
        selected_planet = self.planet_selector.current() if self.planet_selector.current() >= 0 else None

        # Увеличиваем количество кадров для полного цикла
        total_frames = 360  # 360 кадров для полного оборота

        def update(frame):
            ax.cla()
            ax.set_xlim(-self.zoom_level, self.zoom_level)
            ax.set_ylim(-self.zoom_level, self.zoom_level)
            ax.set_title('Моделирование планетарной системы')
            ax.plot(0, 0, 'o', color='yellow', markersize=15)  # Звезда

            for i, (eccentricity_entry, mass_entry, orbit_type, color_label, shape_combo, _) in enumerate(self.planet_entries):
                ecc = float(eccentricity_entry.get() or 0)
                radius = radii[i]

                if orbit_type.get() == "эллиптическая":
                    radius *= (1 + ecc * np.cos(angles[i] + frame * (2 * np.pi / total_frames)))  # Используем полный оборот

                planets[i, 0] = radius * np.cos(angles[i] + frame * (2 * np.pi / total_frames))
                planets[i, 1] = radius * np.sin(angles[i] + frame * (2 * np.pi / total_frames))

                # Сохранение текущей позиции планеты для отображения траектории
                self.trajectories[i].append(planets[i].copy())
                
                # Рисуем траекторию
                trajectory = np.array(self.trajectories[i])
                ax.plot(trajectory[:, 0], trajectory[:, 1], color=color_label.cget("bg"), alpha=0.3)  # Линия траектории
                
                color = color_label.cget("bg")
                marker = "o" if shape_combo.get() == "круг" else ("s" if shape_combo.get() == "квадрат" else "^")
                ax.plot(planets[i, 0], planets[i, 1], marker, color=color, markersize=10)

            if view_mode == "Слежка за планетой" and selected_planet is not None:
                ax.set_xlim(planets[selected_planet, 0] - self.zoom_level, planets[selected_planet, 0] + self.zoom_level)
                ax.set_ylim(planets[selected_planet, 1] - self.zoom_level, planets[selected_planet, 1] + self.zoom_level)

        ani = FuncAnimation(fig, update, frames=np.arange(0, total_frames), interval=50)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanetSimulationApp(root)
    root.mainloop()
