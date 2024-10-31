import tkinter as tk
from tkinter import messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt

def create_network_graph():
    try:
        edges_input = edges_entry.get().strip()
        if not edges_input:
            messagebox.showerror("Ошибка", "Пожалуйста, введите соединения между узлами.")
            return
        
        edges = [tuple(map(int, edge.split(','))) for edge in edges_input.split(';')]
        
        if not all(isinstance(edge, tuple) and len(edge) == 2 for edge in edges):
            messagebox.showerror("Ошибка", "Формат соединений должен быть: узел1,узел2; узел3,узел4; ...")
            return
        
        G = nx.Graph()  # Создание графа
        G.add_edges_from(edges)  # Добавление соединений в граф
        
        title = f'Граф с {G.number_of_nodes()} узлами и {G.number_of_edges()} соединениями'

        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
        plt.title(title)
        plt.show()

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("Построение сетевого графа")

tk.Label(root, text="Введите соединения (формат: узел1,узел2; узел3,узел4):").grid(row=0, column=0, columnspan=2)
edges_entry = tk.Entry(root, width=50)
edges_entry.grid(row=1, column=0, columnspan=2)
edges_entry.insert(0, "1,2; 1,3; 2,3; 3,4")  # Предзаполненное значение

create_button = tk.Button(root, text="Построить граф", command=create_network_graph)
create_button.grid(row=2, columnspan=2)

root.mainloop()
