import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse.linalg as spla
import matplotlib.cm as cm

# 1. LOAD NETWORK
place_name = "Charlottetown, Prince Edward Island, Canada"

G = ox.graph_from_place(place_name, network_type="drive")
G = ox.convert.to_undirected(G)

# largest connected component
largest_cc = max(nx.connected_components(G), key=len)
G = G.subgraph(largest_cc).copy()

print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

# 2. BASIC METRICS
degrees = dict(G.degree())
avg_degree = np.mean(list(degrees.values()))
max_degree = max(degrees.values())

print("Avg degree:", round(avg_degree, 3))
print("Max degree:", max_degree)

plt.figure()
plt.hist(degrees.values(), bins=20)
plt.title("Degree Distribution")
plt.show()

# 3. SHORTEST PATH
avg_sp = nx.average_shortest_path_length(G, weight="length")
print("Average shortest path:", round(avg_sp, 2))

# 4. CENTRALITY
betweenness = nx.betweenness_centrality(G, weight="length", normalized=True)
closeness = nx.closeness_centrality(G, distance="length")

top_betw = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop Betweenness Nodes:")
for n, v in top_betw:
    print(n, v)

# 5. SPECTRAL ANALYSIS
L = nx.laplacian_matrix(G)
eigs = spla.eigsh(L, k=5, which="SM", return_eigenvectors=False)
print("\nSmallest eigenvalues:", sorted(eigs))


# 6. RESILIENCE TEST
G_res = G.copy()
for n, _ in top_betw:
    G_res.remove_node(n)

largest_after = len(max(nx.connected_components(G_res), key=len))
print("\nLargest component after attack:", largest_after)



# 7. VISUALIZATION FUNCTIONS
def plot_network(G, values, title, cmap="viridis"):
    norm = plt.Normalize(min(values), max(values))
    colors = plt.colormaps[cmap](norm(values))
    fig, ax = ox.plot_graph(
        G,
        node_size=20,
        node_color=colors,
        edge_color="gray",
        bgcolor="white"
    )
    plt.title(title)


# Betweenness map
plot_network(G, list(betweenness.values()), "Betweenness Centrality")

# =========================
# 8. DEGREE vs BETWEENNESS
# =========================
deg_list = [degrees[n] for n in G.nodes()]
bet_list = [betweenness[n] for n in G.nodes()]

plt.figure()
plt.scatter(deg_list, bet_list, alpha=0.5)
plt.xlabel("Degree")
plt.ylabel("Betweenness")
plt.title("Degree vs Betweenness")
plt.show()

# =========================
# 9. TOP NODES BAR CHART
# =========================
top15 = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:15]
labels = [str(x[0]) for x in top15]
values = [x[1] for x in top15]

plt.figure(figsize=(10, 4))
plt.bar(labels, values)
plt.xticks(rotation=90)
plt.title("Top 15 Betweenness Nodes")
plt.show()

# 10. FIEDLER VECTOR
eigvals, eigvecs = spla.eigsh(L, k=2, which="SM", return_eigenvectors=True)
fiedler = eigvecs[:, 1]

plot_network(G, fiedler, "Fiedler Vector (Spectral Partition)")