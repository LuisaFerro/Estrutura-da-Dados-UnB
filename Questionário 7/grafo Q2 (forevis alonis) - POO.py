import sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
        
                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
            
    def setDistance(self,d):
        self.dist = d
        
    def setColor(self,color):
        self.color = color
    
    def getColor(self):
        return self.color

    def getDistance(self):
        return self.dist

    def setPred(self,p):
        self.pred = p

    def getConnections(self):
        return self.connectedTo.keys()
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id


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

# def __str__(self):
#         return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
def recebeDados():
    numVertices = int(input())
    redeSocial = Graph()
    for i in range(numVertices):
        valores = input().split()
        proprioId = valores.pop(0)    
        num_conexoes = valores.pop(0)

        vertex = Vertex(proprioId)
        for i in valores:
            redeSocial.addEdge(proprioId,i)
            redeSocial.addEdge(i,proprioId)
            

    meuID,mussumID = input().split()
    
    return redeSocial,meuID,mussumID

def conexoes_ate_mussum(redeSocial,meuID,mussumID):
    if redeSocial.getVertex(mussumID) is None or redeSocial.getVertex(meuID) is None:
        return sys.maxsize
    else:        
        mussum = redeSocial.getVertex(mussumID)
        bfs(mussum)
        minhaRedeSocial = redeSocial.getVertex(meuID)
        distancia = minhaRedeSocial.getDistance()
        return distancia

def inicio():
    redeSocial,meuID,mussumID = recebeDados()
    distancia = conexoes_ate_mussum(redeSocial,meuID,mussumID)
    if distancia == sys.maxsize:
        print('Forevis alonis...')
    else:
        print(distancia-1)

inicio()

# redeSocial,meuID,mussumID = recebeDados()
# conexoes_ate_mussum(redeSocial,meuID,mussumID)
# print(mussumID)
# for i in redeSocial:
#     print(i)
#     print(f'a id acima é {type(i.getId())}')
#     if i.getId() == mussumID:
#         print('acima temos MUSSUM')
        
# distancia = conexoes_ate_mussum(redeSocial,meuID,mussumID)
# print(distancia)



# 9
# 1 1 2
# 2 2 3 4
# 3 3 2 5 6
# 4 3 2 7 8
# 5 1 3
# 6 1 3
# 7 2 4 9
# 8 1 4
# 9 1 7
# 1 9

# 3
# 1 2 2 3
# 2 2 1 3
# 3 2 1 2
# 3 1


# 7
# 1 1 6
# 2 1 6
# 3 1 6
# 4 1 6
# 5 1 6
# 6 5 1 2 3 4 5
# 7 0
# 7 6