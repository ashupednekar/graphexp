import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

graph.add_node('A')
graph.add_nodes_from(['B', 'C', 'D', 'E'])

graph.add_edge(('A', 'B'), v_of_edge='belongs')
graph.add_edges_from([('A','C'), ('B','D'), ('B','E'), ('C', 'E')])

print(graph.nodes())

nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()