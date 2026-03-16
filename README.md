# Technodays 2026 — Data Visualisation Training

Hands-on Jupyter notebook training for data visualisation with Python, using **NetworkX** for network/graph analysis applied to real EU research collaboration data from [CORDIS](https://cordis.europa.eu/).

---

## Contents

| File | Description |
|---|---|
| `networkx.ipynb` | Training notebook — small worked example then a hands-on exercise |
| `cordis_networkx.ipynb` | Reference solution — full CORDIS collaboration network |
| `cordis_orgs.csv` | CORDIS organisation participation data (one row per org per project) |
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

## Notebooks

### `networkx.ipynb` — Training Notebook

Work through a small made-up dataset (6 orgs, 5 projects) to learn the core NetworkX workflow, then attempt the **Your Turn** exercise using real CORDIS data.

1. Small example dataset
2. Basic network graph
3. Styled visualisation — edge width, node size, node colour
4. Community detection (Greedy Modularity)
5. Centrality analysis (degree, betweenness, eigenvector, PageRank)
6. **Your Turn** — replicate the above with `cordis_orgs.csv`, filtered to `masterCall == 'HORIZON-CL5-2022-D2-01'`

### `cordis_networkx.ipynb` — Reference Solution

Full solution to the exercise using real CORDIS data from the Clean Energy cluster (Horizon Europe 2022).

- Filters to `masterCall == 'HORIZON-CL5-2022-D2-01'`
- Extracts country codes from VAT number prefixes
- Builds a collaboration graph (nodes = orgs, edges = shared projects)
- Visualises with edge width, node size, and node colour by country
- Runs community detection and centrality analysis on the top 60 most-connected organisations
- Interactive visualisation with **PyVis** — outputs a standalone HTML file (`cordis_network_interactive.html`) with hover tooltips, drag-to-rearrange, and zoom; embeddable on any website via `<iframe>`
