import sys
import networkx as nx
from network import Network, network_from_triangular_lattice
from TimedNetwork import TimedNetwork, timed_network_from_network

if __name__ == "__main__":
    net = timed_network_from_network(network_from_triangular_lattice(5, 7, p=0.5), \
            p_spdc=0.9, mem_max=4, mem_life=5)
    
    for i in range(20):
        net.simulate()
    
    print(net.get_entanglement_counts())
    net.draw()
