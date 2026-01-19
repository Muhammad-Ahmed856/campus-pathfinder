import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt

# ------------------- EXPANDED CAMPUS GRAPH DATA -------------------
campus_graph = {
    "Library": {"Main Gate": 4, "IT Department": 2, "Auditorium": 3},
    "Main Gate": {"Library": 4, "Cafeteria": 4, "Parking": 3, "Admin Block": 5},
    "IT Department": {"Library": 2, "Cafeteria": 4, "Hostel": 8, "Computer Lab": 3},
    "Cafeteria": {"Main Gate": 4, "IT Department": 4, "Hostel": 6, "Sports Ground": 5},
    "Parking": {"Main Gate": 3, "Science Block": 7},
    "Hostel": {"Cafeteria": 6, "IT Department": 8, "Gym": 4},
    "Auditorium": {"Library": 3, "Admin Block": 4},
    "Admin Block": {"Main Gate": 5, "Auditorium": 4, "Finance Office": 3},
    "Finance Office": {"Admin Block": 3, "Sports Ground": 8},
    "Sports Ground": {"Cafeteria": 5, "Finance Office": 8, "Gym": 6},
    "Gym": {"Hostel": 4, "Sports Ground": 6},
    "Science Block": {"Parking": 7, "Computer Lab": 5},
    "Computer Lab": {"IT Department": 3, "Science Block": 5, "Exam Center": 4},
    "Exam Center": {"Computer Lab": 4, "Medical Center": 6},
    "Medical Center": {"Exam Center": 6, "Security Office": 3},
    "Security Office": {"Medical Center": 3, "Main Gate": 7},
    "Sports Complex": {"Sports Ground": 6, "Hostel": 10},
}

# Convert to networkx graph
G = nx.Graph()
for u in campus_graph:
    for v, w in campus_graph[u].items():
        G.add_edge(u, v, weight=w)


# ---------------------- DIJKSTRA SHORTEST PATH ----------------------
def dijkstra(start, end):
    try:
        path = nx.shortest_path(G, start, end, weight="weight")
        distance = nx.shortest_path_length(G, start, end, weight="weight")
        return path, distance
    except:
        return None, None


# ---------------------- K SHORTEST PATHS ----------------------
def k_shortest(start, end, k=3):
    try:
        paths = list(nx.shortest_simple_paths(G, start, end, weight="weight"))
        return paths[:k]
    except:
        return []


# ---------------------- NEAREST 3 LOCATIONS ----------------------
def nearest(start):
    dist = {}
    for node in G.nodes():
        if node != start:
            try:
                d = nx.shortest_path_length(G, start, node, weight="weight")
                dist[node] = d
            except:
                pass
    return sorted(dist.items(), key=lambda x: x[1])[:3]


# ---------------------- DRAW CAMPUS GRAPH ----------------------
def draw_graph():
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=2200,
            font_size=9, node_color="skyblue")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Campus Map (Graph Visualization)")
    plt.show()


# ---------------------- GUI ----------------------
root = tk.Tk()
root.title("Campus Navigation System")
root.geometry("550x550")

ttk.Label(root, text="Campus Navigation System",
          font=("Arial", 18)).pack(pady=10)

frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Start:").grid(row=0, column=0)
ttk.Label(frame, text="Destination:").grid(row=1, column=0)

start_var = tk.StringVar()
end_var = tk.StringVar()

nodes = list(G.nodes())

combo_start = ttk.Combobox(frame, textvariable=start_var, values=nodes)
combo_end = ttk.Combobox(frame, textvariable=end_var, values=nodes)

combo_start.grid(row=0, column=1)
combo_end.grid(row=1, column=1)

result_box = tk.Text(root, height=15, width=70)
result_box.pack()


# ------------------ ACTION BUTTONS ------------------
def find_path():
    s = start_var.get()
    e = end_var.get()
    if not s or not e:
        return

    path, dist = dijkstra(s, e)

    result_box.delete("1.0", tk.END)

    if not path:
        result_box.insert(tk.END, "No path found.")
        return

    result_box.insert(tk.END, f"Shortest Path: {' → '.join(path)}\n")
    result_box.insert(tk.END, f"Distance: {dist} units\n")
    result_box.insert(
        tk.END, f"Estimated Time: {round(dist*0.8, 1)} minutes\n")
    result_box.insert(tk.END, f"Steps: {len(path)}\n\n")

    result_box.insert(tk.END, "--- 3 Best Routes ---\n")
    for p in k_shortest(s, e):
        d = sum(G[p[i]][p[i+1]]['weight'] for i in range(len(p)-1))
        result_box.insert(
            tk.END, f"{' → '.join(p)} (distance {d})\n")


def show_nearest():
    s = start_var.get()
    if not s:
        return
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, f"Nearest to {s}:\n\n")
    for place, d in nearest(s):
        result_box.insert(tk.END, f"{place} → {d} units\n")


ttk.Button(root, text="Find Best Route",
           command=find_path).pack(pady=5)
ttk.Button(root, text="Nearest Places",
           command=show_nearest).pack(pady=5)
ttk.Button(root, text="Show Campus Graph",
           command=draw_graph).pack(pady=5)

root.mainloop()
