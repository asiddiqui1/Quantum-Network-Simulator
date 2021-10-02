# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:48:23 2018

@author: User
"""

import networkx as nx
import numpy as np
from TimedNetwork import TimedNetwork
import matplotlib.pyplot as plt


class NodeDeletion(TimedNetwork):
    deleted_nodes = []

    def __init__(self, P_reentry, P_deletion , mem_max, mem_life, p_spdc=1,  subgraph=None, graph = nx.Graph() ):
        super(NodeDeletion, self).__init__(graph, subgraph, p_spdc, mem_max, mem_life)
        self.deletion_pr = P_deletion
        self.reentry_pr = P_reentry
        self.original_graph = graph.copy()
        
    #Removes a random node
    def node_deletion(self, random_node):
        #print("Deleted: %s" % str(random_node))
        self.graph.remove_node(random_node)
        self.deleted_nodes.append(random_node)
    
    #Adds a random deleted node    
    def node_reentry(self, random_node):
        #print("Reentered: %s" % str(random_node))
        node_positions = nx.get_node_attributes(self.original_graph, "pos")
        self.graph.add_node(random_node, pos=node_positions[random_node])
        self.graph.add_edges_from(self.original_graph.edges(random_node))
        self.deleted_nodes.remove(random_node)
        nx.set_node_attributes(self.graph, node_positions, "pos")
        
    def simulate(self):
        i = 0
        randomNum = np.random.uniform(size = len(self.graph))
        for node in list(self.graph.nodes):
            if randomNum[i] < self.deletion_pr:
                self.node_deletion(node)
            i+=1
        
        j = 0        
        randomNum2 = np.random.uniform(size=len(self.deleted_nodes))
        for node in list(self.deleted_nodes):
            if randomNum2[j] < self.reentry_pr:
                self.node_reentry(node)
            j+=1

        super(NodeDeletion, self).simulate()
            
            
def node_deletion_from_network(network, p_spdc, mem_max, mem_life, p_del, p_re):
    return NodeDeletion( \
        graph=network.graph, subgraph=network.subgraph, \
        p_spdc=p_spdc, mem_max=mem_max, mem_life=mem_life,
        P_deletion=p_del, P_reentry = p_re)

