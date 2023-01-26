from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue   
        
        

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

# def __str__(self):
#         return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
def recebeDados():
    numVertices = int(input())
    redeSocial = Graph()
    for i in range(numVertices):
        valores = input().split()
        for i in valores: 
            i = int(i)
        proprioId = valores.pop(0)    
        num_conexoes = valores.pop(0)

        vertex = Vertex(proprioId)
        for i in num_conexoes:
            vertex.addNeighbor(i)    
        redeSocial.addVertex(vertex)

    meuId,mussumId = input().split()
    meuId,mussumId = int(meuId),int(mussumId)


numVertices = int(input())
redeSocial = Graph()
for i in range(numVertices):
    valores = input().split()
    for i in valores: 
        i = int(i)
    proprioId = valores.pop(0)    
    num_conexoes = valores.pop(0)

    vertex = Vertex(proprioId)
    for i in num_conexoes:
        vertex.addNeighbor(i)    
    redeSocial.addVertex(vertex)

# for i in redeSocial.getVertices():
#     print(i)

for i in redeSocial:
    print(i)