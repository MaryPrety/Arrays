import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def create_network_graph():
    try:
        num_nodes = int(num_nodes_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число для количества узлов.")
        return

    if num_nodes <= 0:
        messagebox.showerror("Ошибка", "Количество узлов должно быть положительным числом.")
        return

    if network_type_var.get() == 1:
        # Создание социальной сети
        G = nx.erdos_renyi_graph(num_nodes, 0.3)
        title = f'Социальная сеть с {num_nodes} узлами'
    elif network_type_var.get() == 2:
        # Создание компьютерной сети
        G = nx.barabasi_albert_graph(num_nodes, 2)
        title = f'Компьютерная сеть с {num_nodes} узлами'
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите тип сети.")
        return

    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
    plt.title(title)
    plt.ion()  # Включение интерактивного режима
    plt.show()

root = tk.Tk()
root.title("Построение сетевого графа")

tk.Label(root, text="Количество узлов:").grid(row=0, column=0)
num_nodes_entry = tk.Entry(root)
num_nodes_entry.grid(row=0, column=1)
num_nodes_entry.insert(0, "5")  # Предзаполненное значение

network_type_var = tk.IntVar()

tk.Label(root, text="Выберите тип сети:").grid(row=1, column=0)
tk.Radiobutton(root, text="Социальная сеть", variable=network_type_var, value=1).grid(row=1, column=1)
tk.Radiobutton(root, text="Компьютерная сеть", variable=network_type_var, value=2).grid(row=2, column=1)

create_button = tk.Button(root, text="Построить граф", command=create_network_graph)
create_button.grid(row=3, columnspan=2)

root.mainloop()
