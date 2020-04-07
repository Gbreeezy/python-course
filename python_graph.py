# Adjacency Matrix
# Square matrix used to represent a finite graph.
# Elements of the matrix indicate whether pairs of vertices are adjacent
# or not in the graph. If the graph is undirected, the adjacency matrix is symmetric.


class Graph:
    def __init__(self, size):
        self.adj = [] # Store matrix in 2 dim array
        for i in range(1, size+1):
            self.adj.append([0 for i in range(size)])   # take num of nodes and initialize all elements to 0
        self.size = size

    # adding and edge
    def add_edge(self, orig, dest):
        raise NotImplemented
    # removing and edge

    def remove_edge(self, orig, dest):
        raise NotImplemented

    # print the matrix
    def display(self):
        raise NotImplemented


# Sample Graph
g = Graph()
