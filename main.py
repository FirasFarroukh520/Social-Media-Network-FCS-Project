# main.py
 # imported the networkx as nx library
import networkx as nx 
# imported the matplotlib as plt library


import matplotlib.pyplot as plt 
# Implement graph visualization using Matplotlib 
 
def visualize_graph(graph):
    G = nx.Graph()
 
    for user, friends in graph.adjacency_list.items():
        for friend in friends:
            G.add_edge(user, friend)
 
    nx.draw(G, with_labels=True)
    plt.show()
 
# Example usage
class Graph:
    def __init__(self):
        self.adjacency_list = {}
 
    def add_edge(self, user, friend):
        if user not in self.adjacency_list:
            self.adjacency_list[user] = []
        self.adjacency_list[user].append(friend)
 
# Create a sample graph and visualize it
sample_graph = Graph()
sample_graph.add_edge('FIras', 'ali')
sample_graph.add_edge('FIras', 'Mahdi')
sample_graph.add_edge('ali', 'Hussein')
sample_graph.add_edge('Mahdi', 'Hussein')
 
visualize_graph(sample_graph)