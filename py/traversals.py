#!/usr/bin/env python

# implementing BFS



class adjencyList:
    def __init__(self):
        self.adj = {}

    def add(self, from_val, to_val):

        if from_val not in self.adj:
            self.adj[from_val] = set()
        
        self.adj[from_val].add(to_val)


def bfs(adj_list: adjencyList):
    pass
