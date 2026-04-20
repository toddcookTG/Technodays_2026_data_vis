# Technodays 2026 — Data Visualisation Training

Hands-on Jupyter notebook training for data visualisation with Python, using real EU research collaboration data from [CORDIS](https://cordis.europa.eu/).

---

## Contents

| File | Description |
|---|---|
| `networkx/networkx.ipynb` | NetworkX training notebook — small worked example then a hands-on exercise |
| `networkx/networkx_cordis_solution.ipynb` | NetworkX reference solution — CORDIS collaboration network |
| `geopandas/geopandas.ipynb` | GeoPandas training notebook — UK regions choropleth then a hands-on exercise |
| `geopandas/geopandas_cordis_solution.ipynb` | GeoPandas reference solution — CORDIS funding mapped across Europe |
| `assets/cordis_orgs.csv` | CORDIS organisation participation data (one row per org per project) |
| `assets/UK_counties/` | UK regions shapefile |
| `assets/europe_countries/` | Europe countries shapefile |
| `template/` | TG house style — colours, fonts, matplotlib/plotly configuration |
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

### 4. Open a notebook in VS Code

Open any notebook in VS Code, click **Select Kernel** in the top-right corner, and choose **technodays_data_vis** from the list.

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

### `networkx/networkx_cordis_solution.ipynb` — NetworkX Reference Solution

Full solution to the exercise using real CORDIS data from the Clean Energy cluster (Horizon Europe 2022).

- Filters to `masterCall == 'HORIZON-CL5-2022-D2-01'`
- Extracts country codes from VAT number prefixes
- Builds a collaboration graph (nodes = orgs, edges = shared projects)
- Visualises with edge width, node size, and node colour by country
- Runs community detection and centrality analysis on the top 60 most-connected organisations
- Interactive visualisation with **PyVis** — outputs a standalone HTML file (`cordis_network_interactive.html`) with hover tooltips, drag-to-rearrange, and zoom; embeddable on any website via `<iframe>`

---

### `geopandas/geopandas.ipynb` — GeoPandas Training Notebook

Work through a UK regions choropleth using made-up data to learn the core GeoPandas workflow, then attempt the **Your Turn** exercise using real CORDIS data.

1. Reading a shapefile — UK regions
2. Exploring the GeoDataFrame
3. Choropleth map (colour by value)
4. Styled map with TG colours
5. Layered map — regions + cities
6. **Your Turn** — map CORDIS funding per country across Europe using `assets/cordis_orgs.csv` and the Europe shapefile

### `geopandas/geopandas_cordis_solution.ipynb` — GeoPandas Reference Solution

Full solution mapping EU research funding across European countries using CORDIS data.

- Filters to `masterCall == 'HORIZON-CL5-2022-D2-01'`
- Extracts country codes from VAT number prefixes and aggregates funding per country
- Merges onto the Europe shapefile via 2-letter ISO country code
- Choropleths for total funding and number of organisations
- Side-by-side comparison of funding vs. organisation count
- Adjustable label positions for polished annotation
