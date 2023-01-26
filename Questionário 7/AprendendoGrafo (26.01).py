from pythonds.graphs import PriorityQueue,  Graph

def dijkstra(graph: Graph,start_vertex):
    priority_queue = PriorityQueue()
    start_vertex.setDistance(0)

    priority_queue.buildHeap([(v.getDistance(),v) for v in graph])

    while not priority_queue.isEmpty():
        current_vert = priority_queue.delMin() # remove quem tem menor prioridade
    
    for next_vert in current_vert.getConnections():
        new_distance = current_vert.getDistance() + current_vert.getWeight(next_vert)

        if new_distance < nextVert(newDist):
            nextVert.setDistance(new_distance)
            nextVert.setPred(current_vert)
            



for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)


dijkstra('a',3)

