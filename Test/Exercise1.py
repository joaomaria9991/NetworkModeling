import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#I had some custom functions made for the opening the graph because I do not trust NetworkX native functions. This Is how I got my .txt from yours 

# def remove_third_word(input_file_path, output_file_path):
#     with open(input_file_path, 'r') as input_file:
#         with open(output_file_path, 'w') as output_file:
#             for line in input_file:
#                 words = line.strip().split()
#                 if len(words) >= 3:
#                     del words[2]
#                 output_file.write(' '.join(words) + '\n')

# input_file_path = 'test1_graph1.txt'
# output_file_path = 'test1_graph1_treated.txt'

# remove_third_word(input_file_path, output_file_path)




graph = nx.read_edgelist("test1_graph1_treated.txt")

print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())



degrees = dict(graph.degree())

mean_degree = sum(degrees.values()) / graph.number_of_nodes()

clustering_coefficient = nx.average_clustering(graph)


print("Mean degree of the graph:", mean_degree)
print("The Clustering Coeficient of Zachary's Karate Club is: ", clustering_coefficient)



degree_hist = nx.degree_histogram(graph)


#plot the degree histogram
plt.figure(1)
plt.bar(range(len(degree_hist)), degree_hist)



#Generating a random graph with the same <q>:

degrees = [d for n, d in graph.degree()]
mean_degree = sum(degrees) / graph.number_of_nodes()
random_graph = nx.configuration_model(degrees)
random_graph = nx.Graph(random_graph)
degree_hist2 = nx.degree_histogram(random_graph)
clustering_coefficient = nx.average_clustering(random_graph)



print("Mean degree of the random graph:", mean_degree)
print("The Clustering Coeficient of the random graph is: ", clustering_coefficient)


#plot the degree histogram
plt.figure(1)
plt.bar(range(len(degree_hist2)), degree_hist2,color="red")

plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()




