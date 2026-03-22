# Charlottetown Road Network Analysis

## Overview

This project applies graph theory and network science methods to analyze the structural properties of the road network in Charlottetown, Prince Edward Island (Canada). The city’s urban form is compact and spatially constrained, making it an ideal case study for investigating how topology influences accessibility, connectivity, and network vulnerability.

The road network is modeled as a weighted spatial graph, where intersections are nodes and road segments are edges. Using Python-based geospatial and network analysis tools, the study explores both local and global structural patterns in the urban system.

---

## Research Objectives

This project investigates the following:

- How is the Charlottetown road network structurally organized?
- Which intersections act as critical connectivity hubs?
- How robust is the network under targeted disruptions?
- How do spatial constraints influence accessibility and shortest-path structure?

---

## Methodology

The analysis is implemented using Python and open geospatial data from OpenStreetMap.

### Graph Construction
- Tool: OSMnx
- Representation: Weighted undirected graph G = (V, E)
- Nodes: Road intersections
- Edges: Road segments weighted by physical length

### Network Analysis
The following graph-theoretic measures are computed using NetworkX:

- Degree distribution (local connectivity)
- Shortest path length (accessibility)
- Betweenness centrality (flow dependency / bottlenecks)
- Closeness centrality (global accessibility)
- Spectral analysis using Laplacian matrix (algebraic connectivity, Fiedler vector)
- Network resilience under targeted node removal

Shortest path computations are performed using Dijkstra’s algorithm on weighted edges.

---

## Key Findings

- The network exhibits a sparse but well-connected structure, with most intersections having degree 2–3.
- High-betweenness nodes are concentrated along major arterial roads, indicating strong flow dependency on a limited number of intersections.
- Closeness centrality is highest in the city center, reflecting a clear accessibility gradient from core to periphery.
- Spectral analysis reveals moderate global connectivity with clear spatial clustering.
- Targeted removal of high-betweenness nodes significantly increases fragmentation compared to random failures, highlighting heterogeneous robustness.

---

## Tools and Libraries

- Python
- OSMnx
- NetworkX
- NumPy
- SciPy
- Matplotlib

---

## Visualization Examples

The project includes:

- Road network graph visualization
- Degree distribution histogram
- Betweenness centrality heatmap
- Closeness centrality spatial mapping
- Fiedler vector clustering visualization
- Network robustness simulation results

---

## Data Source

- OpenStreetMap (OSM)

---

## Significance

This project demonstrates how graph-theoretic and spectral methods can be used to analyze real-world urban infrastructure. The results highlight how spatial constraints and network topology jointly shape accessibility and vulnerability in small urban systems.

Such methods are relevant for:
- Urban planning
- Transportation optimization
- Infrastructure resilience analysis
- Spatial data science applications

---

## Author

Xuanqi Cheng  
University of Prince Edward Island  