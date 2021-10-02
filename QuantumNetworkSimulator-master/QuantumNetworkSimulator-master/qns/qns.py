#!/usr/bin/env python3

import sys
from network import Network, network_from_triangular_lattice, network_from_trihexagonal_lattice, network_from_square_lattice
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    prob = 0.1
    while prob < 1.00:
        prob = round(prob, 2)
        print("Probability: ", prob)
        
        #net = network_from_square_lattice(8,10,prob)
        #net = network_from_trihexagonal_lattice(8, 10, prob)
        net = network_from_triangular_lattice(8, 10, prob)
        sum = 0
        for m in range(10):
            net.draw()
            net.simulate()
            net.draw_subgraph()
            
            largest = net.size_largest_cluster()
            sum += largest[0]
            #print("Network: " + str(net.size()))
            #print("Subgraph: " + str(net.size_subgraph()))
            print("Largest Cluster: " + str(net.size_largest_cluster()))

        #After 10 runs, it takes the average of the largest clusters
        avg = sum/10.0
        print ("The average of the largest clusters of graphs with " \
               "probability %0.2f " % prob , "is " , avg )
        prob += 0.1

    sys.exit(0)
