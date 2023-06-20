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

L=100
graph=nx.grid_graph([L,L])


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
plt.xlabel('Probability Values (p)')
plt.ylabel('Relative Size (S)')
plt.title('Relative Size of Giant Component S with probability of occupation')
plt.show()

print("The p_c can be observed in the graph by observing at which point a singularity occurs. ")
print("This point occurs near the values at which p~=1/3")
print("This is confirmed by the theory if we susbstitute the <q>=4 in the p_c expression")
print("Therefore, when as n grows, the experiment tends to agree with the mean field theory")