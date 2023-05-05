import networkx as nx
import matplotlib.pyplot as plt
import pickle

n = 50  # number of nodes
p = 0.3 #0  # probability of edge creation

gilbert_graph = nx.erdos_renyi_graph(n, p)

# visualize the graph
nx.draw(gilbert_graph, with_labels=True)
plt.show()

with open('gilbert_graph.pkl', 'wb') as f:
    pickle.dump(gilbert_graph, f)