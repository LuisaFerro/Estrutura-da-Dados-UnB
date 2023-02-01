2 4 66 1 184 3 22 4 43 6from pythonds.graphs import PriorityQueue,  Graph

def dijkstra(graph: Graph,start_vertex):
    priority_queue = PriorityQueue()
    start_vertex.setDistance(0)

    priority_queue.buildHeap([(v.getDistance(),v) for v in graph])

    while not priority_queue.isEmpty():
        current_vert = priority_queue.delMin() # remove quem tem menor prioridade
    
    for next_vert in current_vert.getConnections():
        new_distance = current_vert.getDistance() + current_vert.getWeight(next_vert)

        if new_distance < next_vert.getDistance():
            next_vert.setDistance(new_distance)
            next_vert.setPred(current_vert)
            priority_queue.decreaseKey(next_vert,new_distance)
            



# for nextVert in currentVert.getConnections():
#             newDist = currentVert.getDistance() \
#                     + currentVert.getWeight(nextVert)
#             if newDist < nextVert.getDistance():
#                 nextVert.setDistance( newDist )
#                 nextVert.setPred(currentVert)
#                 pq.decreaseKey(nextVert,newDist)

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

u = g.getVertex('u')
dijkstra(g,u)

for v in g:
    print(v)
