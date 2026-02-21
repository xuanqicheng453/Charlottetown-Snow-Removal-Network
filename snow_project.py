# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

place_name = "Charlottetown, Prince Edward Island, Canada"

G = ox.graph_from_place(
    place_name,
    network_type="drive"
)
nodes, edges = ox.graph_to_gdfs(G)
print("Number of nodes:", len(nodes))
print("Number of road segments:", len(edges))
print(edges.head())
fig, ax = ox.plot_graph(G)
edges.to_file("charlottetown_roads.shp")