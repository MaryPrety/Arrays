import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, filedialog, colorchooser

class PieChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Круговая диаграмма")
        self.root.geometry("800x600")
        
        self.categories = ["Категория 1", "Категория 2", "Категория 3"]
        self.data = [20, 30, 50]
        self.colors = ["#ff9999", "#66b3ff", "#99ff99"]
        self.title = "Продажи по категориям"
        
        self.create_widgets()
        self.update_pie_chart()

    def create_widgets(self):
        # Создаем Canvas для скроллинга
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Создаем фрейм внутри Canvas и прокручиваем его
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Добавляем Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Фрейм для диаграммы
        self.chart_frame = tk.Frame(self.root, padx=10, pady=10)
        self.chart_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Таблица ввода данных и кнопки
        self.create_data_table()
        self.create_control_buttons()

    def create_data_table(self):
        # Заголовки
        headers = ["Категория", "Значение", "Цвет"]
        for i, header in enumerate(headers):
            tk.Label(self.scrollable_frame, text=header).grid(row=0, column=i)
        
        self.category_entries, self.data_entries, self.color_buttons = [], [], []

        for i, (category, value, color) in enumerate(zip(self.categories, self.data, self.colors)):
            self.add_row(i, category, value, color)

    def add_row(self, row, category="", value="", color="#ffffff"):
        # Поля ввода для категории
        category_entry = tk.Entry(self.scrollable_frame, width=15)
        category_entry.insert(0, category)
        category_entry.grid(row=row+1, column=0)
        self.category_entries.append(category_entry)

        # Поля ввода для значений
        data_entry = tk.Entry(self.scrollable_frame, width=10)
        data_entry.insert(0, value)
        data_entry.grid(row=row+1, column=1)
        self.data_entries.append(data_entry)

        # Кнопка выбора цвета
        color_button = tk.Button(self.scrollable_frame, bg=color, width=5, command=lambda row=row: self.choose_color(row))
        color_button.grid(row=row+1, column=2)
        self.color_buttons.append(color_button)

    def create_control_buttons(self):
        # Панель управления
        control_frame = tk.Frame(self.root, pady=10)
        control_frame.pack(fill=tk.X)

        tk.Button(control_frame, text="Добавить категорию", command=self.add_category).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Удалить категорию", command=self.remove_category).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Обновить диаграмму", command=self.update_pie_chart).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Сохранить диаграмму", command=self.save_chart).pack(side=tk.LEFT, padx=5)

    def add_category(self):
        row = len(self.category_entries)
        self.add_row(row)
        self.update_pie_chart()

    def remove_category(self):
        if self.category_entries:
            self.category_entries[-1].grid_forget()
            self.data_entries[-1].grid_forget()
            self.color_buttons[-1].grid_forget()

            self.category_entries.pop()
            self.data_entries.pop()
            self.color_buttons.pop()

            self.update_pie_chart()

    def choose_color(self, row):
        color_code = colorchooser.askcolor(title="Выберите цвет")[1]
        if color_code:
            self.color_buttons[row].config(bg=color_code)

    def update_pie_chart(self):
        self.categories = [entry.get() for entry in self.category_entries]
        self.data = [int(entry.get()) for entry in self.data_entries]
        self.colors = [button.cget("bg") for button in self.color_buttons]

        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        fig = self.create_pie_chart(self.categories, self.data, self.colors, self.title)
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_pie_chart(self, categories, data, colors, title):
        fig, ax = plt.subplots()
        ax.pie(data, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
        ax.set_title(title)
        return fig

    def save_chart(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            self.create_pie_chart(self.categories, self.data, self.colors, self.title).savefig(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = PieChartApp(root)
    root.mainloop()
