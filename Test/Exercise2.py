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


def pagerank(G, d=0.85, tol=1e-6, max_iter=100):


    A = nx.adjacency_matrix(G).todense()

    n = A.shape[0]
    r = np.ones((n, 1)) / n
    for i in range(max_iter):
        r_new = d * A @ r + (1 - d) / n * np.ones((n, 1))
        if np.linalg.norm(r - r_new) < tol:
            break
        r = r_new

    r /= np.sum(r)

    pagerank_dict = {node: r[i, 0] for i, node in enumerate(G.nodes())}
    return pagerank_dict

def dict_difference(d1, d2):
    diff_dict = {}
    for key in set(d1).intersection(set(d2)):
        diff_dict[key] = abs(((d1[key] - d2[key])/d2[key]))*100
    return diff_dict


graph = nx.read_edgelist("test1_digraph_treated.txt")
digraph = nx.DiGraph(graph)


print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

rank_mine=pagerank(graph, d=0.85, tol=1e-6, max_iter=100)
rank_nx=nx.pagerank(graph,alpha=0.85)

print("The page rank, according to networkX, is:", rank_nx)
print("The page rank, according to me, is:", rank_mine)

diff_dict=dict_difference(rank_mine,rank_nx)

print(diff_dict)
#The relative diference of the page rank is 16% at max. One could say my method works.


nx.draw_networkx(digraph, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()



"""
In the PageRank algorithm, the damping factor d represents the probability that a user will 
continue to follow links on the current page, as opposed to jumping to another page. 
When d tends to 1, it means that users are increasingly likely to follow links on the current page and less likely to jump to other pages at random.
Setting d close to 1 tends to result in a more evenly distributed PageRank among the vertexes in the graph,
since users are less likely to get stuck on a subset of highly connected nodes. 
As one can see, if I set my values closer to one the variance of the page rank dict goes down.
"""