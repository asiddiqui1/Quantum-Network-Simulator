import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

KEY_PROB = "pr"

class Network:
    # A Network consists of a network topology (graph) and possibly a
    # subgraph that is the result of a simulation.
    # If subgraph == None, then this is just a network topology.
    # If subgraph != None, then subgraph is the simulation result for a
    #   topology given by graph.
    # p_spdc is the probability that an edge source produces a photon pair
    def __init__(self, graph=nx.Graph(), subgraph=None, p_spdc=1):
        self.graph = graph
        self.subgraph = subgraph
        self.p_spdc = p_spdc

    # Returns a dictionary of edge => probability
    def get_edge_probabilities(self):
        return nx.get_edge_attributes(self.graph, KEY_PROB)

    def size(self):
        return (len(self.graph), len(self.graph.edges()))

    # TODO: Duplicates size()
    def size_subgraph(self):
        if self.subgraph == None:
            raise ValueError("Network must contain a subgraph.")
        orphans = len(list(nx.isolates(self.subgraph)))
        return (len(self.subgraph) - orphans, len(self.subgraph.edges()))

    # Returns the size of the largest connected cluster of the Network subgraph
    # TODO: Partially duplicates size(). Decouple?
    def size_largest_cluster(self):
        if self.subgraph == None:
            raise ValueError("Network must contain a subgraph.")
        if len(self.subgraph) == 0:
            return (0, 0)
        largest = max(nx.connected_component_subgraphs(self.subgraph), key=len)
        return (len(largest), len(largest.edges()))

    # Returns True if the network is f-large.
    # That is, if (nodes / all possible nodes) >= f with 0 <= f <= 1
    def is_large(self, f):
        if f < 0 or f > 1:
            raise ValueError("f must be >= 0 and <= 1.")
        return (self.size_subgraph()[0] / self.size()[0]) >= f

    # TODO: Useful for interactive testing only.
    def draw(self):
        pos = nx.get_node_attributes(self.graph, "pos")
        nx.draw_networkx(self.graph, pos)
        plt.show()

    # TODO: Useful for interactive testing only. Also duplicates: draw()
    def draw_subgraph(self):
        pos = nx.get_node_attributes(self.subgraph, "pos")
        nx.draw_networkx(self.subgraph, pos)
        plt.show()

    def simulate(self):
        edges_pr = self.get_edge_probabilities()
        random = np.random.uniform(size=len(edges_pr))
        edges = zip([*edges_pr], random)

        self.subgraph = nx.create_empty_copy(self.graph)
        for e in edges:
            # We compare to p_spdc * edges_pr[...] because we want to know if
            #  a pair is generated AND entanglement occurs.
            #  => P(SPDC) * P(entanglement | SPDC) == p_spdc * edges_pr[..]
            if e[1] < (self.p_spdc * edges_pr[e[0]]):
                self.subgraph.add_edge(*e[0], **{KEY_PROB: edges_pr[e[0]]})
                
                
def network_from_file(filename):
    # https://networkx.github.io/documentation/stable/
    #           reference/readwrite/edgelist.html
    # TODO: Implement.
    raise NotImplementedError

# Create an (m,n) periodic triangular lattice network with Pr = p
def network_from_triangular_lattice(m, n, p):
    net = Network(nx.triangular_lattice_graph(m, n, with_positions=True, periodic=True))
    nx.set_edge_attributes(net.graph, p, KEY_PROB)
    return net

# Create an (m,n) periodic square lattice network with Pr = p
def network_from_square_lattice(m, n, p):
    net = Network(nx.grid_2d_graph(m, n, periodic=True))
    values={}
    for node in list(net.graph.nodes):
        pos = node
        values[node] = pos
    nx.set_node_attributes(net.graph,values, name = "pos")
    nx.set_edge_attributes(net.graph, p, KEY_PROB)
    return net 

# Create an (m,n) periodic trihexagonal lattice network with Pr = p
def network_from_trihexagonal_lattice(m,n,p):
    net = Network(nx.triangular_lattice_graph(m,n, with_positions=True, periodic=True))
    delete_positions = [(1,0),(3,0), (0,2), (2,2), (4,2), (1,4), (3,4), (0,6), (2,6), (4,6)]
    pos = nx.get_node_attributes(net.graph, "pos")
    for node,position in pos.items():
        if node in delete_positions:
            net.graph.remove_node(node)
    nx.set_edge_attributes(net.graph, p, KEY_PROB)
    return net
