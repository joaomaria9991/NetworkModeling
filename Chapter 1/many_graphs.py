import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


n_vals = [3,10,30,100,300,1000]  # number of nodes
p_vals=[]
for n in n_vals:
    p=2/(n-1)
    p_vals.append(p)
mean_degrees = {}
count=0
iter=range(1,50)

for n in n_vals:
        p=2/(n-1)

        for i in iter:
            gilbert_graph = nx.erdos_renyi_graph(n, p)
            mean_degree = sum(dict(gilbert_graph.degree()).values()) / float(len(gilbert_graph))
            mean_degrees[n] = mean_degree
 

values = list(mean_degrees.values())
plt.hist(values)
plt.show()

print(mean_degrees)
##### Theoretical Results####
#L=n()

