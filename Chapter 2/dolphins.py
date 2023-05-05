import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def prep_txt(graph_file):
	graph_edges=[]
	for line in graph_file:
				a= str(line).strip("\n").split(" ")
				res = [eval(i) for i in a]
				graph_edges.append(res)
	return graph_edges


def get_unique_numbers(numbers):
		list_of_unique_numbers = []

		unique_numbers = set(numbers)
		

		for number in unique_numbers:
			list_of_unique_numbers.append(number)

		return list_of_unique_numbers


graph_file= open("Chapter 2\soc-dolphins.txt", "r")
graph_edges=prep_txt(graph_file)
graph_vertex= get_unique_numbers([item for sub_list in graph_edges for item in sub_list]) #Flat na lista e apanha os valores únicos para vertices


graph=nx.Graph()
graph.add_nodes_from(graph_vertex)
graph.add_edges_from(graph_edges)

# visualize the graph
plt.figure(1)
nx.draw(graph, with_labels=True)
plt.show()


avg_degree = sum(dict(nx.average_degree_connectivity(graph)).values()) / float(len(graph))
cc = nx.average_clustering(graph)
msp = nx.average_shortest_path_length(graph)
diameter = nx.diameter(graph)



print("--------Measures------")
print("Number of nodes: ",len(graph_vertex))
print("Mean Degree: ",avg_degree)
print("Clustering Coefficient: ", cc)
print("Mean Shortest Path: ", msp)
print("Diameter: ", diameter)



# get the degree histogram
degree_hist = nx.degree_histogram(graph)



# compute the degree distribution and plot the histogram
degrees = [deg for node, deg in nx.degree(graph)]
degree_counts = Counter(degrees)
degree_vals, degree_counts = zip(*degree_counts.items())
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), align='left')

# compute the tendency line
tendency_degrees = np.linspace(min(degrees), max(degrees), num=100)
coefficients = np.polyfit(degree_vals, degree_counts, 1)
tendency_counts = np.polyval(coefficients, tendency_degrees)

# plot the tendency line
# plot the degree histogram
plt.figure(2)
plt.bar(range(len(degree_hist)), degree_hist)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')

plt.plot(tendency_degrees, tendency_counts, 'r--')

# show the plot
plt.show()