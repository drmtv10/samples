#!/bin/python

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # breadth first traversal - print 
    def BFS(self, s):
        visited = list()
        for _ in range(len(self.graph)):
            visited.append(False)

        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print "{} ".format(s)

            #find adjacent vertices for dequeued s
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS_util(self, v, visited):
        visited[v] = True
        print "{} ".format(v)
        for i in self.graph[v]:
            if visited[i] == False:
                visited[i] = True
                self.DFS_util(i, visited)
        
    #Depth first traversal
    def DFS(self, v):
        visited = [False]*(len(self.graph))

        self.DFS_util(v, visited)
        
        
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    print g.graph
  
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
    g.BFS(2) 
    print ("Following is Depth First Traversal"
                  " (starting from vertex 2)") 
    g.DFS(2)
    """
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 0)") 
    g.BFS(0) 
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 3)") 
    g.BFS(3) 
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 1)") 
    g.BFS(1)
    """
