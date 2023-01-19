class Vertex:
    def __init__(self,id):
        self.id = id
        self.connect_to = {}
    
    def add_neighbour(self,nbr,weight=0): #nbr= objeto que está passando, o vizinho;
        self.connect_to[nbr] = weight

    def del_neighbour(self,nbr):
        if nbr in self.connect_to:
            del self.connect_to[nbr]
    
    def get_connections(self):
        return self.connect_to.keys()

    def get_id(self):
        self.get_id = id
    
    def set_id(self,id):
        return self.id

    def get_weigh(self,nbr):
        return self.connect_to[nbr]

    def __str__(self) -> str:
        return f'{self.id} connected_to {[x.id for x in self.connect_to]}'

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vert = 0

    def __iter__(self): #indica a maneira com a qual os objetos dessa lista podem ser iterados
        return iter(self.vert_list.values()) #.values() -> retorna uma lista
        
    def add_vertex(self,key):
        self.vert_list[key] = Vertex(key)
        self.num_vert += 1
        
        return self.vert_list[key]

    def del_vertex(self,key):
        for i in self.vert_list.values(): #em que a chave é "v1","v2" e o valor é de fato valor do vértice
            i.del_neighbour(self.vert_list[key])
        
        if key in self.vert_list:
            del self.vert_list[key]
            self.num_vert -= 1
    
    def get_vertex(self,key):
        if key in self.vert_list:
            return self.vert_list[key]
        
        return None

    def add_edge(self, f, t, cost = 0): #f = vertice de origem | t = vertice destino
        if f not in self.vert_list: #em que o self é o próprio objeto
            self.add_vertex(f)

        if t not in self.vert_list:
            self.add_vertex(t)

        self.vert_list[f].add_neighbour(self.vert_list[t], cost)


            

v0 = Vertex('v0')
v1 = Vertex('v1')
v2 = Vertex('v2')
g = Graph()

for i in range(6):
    g.add_vertex(i)

g.add_edge(0,1,5) #vertice origem, vertice que conecta, 
g.add_edge(0,2,5)
g.add_edge(2,3,5)

for i in g:
    print(i)

#objetivo:

# v0.add_neighbour(v1)
# v0.add_neighbour(v2)
# v3 = 1

# # print(v0)
# # print(v1)

# v0.del_neighbour(v2)
# v0.del_neighbour(v3)

# # print(v0)
# # print(v0.get_weigh(v1))

