**Campus Navigation (Graph Theory Project)**
# Campus Navigation (Graph Theory Project)

**Brief**

This project models a campus as a weighted graph and provides a small GUI to compute shortest paths, k-shortest routes, nearest locations, and a visual graph. The main application is `campus.py` and it uses `networkx` for graph algorithms and `matplotlib` for visualization.

**Features**
- **Shortest Path:** Find the minimum-weight route between two locations (distance + estimated time).
- **K Shortest Paths:** Show alternate simple paths (top-k) between two nodes.
- **Nearest Locations:** List the 3 closest nodes from a chosen start.
- **Graph Visualization:** Display node positions and edge weights with Matplotlib.

**Requirements**
- **Python:** 3.8 or newer recommended.
- **Dependencies:** See [requirements.txt](requirements.txt). Primary libraries: `networkx`, `matplotlib`.
- **GUI toolkit:** `tkinter` (usually included with Python; on some Linux distros install `python3-tk`).

**Quick Install**

Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Run the App**

```bash
python campus.py
```

GUI usage:
- Choose `Start` and `Destination` from the dropdowns.
- Click **Find Best Route** to compute shortest path and list top-k alternatives.
- Click **Nearest Places** to show the three closest locations.
- Click **Show Campus Graph** to open a Matplotlib visualization window.

**Project Structure**
- `campus.py` — main GUI and graph code.
- `requirements.txt` — Python dependencies.
- `.gitignore` — files ignored by Git.

**How it works (brief)**
- The campus topology is defined by the `campus_graph` dictionary inside `campus.py`. Edges include a numeric weight representing distance/time.
- `networkx` builds a weighted Graph from that dictionary and computes shortest paths with `nx.shortest_path` and `nx.shortest_path_length` using the `weight` attribute.
- K-shortest simple paths are provided by `nx.shortest_simple_paths`.

**Customization**
- Edit the `campus_graph` mapping in `campus.py` to add/remove nodes or change edge weights.

**Examples**
- To get the shortest path from `Library` to `Gym`, run the app, choose those nodes, then click **Find Best Route**.

**Contributing**
- Fork the repository and open a PR. If you add new external packages, update `requirements.txt`.

**License**
- No license file is included. Add a `LICENSE` if you plan to publish this publicly (e.g., MIT, Apache-2.0).

**Files of interest**
- [campus.py](campus.py)
- [requirements.txt](requirements.txt)
- [.gitignore](.gitignore)


**Author**

- Muhammad Ahmed

**License**

This project is available under the MIT License — see [LICENSE](LICENSE).
