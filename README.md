# Quantum-Network-Simulator  
Corey Matyas, Aliza Siddiqui, 2018   
Code was written to aid the following work: https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.1.023032  

This module was designed to simulate and test the robustness quantum networks with several nodes in different topologies.   
One of the main issues with any network is communication server (node) failure.   
For every type of topology studied, the code:  
* Simulates node failure by random removal of nodes
* Finds the largest connected cluster

This will judge how durable specific network architectures are to unforeseen malfunctioning. 


Dependencies  
* Python 3.6 (or probably any Python3)
* numpy
* NetworkX 2.1+
* matplotlib  
  
Running
* pip install -r requirements.txt
* python qns/qns.py
