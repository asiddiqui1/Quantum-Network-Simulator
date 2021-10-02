import networkx as nx
import numpy as np
from network import Network

KEY_ENTANGLEMENT = "entanglement"

class TimedNetwork(Network):
    time_step = 0
    
    def __init__(self, graph=nx.Graph(), subgraph=None, \
            p_spdc=1, mem_max=0, mem_life=1000):
        super(TimedNetwork, self).__init__(graph, subgraph, p_spdc)

        # Number of quantum memory units assigned to each edge endpoint
        self.mem_max = mem_max
        # Number of time steps that an entangled pair persists in memory
        self.mem_life = mem_life

        # Each edge starts with no entanglement
        # The dictionary comprehension is required for each edge to get its
        #  own empty list. Otherwise, they all get the SAME list reference.
        nx.set_edge_attributes(self.graph, \
            {e: [] for e in self.graph.edges()}, KEY_ENTANGLEMENT)
    
    def get_entanglement_counts(self):
        return {k: len(v) for k, v in \
            nx.get_edge_attributes(self.graph, KEY_ENTANGLEMENT).items()}

    def simulate(self):
        super(TimedNetwork, self).simulate()

        # Test edges for quantum memory decoherence. If the oldest entangled
        #  pair (index 0, FIFO) is older than mem_life, decohere it.
        entanglement = nx.get_edge_attributes(self.graph, KEY_ENTANGLEMENT)
        for e in entanglement:
            if len(entanglement[e]) > 0 and \
                    entanglement[e][0] + self.mem_life < self.time_step:
                entanglement[e].pop(0)

        # Increase entanglement count for edges entangled (in subgraph)
        # Mapping system needed because the node order in the subgraph edges
        #  is NOT retained by .add_edge(...).
        mapping = {tuple(sorted(e)): e for e in self.graph.edges()}
        for e in self.subgraph.edges():
            graph_edge = mapping[tuple(sorted(e))]
            if len(entanglement[graph_edge]) < self.mem_max:
                #print("Entangled: ", graph_edge)
                entanglement[graph_edge].append(self.time_step)

        nx.set_edge_attributes(self.graph, entanglement, KEY_ENTANGLEMENT)
        self.time_step += 1
                

def timed_network_from_network(network, p_spdc, mem_max, mem_life):
    return TimedNetwork( \
        graph=network.graph, subgraph=network.subgraph, \
        p_spdc=p_spdc, mem_max=mem_max, mem_life=mem_life)
    
        
    
