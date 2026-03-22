# Charlottetown Snow Removal Network Analysis

**Author:** Xuanqi Cheng  
**Project Type:** Work-integrated Research / Urban Network Analysis  
**Advisor:** Justin Kakeu  
**Technologies:** Python, OSMnx, NetworkX, GeoPandas, Matplotlib, SciPy  

---

## Project Overview
This project analyzes the road network of Charlottetown, Prince Edward Island, Canada using graph theory and spatial network analysis. The goal is to understand network structure, identify critical intersections, and evaluate network resilience under disruption scenarios. The results provide insights for snow removal prioritization and urban infrastructure planning.

---

## Key Findings

- The network consists of **1,444 nodes** and **3,762 edges**.
- The average degree is **2.918**, indicating a relatively sparse but well-connected urban structure.
- The average shortest path length is **4,142 meters**, reflecting a compact city layout.
- A small number of intersections carry a large proportion of shortest-path traffic based on betweenness centrality.
- Key intersections are primarily located along major corridors such as:
  - University Avenue  
  - Belvedere Avenue  
  - Mount Edward Road  
  - St Peters Road  
  - North River Road  
- These intersections represent critical connectivity points within the network.

---

## Methodology

### 1. Network Extraction
- Road network retrieved from OpenStreetMap using **OSMnx**
- Converted into a graph representation (intersections = nodes, roads = edges)
- Analysis performed on the **largest connected component**

### 2. Network Metrics
- **Degree distribution**: measures local connectivity of intersections
- **Shortest path analysis**: evaluates overall accessibility
- **Betweenness centrality**: identifies critical routing intersections
- **Closeness centrality**: measures accessibility from each node
- **Spectral analysis**: Laplacian eigenvalues and algebraic connectivity

### 3. Network Resilience
- Top 5% highest betweenness nodes were removed
- Impact measured using largest connected component size
- Used to simulate disruption scenarios (e.g., blocked roads during snow events)

---

## Results Summary

- Network size: 1,444 nodes / 3,762 edges  
- Average shortest path length: 4,142 meters  
- Maximum node degree: 5  
- Algebraic connectivity: 0.001649  
- After removal of critical nodes: largest component reduced from 1,444 to 1,438 nodes  

---

## Interpretation

The Charlottetown road network is generally compact and efficient, with most areas accessible through short paths. However, connectivity is not uniformly distributed. A small number of high-centrality intersections act as structural bottlenecks, meaning that disruptions at these locations could disproportionately affect mobility.

The resilience analysis shows that while global connectivity remains largely stable under targeted node removal, peripheral accessibility is more vulnerable. This highlights the importance of prioritizing key intersections in snow removal and maintenance strategies.

---

## Files

| File | Description |
|------|-------------|
| `snow_project.py` | Main analysis script (network construction, metrics, visualization) |
| `charlottetown_roads.csv` | Extracted road network data |
| `README.md` | Project documentation |

---

## How to Run

Install dependencies:
```bash
pip install osmnx networkx geopandas matplotlib scipy