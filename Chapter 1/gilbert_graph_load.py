import networkx as nx
import pickle
import matplotlib.pyplot as plt


# load the graph from a file
with open('gilbert_graph.pkl', 'rb') as f:
    gilbert_graph = pickle.load(f)

# visualize the graph
nx.draw(gilbert_graph, with_labels=True)
plt.show()