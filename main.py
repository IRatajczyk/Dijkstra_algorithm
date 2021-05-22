# -*- coding: utf-8 -*-
"""
Created on %(21.05)s

@author: %Igor Ratajczyk 400513
"""
import math
import json

class WeightedGraph:
    
    def __init__(self,matrix,weights):
        self.adj_matrix=matrix
        self.weights = weights
        self.adj_list=self.adjlist()

        
        
    def adjlist(self):
        adjmat=self.adj_matrix
        weight=self.weights
        dct = {} 
        iterator = len(adjmat)
        for i in range(iterator):
            acc_list = []
            for j in range(iterator):
                for k in range(adjmat[i][j]):
                    acc_list.append((j + 1,weight[i][j]))
                if acc_list: 
                    dct[i + 1] = acc_list 
        return dct
    

    
    
    def Dijkstra(self,start=None):
        Graph=self.adj_list
        if start == None:
            start = list(Graph.keys())[0]
        d={v: math.inf for v in Graph.keys()}
        d[start]=0
        p={v: -1 for v in Graph.keys()}
        Q=[key for key in Graph.keys()]
        Q.remove(start)
        prev=start
        while Q:
            for u in Q:
                for elem in Graph[prev]:
                    if elem[0] == u:
                        if d[prev] + elem[1] < d[u]:
                            d[u] = d[prev] + elem[1]
                            p[u] = prev
            prev=Q[0]
            for elem in Q:
                prev=elem if d[elem]<d[prev] else prev
            Q.remove(prev)
        return d,p
    
    def extract_Shortest_Path(self,begin,end):
        weights, result = self.Dijkstra(begin)
        x = result[end]
        path = [end]
        acc = 0
        while result[x] != -1:
            path.append(x)
            acc += weights[x]
            x = result[x]
        path.append(begin)
        return path[::-1], acc

        

        
        
H=WeightedGraph([
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    ],[
    [0, 2, 0, 3, 0, 0, 4, 0, 11, 0],
    [7, 0, 5, 13, 12, 1, 3, 0, 6, 0],
    [0, 14, 0, 0, 1, 0, 11, 1, 4, 0],
    [6, 11, 0, 0, 41, 32, 17, 0, 17, 0],
    [0, 1, 15, 2, 0, 0, 4, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 4, 0],
    [5, 0, 1, 32, 1, 27, 4, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 6, 1, 0],
    [21, 1, 0, 0, 1, 43, 1, 0, 87, 0],
    [0, 2, 1, 3, 0, 0, 17, 0, 90, 13],
    ]
    )

if __name__ == '__main__':
    
    print('Graph H:')
    
    with open('Exemplary_graph_con.json') as file:
        connections = json.load(file)
    with open('Exemplary_graph_weights.json') as file:
        weights = json.load(file)
    H=WeightedGraph(connections,weights)
    path,distance = H.extract_Shortest_Path(1,5)
    print('The path from ',path[0],' to ',path[-1], ' is: ',path)
    print('Total distance is equal to : ',distance)
        
    path,distance = H.extract_Shortest_Path(1,9)
    print('The path from ',path[0],' to ',path[-1], ' is: ',path)
    print('Total distance is equal to : ',distance)
    
    
    print('Graph G:')
    
    with open('Exemplary_graph_con_1.json') as file:
        connections = json.load(file)
    with open('Exemplary_graph_weights_1.json') as file:
        weights = json.load(file)
        
    G=WeightedGraph(connections,weights)
    path,distance = G.extract_Shortest_Path(2,8)
    print('The path from ',path[0],' to ',path[-1], ' is: ',path)
    print('Total distance is equal to : ',distance)
    
    path,distance = G.extract_Shortest_Path(5,6)
    print('The path from ',path[0],' to ',path[-1], ' is: ',path)
    print('Total distance is equal to : ',distance)
    
    
