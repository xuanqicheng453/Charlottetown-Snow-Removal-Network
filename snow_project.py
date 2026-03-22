import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse.linalg as spla

# 1.Load road network for Charlottetown
place_name = "Charlottetown, Prince Edward Island, Canada"

# Download road network (drivable streets)
G = ox.graph_from_place(place_name, network_type="drive")
print("Original graph:")
print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

# Quick plot of the full network
ox.plot_graph(G, node_size=10, edge_color='gray')

# Convert to undirected graph for network analysis
G = ox.convert.to_undirected(G)

# Extract the largest connected component
largest_cc = max(nx.connected_components(G), key=len)
G = G.subgraph(largest_cc).copy()

print("Largest connected component:")
print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

# 2.Build adjacency matrices
# Binary adjacency matrix (edges = 1)
A_binary = nx.to_numpy_array(G, weight=None)
print("Binary adjacency matrix shape:", A_binary.shape)

# Weighted adjacency matrix (weight = road length)
A_weighted = nx.to_numpy_array(G, weight="length")
print("Weighted adjacency matrix shape:", A_weighted.shape)

# 3. Compute basic node metrics
degrees = dict(G.degree())
avg_degree = sum(degrees.values()) / len(degrees)
max_degree = max(degrees.values())
print("Average degree:", round(avg_degree, 3))
print("Maximum degree:", max_degree)

# Plot degree distribution
plt.hist(degrees.values(), bins=20, color='skyblue')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# 4. Shortest path metric
print("Computing average shortest path length...")
avg_shortest_path = nx.average_shortest_path_length(G, weight="length")
print("Average shortest path length:", round(avg_shortest_path, 3))

# 5. Centrality measures
# Betweenness centrality
print("Computing betweenness centrality...")
betweenness = nx.betweenness_centrality(G, weight="length", normalized=True)
top5_betw = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 betweenness nodes:", top5_betw)

# Closeness centrality
print("Computing closeness centrality...")
closeness = nx.closeness_centrality(G, distance="length")
top5_close = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 closeness nodes:", top5_close)

# 6. Laplacian eigenvalues (spectral properties)
print("Computing smallest Laplacian eigenvalues...")
L = nx.laplacian_matrix(G)
# Compute 5 smallest eigenvalues
eigenvalues = spla.eigsh(L, k=5, which="SM", return_eigenvectors=False)
eigenvalues = sorted(eigenvalues)
print("Smallest 5 eigenvalues:", eigenvalues)

# 7. Network resilience analysis
G_res = G.copy()
# Remove top 5 betweenness nodes
for node, _ in top5_betw:
    G_res.remove_node(node)

largest_cc_after = max(nx.connected_components(G_res), key=len)
print("Largest component size after removal:", len(largest_cc_after))

# 8.Visualizations for professor

# 8a. Node size proportional to degree
node_sizes = [degrees[n]*20 for n in G.nodes()]
ox.plot_graph(G, node_size=node_sizes, node_color='blue', edge_color='gray', bgcolor='white')

# 8b. Node color proportional to betweenness centrality using matplotlib colormap
import matplotlib.cm as cm

node_color = [betweenness[n] for n in G.nodes()]
node_sizes = [20]*len(G.nodes())

# Normalize values for the colormap
norm = plt.Normalize(vmin=min(node_color), vmax=max(node_color))
colors = cm.viridis(norm(node_color))  # maps numbers to colors

# Plot the network
fig, ax = ox.plot_graph(
    G,
    node_size=node_sizes,
    node_color=colors,
    edge_color='gray',
    bgcolor='white'
)

# 8c. Highlight top 5% betweenness nodes
threshold = np.percentile(list(betweenness.values()), 95)
important_nodes = [n for n, v in betweenness.items() if v >= threshold]
colors = ['red' if n in important_nodes else 'blue' for n in G.nodes()]
ox.plot_graph(G, node_size=20, node_color=colors, edge_color='gray', bgcolor='white')

# 8d. Show fragmentation after removing top nodes
G_removed = G.copy()
G_removed.remove_nodes_from(important_nodes)
components = list(nx.connected_components(G_removed))
component_colors = {}
for i, comp in enumerate(components):
    for n in comp:
        component_colors[n] = i
node_colors = [component_colors.get(n, 0) for n in G_removed.nodes()]
import matplotlib.cm as cm

# Map component IDs to colors using a colormap
component_ids = [component_colors[n] for n in G_removed.nodes()]
norm = plt.Normalize(vmin=min(component_ids), vmax=max(component_ids))
colors = cm.tab20(norm(component_ids))

# Plot the fragmented network
fig, ax = ox.plot_graph(
    G_removed,
    node_size=20,
    node_color=colors,
    edge_color='gray',
    bgcolor='white'
)

# 8e. Optional: Fiedler vector (spectral clustering insight)
fiedler_vector = spla.eigsh(L, k=2, which='SM', return_eigenvectors=True)[1][:,1]

node_color_fiedler = fiedler_vector
import matplotlib.cm as cm

# Normalize Fiedler vector for coloring
norm = plt.Normalize(vmin=min(fiedler_vector), vmax=max(fiedler_vector))
colors = cm.plasma(norm(fiedler_vector))

# Plot with mapped colors
fig, ax = ox.plot_graph(
    G,
    node_size=20,
    node_color=colors,
    edge_color='gray',
    bgcolor='white'
)
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# Normalize Fiedler vector values
norm = plt.Normalize(vmin=min(fiedler_vector), vmax=max(fiedler_vector))
colors = cm.plasma(norm(fiedler_vector))  # map values to RGBA colors

# Plot graph with mapped colors
fig, ax = ox.plot_graph(
    G,
    node_size=20,
    node_color=colors,
    edge_color='gray',
    bgcolor='white'
)

# 9.Print street names for top nodes (real-world reference)
print("\nTop Betweenness Nodes with Street Names:\n")
for node, value in top5_betw:
    print(f"\nNode ID: {node}, Betweenness: {value:.6f}")
    edges = G.edges(node, data=True)
    street_names = set()
    for u, v, data in edges:
        if 'name' in data:
            if isinstance(data['name'], list):
                street_names.update(data['name'])
            else:
                street_names.add(data['name'])
    print("Connected streets:", street_names)

