from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(start): #em que o start é o vertice do qual se começa a busca em largura
    start.setDistance(0)
    start.setPred(None)

    vert_queue = Queue() #fila
    vert_queue.enqueue(start)

    while vert_queue.size() >0:
        current_vert = vert_queue.dequeue()
        
        for nbr in current_vert.getConnections():
            if nbr.getColor() == 'white': #ou seja, se eu ainda não percorri esse vizinho. A cor branco indica que ele acabou de ser inicializado e aidnda n fio identificado
                nbr.setColor('gray')
                nbr.setDistance(current_vert.getDistance()+1)
                nbr.setPred(current_vert)
                vert_queue.enqueue(nbr)
        current_vert.setColor('black')

#acima temos a busca em largura, ou seja, mostra todos que estão conectados ao elemento sem 1 salto, 2 saltos, 3 saltos, etc

# g = Graph()
# v = g.getVertex(0)
# bfs(v)

class DFSGraph(): 
    def __init__(self) -> None:
        super().__init__()
        self.time = 0

    def dfs(self): #criamos um método em DFSGraph; Queremos ua recursão indireta
        for vert in self: #sendo o SELF um objeto de grafo
            vert.setCOlor('white') 
            vert.setPred(-1)

        for vert in self:
            if vert.getColor() == 'white': #começa o processo recursivo só no branco
                self.dfs_visit(vert)

    def dfs_visit(self,start_vertex):
        start_vertex.setColor('gray')
        self.time += 1
        start_vertex.setDiscovery(self.time)

        for nextVert in start_vertex.getConnections():
            if nextVert.getColor() == 'white':
                nextVert.setPred(start_vertex)
                self.dfs_visit(nextVert)

            self.setColor('back')
            self.time += 1
            start_vertex.setFinish(self.time)







