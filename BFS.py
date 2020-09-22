#rabah gattfi
#9/20/2020

from collections import defaultdict
class GraphBFS: 

    
    def initial(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,fromNode,toNode): 
        self.graph[fromNode].append(toNode)

    
    def BFS(self, sourceNode): 
        
        visited = [False] * (len(self.graph)) 
        
        queue = [] 
    
        visited[ord(sourceNode)-65] = True
        queue.append(sourceNode) 
        
        while queue: 
            
            sourceNode = queue.pop(0) 
            print (sourceNode, end = " ") 
             
            for adjacentNode in self.graph[sourceNode]: 
                if visited[ord(adjacentNode)-65] == False: 
                    queue.append(adjacentNode) 
                    visited[ord(adjacentNode)-65] = True


graphBfs = GraphBFS() 
graphBfs.addEdge('A', 'B') 
graphBfs.addEdge('A', 'C') 
graphBfs.addEdge('B', 'A')
graphBfs.addEdge('B', 'C')
graphBfs.addEdge('B', 'D') 
graphBfs.addEdge('C', 'A') 
graphBfs.addEdge('C', 'B') 
graphBfs.addEdge('C', 'D') 
graphBfs.addEdge('C', 'E')
graphBfs.addEdge('D', 'B') 
graphBfs.addEdge('D', 'C')
graphBfs.addEdge('D', 'E')
graphBfs.addEdge('D', 'F')
graphBfs.addEdge('E', 'C')
graphBfs.addEdge('E', 'D')
graphBfs.addEdge('E', 'F')
graphBfs.addEdge('F', 'D')
graphBfs.addEdge('F', 'E') 
print ("Breadth First Traversal"
                  " (start from vertex A)") 

graphBfs.BFS('A')
