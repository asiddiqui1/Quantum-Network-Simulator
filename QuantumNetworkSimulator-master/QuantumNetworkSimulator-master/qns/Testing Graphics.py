# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:58:13 2018

@author: User
"""
import graphics as gp
import numpy as np
import time

def addEmptyList(Node_Edges):
    for x in range(28):
        Node_Edges[x] = [] #Adds empty list as value for each node(as a number) key
        
def simulate(Node_Edges, Node, deleted_nodes,win):
    #Node Deletion
    randomNum = np.random.uniform(size = 28)
    i = 0
    for node in Node:
        time.sleep(0.6)
        if randomNum[i] < 0.2:
            randomNode = Node[i]
            for edge in Node_Edges[i+1]:
                edge.undraw()
            randomNode.undraw()
            deleted_nodes.append(randomNode)
        i+=1
   
    #Node Re-entry     
    j = 0
    randomNum = np.random.uniform(size=len(deleted_nodes))
    for node in deleted_nodes:
        time.sleep(0.6)
        if randomNum[j] < 0.6:
            randomNode = deleted_nodes[j]
            pos = (Node.index(randomNode)) + 1
            for edge in Node_Edges[pos]:
                edge.draw(win)
            randomNode.draw(win)
            deleted_nodes.remove(randomNode)
        j+=1
    for node in deleted_nodes: #Goes back and re-deletes all the edges of the deleted nodes
        pos = (Node.index(node)) + 1
        for edge in Node_Edges[pos]:
            edge.undraw()
    #randomNode = Node[1]
    #for edge in Node_Edges[2]:
     #   edge.undraw()
    #randomNode.undraw()
  
def main():
    win = gp.GraphWin("Node Deletion Animation",600, 770)
    Node = [] #List of nodes
    Node_Edges = {} #Dictionary of node edges keyed by node number
    deleted_nodes = [] 
    addEmptyList(Node_Edges) 
    nodeNum = 0
    
    #Creating the lattice
    x = 0
    y = 0
    counter1 = 100
    counter2 = 750
    while y<= 15:
        if y == 0 or y % 6 == 0:
            counter1 = 100
            x = 0
            while x <= 24:
                if x==0:
                    c = gp.Circle(gp.Point(counter1,counter2),10)
                    Node.append(c)
                    nodeNum+=1
                    print(nodeNum)
                    c.setFill('darkgreen')
                    c.draw(win)
                    counter1+=100
                    x+=6
                elif x == 24:
                    c = gp.Circle(gp.Point(counter1,counter2),10)
                    Node.append(c)
                    nodeNum+=1
                    print(nodeNum)
                    c.setFill('darkgreen')
                    c.draw(win)
                    l = gp.Line(gp.Point(counter1-100,counter2),gp.Point(counter1,counter2))
                    Node_Edges[nodeNum].append(l)
                    Node_Edges[nodeNum-1].append(l)
                    l.draw(win)
                    counter1+=100
                    x+=6
                else:
                    c = gp.Circle(gp.Point(counter1,counter2),10)
                    Node.append(c)
                    nodeNum+=1
                    print(nodeNum)
                    c.setFill('darkgreen')
                    c.draw(win)
                    l = gp.Line(gp.Point(counter1-100,counter2),gp.Point(counter1,counter2))
                    Node_Edges[nodeNum].append(l)
                    Node_Edges[nodeNum-1].append(l)
                    l.draw(win)
                    counter1+=100
                    x+=6
            counter2-=100
            y+=3
        elif y%3 == 0:
            counter1 = 150
            x = 3
            while x<=21:
                if x==3: #First node in row
                    c = gp.Circle(gp.Point(counter1,counter2),10)
                    Node.append(c)
                    nodeNum+=1
                    print(nodeNum , "Adding into Node_Edges")
                    c.setFill('darkgreen')
                    c.draw(win)
                    if y!=15:
                        #templist = []
                        line1 = gp.Line(gp.Point(counter1-50,counter2-100),gp.Point(counter1,counter2)) #+4
                        Node_Edges[nodeNum].append(line1)
                        line2 = gp.Line(gp.Point(counter1-50,counter2+100),gp.Point(counter1,counter2))#-5
                        Node_Edges[nodeNum].append(line2)
                        line3 = gp.Line(gp.Point(counter1+50,counter2-100),gp.Point(counter1,counter2))#+5
                        Node_Edges[nodeNum].append(line3)
                        line4 = gp.Line(gp.Point(counter1+50,counter2+100),gp.Point(counter1,counter2))#-4
                        Node_Edges[nodeNum].append(line4)
                        Node_Edges[nodeNum-5].append(line2)
                        Node_Edges[nodeNum-4].append(line4)
                        Node_Edges[nodeNum+4].append(line1)
                        Node_Edges[nodeNum+5].append(line3)
                        #Node_Edges[nodeNum] = templist
                        line1.draw(win)
                        line2.draw(win)
                        line3.draw(win)
                        line4.draw(win)
                    else:
                        #templist = []
                        line1 = gp.Line(gp.Point(counter1-50,counter2+100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line1)
                        line2 = gp.Line(gp.Point(counter1+50,counter2+100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line2)
                        Node_Edges[nodeNum-5].append(line1)
                        Node_Edges[nodeNum-4].append(line2)
                       # Node_Edges[nodeNum] = templist
                        line1.draw(win)
                        line2.draw(win)
                    counter1+=100
                    x+=6
                else:
                    c = gp.Circle(gp.Point(counter1,counter2),10)
                    Node.append(c)
                    nodeNum+=1
                    print(nodeNum, "Adding into Node_Edges")
                    c.setFill('darkgreen')
                    c.draw(win)
                    if y!=15:
                        #templist = []
                        l = gp.Line(gp.Point(counter1-100,counter2),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(l) #Edge shared(horizontal)
                        line1 = gp.Line(gp.Point(counter1-50,counter2-100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line1)
                        line2 = gp.Line(gp.Point(counter1-50,counter2+100), gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line2)
                        line3 = gp.Line(gp.Point(counter1+50,counter2-100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line3)
                        line4 = gp.Line(gp.Point(counter1+50,counter2+100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line4)
                        #Node_Edges[nodeNum] = templist #adds list of edges as a value of key "node"
                        Node_Edges[nodeNum-1].append(l) #adds edge shared by two nodes to list of both nodes
                        Node_Edges[nodeNum-5].append(line2)
                        Node_Edges[nodeNum-4].append(line4)
                        Node_Edges[nodeNum+4].append(line1)
                        Node_Edges[nodeNum+5].append(line3)
                        line1.draw(win)
                        line2.draw(win)
                        line3.draw(win)
                        line4.draw(win)
                        l.draw(win)
                    else: # if its the topmost row
                        #templist = []
                        l = gp.Line(gp.Point(counter1-100,counter2),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(l)
                        line1 = gp.Line(gp.Point(counter1-50,counter2+100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line1)
                        line2 = gp.Line(gp.Point(counter1+50,counter2+100),gp.Point(counter1,counter2))
                        Node_Edges[nodeNum].append(line2)
                        #Node_Edges[nodeNum] = templist
                        Node_Edges[nodeNum-1].append(l)
                        Node_Edges[nodeNum-5].append(line1)
                        Node_Edges[nodeNum-4].append(line2)
                        line1.draw(win)
                        line2.draw(win)
                        l.draw(win)
                    counter1+=100
                    x+=6
            counter2-=100
            y+=3
    
    #Adding in source stations
    x3 = 6
    y3 = 0
    counter3 = 200
    counter4 = 750
    while y3 <=15:
        if y3 % 6 == 0 or y3 == 0:
            counter3 = 150
            x3 = 3
            while x3 <=21:
                c = gp.Circle(gp.Point(counter3, counter4),10)
                c.setFill('blue')
                c.draw(win)
                counter3+=100
                x3+=6
            counter4-=100
            y3+=3
        elif y3 % 3 == 0:
            counter3 = 200
            x3 = 6
            while x3 <=18:
                c = gp.Circle(gp.Point(counter3,counter4),10)
                c.setFill('blue')
                c.draw(win)
                counter3+=100
                x3+=6
            counter4-=100
            y3+=3
    
    x4 = 1.5
    y4 = 1.5
    counter5 = 125
    counter6 = 700
    while y4 <= 13.5:
        x4 = 1.5
        counter5 = 125
        while x4 <= 22.5:
            c = gp.Circle(gp.Point(counter5,counter6),10)
            c.setFill('blue')
            c.draw(win)
            counter5+=50
            x4+=3
        counter6-= 100
        y4+=3
    j = 0
    for node in Node:
        j+=1
    #print("Total amount of nodes in Node",j)
    print()
    print()
    #for k,v in Node_Edges.items():
    #    print(k,v)
    #    print()
    simulate(Node_Edges, Node, deleted_nodes, win)
    print("Animation DoneAnimation DoneAnimation DoneAnimation DoneAnimation DoneAnimation Done")
    win.getMouse()
    win.close()    # Close window when done

main()