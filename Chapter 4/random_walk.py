import networkx as nx
import random
import numpy as np

n=9
p=0.5

graph=nx.gnp_random_graph(n, p, seed=None, directed=False)


num_walkers = 1000
current_nodes = [random.choice(list(graph.nodes())) for _ in range(num_walkers)]

# perform 1000 steps of the random walk for each walker
num_steps = 10000
walkers_per_node = np.zeros((num_steps, graph.number_of_nodes()))
for i in range(num_steps):
    for j in range(num_walkers):
        # get the neighbors of the current node for the current walker
        neighbors = list(graph.neighbors(current_nodes[j]))
        
        # choose a random neighbor as the next node for the current walker
        if neighbors:
            next_node = random.choice(neighbors)
        else:
            # if the current node has no neighbors, choose a new starting node for the current walker
            next_node = random.choice(list(G.nodes()))
        
        # move to the next node for the current walker
        current_nodes[j] = next_node
        
        # update the count of walkers on the current node at the current step
        walkers_per_node[i, current_nodes[j]] += 1

print(walkers_per_node/num_walkers)

#Computing M theoretically

A = nx.adjacency_matrix(graph)
A2 = A.dot(A)
Q = np.diag(1/A2.diagonal()) #diagonal matrix with 1/degree as entries
M = A.dot(Q)

print(M)