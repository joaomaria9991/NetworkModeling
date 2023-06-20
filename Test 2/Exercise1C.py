import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math





def occupy_edges(graph, probability):
    occupied_graph = nx.create_empty_copy(graph)
    
    for node1, node2 in graph.edges():
        r = random.random()
        if r <= probability:
            occupied_graph.add_edge(node1, node2)
    return occupied_graph


start = 0.01
end = 1.0
step = 0.01

p_vals = np.arange(start, end + step, step)
relative_sizes_list=[]

L=20
graph=nx.grid_graph([L,L,L])


for i in p_vals:
    p=i
    H = occupy_edges(graph, p)
    GIANT_COMP=max(nx.connected_components(H), key=len)
    component_size = len(GIANT_COMP)
    relative_size = component_size / graph.number_of_nodes()
    relative_sizes_list.append(relative_size)




#PLOT
plt.figure(1)
plt.plot(p_vals,relative_sizes_list, color='red')
plt.xlabel('Probability Values')
plt.ylabel('Relative Size')
plt.title('Relative Size of Giant Component S with probability of occupation')
plt.show()


print("Now the Graph has more degrees of liberty, it has 6 first neighborus, therefore <q>=6")
print("By observing the graph we can see that the singularity (p_c) occurs around p=0.2")
print("Once again if we substitute <q> in the theoretical expression it returns 0.2, which proves the mean field theory")