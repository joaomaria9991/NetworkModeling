import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import math



def solve_equation(p, q):
    S = 0.5  # Initial guess for S

    # Iterate until a stable value of S is obtained
    while True:
        prev_S = S
        S = 1 - math.exp(-p * q * S)

        # Check for convergence
        if abs(S - prev_S) < 1e-6:
            break

    return S



def generate_er_graph(num_nodes, avg_degree):
    # Calculate the probability of creating an edge
    p = avg_degree / (num_nodes - 1)
    
    # Create an Erdős-Rényi graph
    graph = nx.Graph()
    graph.add_nodes_from(range(num_nodes))
    
    for node1 in range(num_nodes):
        for node2 in range(node1 + 1, num_nodes):
            if random.random() < p:
                graph.add_edge(node1, node2)
    
    return graph


def occupy_edges(graph, probability):
    # Create an empty graph
    occupied_graph = nx.create_empty_copy(graph)
    
    # Iterate over all edges in the original graph
    for node1, node2 in graph.edges():
        # Generate a random number between 0 and 1
        r = random.random()
        
        # Add the edge to the new graph with probability p
        if r <= probability:
            occupied_graph.add_edge(node1, node2)
    
    return occupied_graph



# Generate an Erdős-Rényi graph with approximately 3 mean degree
num_nodes = 1000  # Adjust the number of nodes as per your requirements
avg_degree = 3
graph = generate_er_graph(num_nodes, avg_degree)


# Compute the degrees of all nodes
degrees = dict(graph.degree())

# Compute the mean degree
mean_degree = sum(degrees.values()) / len(degrees)



start = 0.01
end = 1.0
step = 0.01

p_vals = np.arange(start, end + step, step)
relative_sizes_list=[]
theo_vals=[]


for i in p_vals:
    p=i
    H = occupy_edges(graph, p)
    GIANT_COMP=max(nx.connected_components(H), key=len)
    component_size = len(GIANT_COMP)
    relative_size = component_size / graph.number_of_nodes()
    relative_sizes_list.append(relative_size)
    theo_vals.append(solve_equation(p, mean_degree))


plt.figure(1)
plt.plot(p_vals,relative_sizes_list, color='red')
plt.plot(p_vals, theo_vals, linestyle='--',color='black')
plt.xlabel('Probability Values')
plt.ylabel('Relative Size')
plt.title('Relative Size of Giant Component S with probability of occupation')
plt.legend(['Simulated', 'Theoretical'], loc='lower right')  # Add a legend

plt.show()

