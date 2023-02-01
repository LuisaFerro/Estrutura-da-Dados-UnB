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

class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
               tmp = self.heapArray[i//2]
               self.heapArray[i//2] = self.heapArray[i]
               self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False
        
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

    def __iter__(self):
        return iter(self.vertices.values())
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)

    def getVertices(self):
        return list(self.vertices.keys())

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

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getConnections(self):
        return self.connectedTo.keys()
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

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

def recebeDados():
    numVertices = int(input())
    vizinhanca = Graph()

    for i in range(numVertices):
        valores = input().split()
        for i in range(len(valores)):
            valores[i] = int(valores[i])
        proprioId = valores.pop(0)    
        num_conexoes = valores.pop(0)

        while len(valores) != 0:
            dist = valores.pop(0)
            outraCasa = valores.pop(0)

            vizinhanca.addEdge(proprioId,outraCasa,dist)
            # vizinhanca.addEdge(outraCasa,proprioId,dist)

    return vizinhanca

def conectaDuto(vizinhanca):
    casas = vizinhanca.getVertices()
    menores_dist = []
    conexoesQueJaForam = []

    for i in casas:
        vertice = vizinhanca.getVertex(i)
        dijkstra(vizinhanca,vertice)
        menorDist = sys.maxsize
        subMenoresDist = []
        for j in vizinhanca:
            if j.getDistance() != 0 and j.getDistance() < menorDist:
                tupla = (vertice.getId(),j.getId())
                if tupla not in conexoesQueJaForam:
                    menorDist = j.getDistance()
                    conexoesQueJaForam.append((vertice.getId(),j.getId()))

        if menorDist != sys.maxsize:
            menores_dist.append(menorDist)
        
        print(conexoesQueJaForam)
    print(menores_dist)

    return menores_dist


	
# # 6
# 5 3 61 4 65 6 51 1
# 4 5 167 3 61 5 22 2 103 1 168 6
# 2 4 66 1 184 3 22 4 43 6
# 3 4 184 2 167 4 13 1 83 6
# 6 5 65 5 125 1 168 4 43 2 83 3
# 1 5 66 2 51 5 125 6 13 3 103 4

def inicio():
    vizinhanca = recebeDados()
    dist = conectaDuto(vizinhanca)
    print(f'R$ {float(sum(dist)*3.14)}')

inicio()

# vizi = recebeDados()
# conectaDuto(vizi)

# 3
# 1 2 6 2 7 3
# 2 2 6 1 20 3
# 3 2 7 1 20 2
