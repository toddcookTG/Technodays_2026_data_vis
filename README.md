# Technodays 2026 — Data Visualisation Training

Hands-on Jupyter notebook training for data visualisation with Python, starting with **NetworkX** for network/graph analysis.

---

## Contents

| File | Description |
|---|---|
| `networkx.ipynb` | Comprehensive NetworkX training notebook |
| `requirements.txt` | Python package dependencies |

---

## Setup

### Prerequisites
- [Python 3.11+](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- VS Code extensions:
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Register the kernel with Jupyter

```bash
python -m ipykernel install --user --name technodays_data_vis --display-name "technodays_data_vis"
```

### 4. Open the notebook in VS Code

Open `networkx.ipynb` in VS Code, click **Select Kernel** in the top-right corner, and choose **technodays_data_vis** from the list.

---

## NetworkX Notebook — Topics Covered

1. What is NetworkX?
2. Graph types (`Graph`, `DiGraph`, `MultiGraph`)
3. Adding nodes and edges
4. Node and edge attributes
5. Visualising graphs (layouts, custom styling)
6. Graph properties and inspection
7. Paths and connectivity algorithms
8. Centrality measures (degree, betweenness, PageRank, …)
9. Clustering coefficients and community detection
10. Classic graph generators (Erdős–Rényi, Barabási–Albert, Watts–Strogatz, …)
11. Building graphs from real-world data (pandas DataFrames)
12. Directed graphs and DAGs
13. Saving and loading graphs (GraphML, JSON, NumPy)
