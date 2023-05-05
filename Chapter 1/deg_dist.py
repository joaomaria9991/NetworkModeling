import networkx as nx
import matplotlib.pyplot as plt

n = 100  # number of nodes
p = 0.3 #0  # probability of edge creation

gilbert_graph = nx.erdos_renyi_graph(n, p)


# get the degree histogram
degree_hist = nx.degree_histogram(gilbert_graph)

# plot the degree histogram
plt.bar(range(len(degree_hist)), degree_hist)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()


g=nx.gnp_random_graph(n, p, seed=None, directed=False)



degree_hist = nx.degree_histogram(g)

# plot the degree histogram
plt.bar(range(len(degree_hist)), degree_hist)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()