# Charlottetown Snow Removal Network Analysis

**Author:** Xuanqi Cheng  
**Project Type:** Work-integrated Research / Network Analysis  
**Technologies:** Python, OSMnx, NetworkX, GeoPandas, Matplotlib, SciPy  

---

## Project Overview
This project analyzes the road network of **Charlottetown, Prince Edward Island, Canada** with a focus on understanding network structure, identifying critical intersections, and assessing network resilience. The goal is to move from abstract network metrics to spatially intuitive visualizations that can inform decision-making for snow removal and urban planning.

---

## Key Analyses
1. **Network Extraction**
   - Road network retrieved from OpenStreetMap using **OSMnx**.
   - Converted to an undirected graph and extracted the **largest connected component** for analysis.

2. **Network Metrics**
   - **Degree**: Average and maximum node degree; visualized via a histogram.
   - **Shortest Path**: Average shortest path length (weighted by road length).
   - **Centrality Measures**:
     - Betweenness centrality (top 5 nodes highlighted)
     - Closeness centrality (top 5 nodes highlighted)
   - **Spectral Properties**: Smallest Laplacian eigenvalues, optional Fiedler vector for cluster detection.

3. **Network Resilience**
   - Top 5 betweenness nodes removed to simulate network disruption.
   - Size of the largest connected component monitored after node removal.
   - Visualizations of network fragmentation by connected components.

4. **Visualizations**
   - Node size proportional to degree.
   - Node color representing centrality measures.
   - Edge thickness proportional to importance.
   - Critical nodes highlighted and network fragmentation shown.
   - Optional Fiedler vector visualized for structural clusters.

---

## Files
| File | Description |
|------|-------------|
| `snow_project.py` | Main Python script for data extraction, network analysis, and visualization |
| `charlottetown_roads.csv` | CSV export of the road network data |
| `README.md` | Project documentation |
| `figures/` *(optional)* | Folder containing final visualizations/maps |

---

## How to Run
1. Install required Python packages:
```bash
pip install osmnx networkx geopandas matplotlib scipy