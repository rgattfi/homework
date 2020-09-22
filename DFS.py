#rabah gattfi
#9/20/2020
from collections import defaultdict 
class GraphDFS: 

     
    def initial(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,fromNode,toNode): 
        self.graph[fromNode].append(toNode) 
     
        self.graph[fromNode].append(toNode)

    def DFS(self,node,visitedNodes):
        
        if node not in visitedNodes:
        
            visitedNodes.append(node)
            
            for adjacenctaNode in self.graph[node]:
                
                self.DFS(adjacenctaNode,visitedNodes)
        
        return visitedNodes


graphDfs = GraphDFS() 
graphDfs.addEdge('A', 'B') 
graphDfs.addEdge('A', 'C') 
graphDfs.addEdge('B', 'A')
graphDfs.addEdge('B', 'C')
graphDfs.addEdge('B', 'D') 
graphDfs.addEdge('C', 'A') 
graphDfs.addEdge('C', 'B') 
graphDfs.addEdge('C', 'D') 
graphDfs.addEdge('C', 'E')
graphDfs.addEdge('D', 'B') 
graphDfs.addEdge('D', 'C')
graphDfs.addEdge('D', 'E')
graphDfs.addEdge('D', 'F')
graphDfs.addEdge('E', 'C')
graphDfs.addEdge('E', 'D')
graphDfs.addEdge('E', 'F')
graphDfs.addEdge('F', 'D')
graphDfs.addEdge('F', 'E')
print (" Depth First Traversal"
                  " ( from vertex A)")

visitedOrder = graphDfs.DFS('A',[])
print(' '.join(visitedOrder))
