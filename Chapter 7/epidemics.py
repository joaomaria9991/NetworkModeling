import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import math




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


# Generate an Erdős-Rényi graph with approximately 3 mean degree
num_nodes = 100  # Adjust the number of nodes as per your requirements
avg_degree = 3
# Define parameters
dt = 0.1  # Length of each time step
beta = 0.08  # Infection probability
gamma = 0.1  # Recovery probability


G = generate_er_graph(num_nodes, avg_degree)

#Initialize states
state = 'S'
attributes = {node: state for node in G.nodes}
nx.set_node_attributes(G, attributes, 'state')
new_states = {node: G.nodes[node]['state'] for node in G.nodes}


#Take a random sample of nodes from the graph and infect thoose degenerates 
num_infected = 10
infected_nodes = random.sample(G.nodes, num_infected)

for node in infected_nodes:
    G.nodes[node]['state'] = 'I'


# Store SIR data

SUS=[]
INF=[]
REC=[]

# Simulation loop
while True:
    # Iterate over edges in the network
    for edge in G.edges:
        node1, node2 = edge

        # Check if the edge connects an infected node to a susceptible node
        if G.nodes[node1]['state'] == 'I' and G.nodes[node2]['state'] == 'S':
            # Infect the susceptible node with probability beta * dt
            if random.random() < beta * dt:
                new_states[node2] = 'I'
                new_states[node1] = 'I'

        elif G.nodes[node1]['state'] == 'S' and G.nodes[node2]['state'] == 'I':
            # Infect the susceptible node with probability beta * dt
            if random.random() < beta * dt:
                new_states[node1] = 'I'
                new_states[node2] = 'I'

    # Iterate over nodes in the network
    for node in G.nodes:
        # Check if the node is infected
        if G.nodes[node]['state'] == 'I':
            # Recover the node with probability gamma * dt
            if random.random() < gamma * dt:
                new_states[node] = 'R'

    # Update the node states with the new states
    nx.set_node_attributes(G, new_states, 'state')

    # Count the number of infected nodes
    num_infected = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'I')
    INF.append(num_infected)
    # Count the number of suscepitbles nodes
    num_sus = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'S')
    SUS.append(num_sus)
    # Count the number of recovered nodes
    num_rec = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'R')
    REC.append(num_rec)
    # Break the loop if there are no infected nodes left
    if num_infected == 0:
        break


print(beta/gamma)
time=range(len(SUS))

plt.figure(1)
plt.plot(time,SUS, color='blue')
plt.plot(time, INF,color='red')
plt.plot(time, REC,color='green')
plt.xlabel('Arbitrary Time')
plt.ylabel('  Percentage of Populations ')
plt.title('SIR Model')
plt.legend(['Susceptible', 'Infected','Recovered'], loc='lower right')  # Add a legend

plt.show()

