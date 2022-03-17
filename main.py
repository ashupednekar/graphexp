from igraph import Graph, plot
import matplotlib.pyplot as plt

# from collections import namedtuple
# Graph = namedtuple('Graph', ['nodes', 'edges'])

nodes = ['banking', 'account', 'loan', 'card', 'saving', 'current', 'home', 'car', 'debit', 'credit', 'gold', 'classic']
edges = [
    ('banking', 'account'),
    ('banking', 'loan'),
    ('banking', 'card'),
    ('account', 'saving'),
    ('account', 'current'),
    ('loan', 'home'),
    ('loan', 'car'),
    ('card', 'debit'),
    ('card', 'credit'),
    ('saving', 'gold'),
    ('saving', 'classic'),
    ('current', 'gold'),
    ('current', 'classic'),
    ('debit', 'gold'),
    ('debit', 'classic'),
    ('credit', 'gold'),
    ('credit', 'classic'),
]

graph = Graph()
graph.add_vertices(nodes)
graph.add_edges(edges)

account = graph.vs.find(name='account')
current = graph.vs.find(name='current')
classic = graph.vs.find(name='classic')
"""['__class__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'all_edges', 'attribute_names', 'attributes', 'betweenness', 'closeness', 
'constraint', 'degree', 'delete', 'diversity', 'eccentricity', 'get_shortest_paths', 'graph', 'in_edges', 'incident', 
'indegree', 'index', 'is_minimal_separator', 'is_separator', 'neighbors', 'out_edges', 'outdegree', 'pagerank', 
'personalized_pagerank', 'predecessors', 'shortest_paths', 'strength', 'successors', 'update_attributes'] """
# print(account < current)
# print(classic < current)


print([x for x in current.neighbors() if x < current])
print([x for x in current.neighbors() if x > current])



#
# fig, ax = plt.subplots()
# visual_style = {}
# visual_style["vertex_size"] = 20
# visual_style["vertex_label"] = graph.vs["name"]
# visual_style["layout"] = graph.layout()
# visual_style["bbox"] = (300, 300)
# visual_style["margin"] = 20
# plot(graph, **visual_style, target=ax)
# plt.show()
