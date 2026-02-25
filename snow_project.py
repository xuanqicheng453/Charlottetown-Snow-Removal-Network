import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place_name = "Charlottetown, Prince Edward Island, Canada"


G = ox.graph_from_place(place_name, network_type="drive")

print("Original graph:")
print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

ox.plot_graph(G)

import networkx as nx

G = ox.convert.to_undirected(G)


largest_cc = max(nx.connected_components(G), key=len)
G = G.subgraph(largest_cc).copy()

print("Largest connected component:")
print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

import numpy as np

A_binary = nx.to_numpy_array(G, weight=None)
print("Binary adjacency matrix shape:", A_binary.shape)


A_weighted = nx.to_numpy_array(G, weight="length")
print("Weighted adjacency matrix shape:", A_weighted.shape)

degrees = dict(G.degree())

avg_degree = sum(degrees.values()) / len(degrees)
max_degree = max(degrees.values())

print("Average degree:", round(avg_degree, 3))
print("Maximum degree:", max_degree)

import matplotlib.pyplot as plt
plt.hist(degrees.values(), bins=20)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

print("Computing average shortest path length...")

avg_shortest_path = nx.average_shortest_path_length(G, weight="length")
print("Average shortest path length:", round(avg_shortest_path, 3))

print("Computing betweenness centrality...")

betweenness = nx.betweenness_centrality(G, weight="length", normalized=True)

top5 = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 betweenness nodes:", top5)

print("Computing closeness centrality...")

closeness = nx.closeness_centrality(G, distance="length")

top5_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 closeness nodes:", top5_closeness)

import scipy.sparse.linalg as spla

print("Computing smallest Laplacian eigenvalues...")

L = nx.laplacian_matrix(G)

eigenvalues = spla.eigsh(L, k=5, which="SM", return_eigenvectors=False)

eigenvalues = sorted(eigenvalues)

print("Smallest 5 eigenvalues:")
print(eigenvalues)

G_res = G.copy()

for node, _ in top5:
    G_res.remove_node(node)

largest_cc_after = max(nx.connected_components(G_res), key=len)

print("Largest component size after removal:",
      len(largest_cc_after))