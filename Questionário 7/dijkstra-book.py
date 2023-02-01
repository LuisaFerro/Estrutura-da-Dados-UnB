from pythonds.graphs import PriorityQueue, Graph, Vertex

class VertexAlterado(Vertex):
    def __iter__(self):
        return iter(self.vertices.values())

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

g = Graph()
g.addVertex('u')
g.addVertex('v')
g.addVertex('w')
g.addVertex('x')
g.addVertex('y')
g.addVertex('z')
g.addEdge('u','v',2)
g.addEdge('u','x',1)
g.addEdge('u','w',5)
g.addEdge('v','x',2)
g.addEdge('v','w',3)
g.addEdge('x','w',3)
g.addEdge('x','y',1)
g.addEdge('y','w',1)
g.addEdge('w','z',5)
g.addEdge('y','z',1)

# u = g.getVertex('u')
# dijkstra(g,u)
# # print(g.getVertices())
# for v in g:
#     print(v)

v = g.getVertex('u')
for j in v.getConnections():
    print(j.getId())


# def getConnectionsListToVertex(self):
#     lista = []
#     for j in self.getConnections():
#         lista.append(j.getId())
#     return lista

