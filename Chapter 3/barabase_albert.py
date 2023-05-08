import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

N=100000
m=1


graph=nx.barabasi_albert_graph(N, m)


degree_hist = nx.degree_histogram(graph)

y=degree_hist
x=range(1,len(y)+1)

y_log=np.array(y)
x_log=np.array(x)

# plot the degree histogram
# plt.figure(1)
# plt.bar(range(len(degree_hist)), degree_hist)
# plt.xlabel('Degree')
# plt.ylabel('Frequency')
# plt.title('Degree Distribution')
# plt.plot(x, y)


# plt.show()


cum_dist=np.cumsum(degree_hist[::-1])[::-1]
y_log_cum=np.log(cum_dist+1)

#x=x[3:]
#y_log=y_log[3:]

fit=np.polyfit(np.log(x)[3:-3], (y_log_cum+1)[3:-3],1)
print(fit)

plt.figure(2)
#plt.bar(range(len(cum_dist)), cum_dist)
plt.plot(np.log(x)[3:-3], (y_log_cum+1)[3:-3])
plt.xlabel('Degree')
plt.ylabel('Cumulative Frequency')
plt.title('Cumulative Degree Distribution')
plt.show()



