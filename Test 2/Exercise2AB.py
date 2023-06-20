import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math





# Define parameters
dt = 10
beta = 0.1
gamma = 0.05  


#Graph Creation
n=21
G=nx.star_graph(n)



state = 'S'
attributes = {node: state for node in G.nodes}
nx.set_node_attributes(G, attributes, 'state')
new_states = {node: G.nodes[node]['state'] for node in G.nodes}



node_with_max_degree = max(G.degree, key=lambda x: x[1])[0]


num_infected = 1
infected_nodes = random.sample(set(G.nodes) - {node_with_max_degree}, num_infected)

for node in infected_nodes:
    G.nodes[node]['state'] = 'I'



SUS=[]
INF=[]
REC=[]


REC_FINAL=[]


while True:
    for edge in G.edges:
        node1, node2 = edge

        if G.nodes[node1]['state'] == 'I' and G.nodes[node2]['state'] == 'S':
            if random.random() < beta * dt:
                new_states[node2] = 'I'
                new_states[node1] = 'I'

        elif G.nodes[node1]['state'] == 'S' and G.nodes[node2]['state'] == 'I':
            if random.random() < beta * dt:
                new_states[node1] = 'I'
                new_states[node2] = 'I'

    for node in G.nodes:
        if G.nodes[node]['state'] == 'I':
            if random.random() < gamma * dt:
                new_states[node] = 'R'

    nx.set_node_attributes(G, new_states, 'state')

    num_infected = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'I')
    INF.append(num_infected)
    num_sus = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'S')
    SUS.append(num_sus)
    num_rec = sum(1 for node in G.nodes if G.nodes[node]['state'] == 'R')
    REC.append(num_rec)
    if num_infected == 0:
        break




time=range(len(INF))

plt.figure(1)
plt.plot(time,SUS, color='blue')
plt.plot(time, INF,color='red')
plt.plot(time, REC,color='green')
plt.xlabel('Arbitrary Time')
plt.ylabel('  Percentage of Populations ')
plt.title('SIR Model')
plt.legend(['Susceptible', 'Infected','Recovered'], loc='lower right')  # Add a legend

plt.show()
