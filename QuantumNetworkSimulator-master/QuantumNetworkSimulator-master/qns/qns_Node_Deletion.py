
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:57:12 2018

@author: User
"""

import sys
import networkx as nx
from network import Network, network_from_triangular_lattice
from NodeDeletion import NodeDeletion, node_deletion_from_network


if __name__ == "__main__":
    net = node_deletion_from_network( \
            network_from_triangular_lattice(6, 8, p=0.5), \
            p_spdc=0.9, mem_max=4, mem_life=5, p_del=0.02, p_re=0.2)  
    
    
    for i in range(30):
        net.simulate()
        net.draw_subgraph()
    
