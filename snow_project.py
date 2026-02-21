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

# 1️⃣ 下载Charlottetown的可驾驶道路网络
place_name = "Charlottetown, Prince Edward Island, Canada"

G = ox.graph_from_place(
    place_name,
    network_type="drive"
)

# 2️⃣ 转换为GeoDataFrame
nodes, edges = ox.graph_to_gdfs(G)

print("Number of nodes:", len(nodes))
print("Number of road segments:", len(edges))
print(edges.head())

# 3️⃣ 画图展示
fig, ax = ox.plot_graph(G)

# 4️⃣ 保存为shapefile给教授
edges.to_file("charlottetown_roads.shp")