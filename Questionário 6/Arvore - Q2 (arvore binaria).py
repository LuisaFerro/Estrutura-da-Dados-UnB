lista = []
deuRuim = False

class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def inorder(raiz):
    global lista

    if raiz:
        inorder(raiz.esq)
        lista.append(raiz.dado)
        inorder(raiz.dir)
    else:
        lista.append(0)

def constituiArvoreBinariaDeBusca(raiz):
    global lista
    global deuRuim
    
    inorder(raiz)
    listaOrdenada = lista[:]
    listaOrdenadaReverse = lista[:]
    listaOrdenada.sort()
    listaOrdenadaReverse.sort(reverse=True)

    print(lista)
    
    if lista == listaOrdenada or lista == listaOrdenadaReverse:
        lista = []
        return True
    else:
        lista = []
        return False

raiz = ArvoreBinaria(2, ArvoreBinaria(3), None)
print(constituiArvoreBinariaDeBusca(raiz))

raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))
    
raiz = ArvoreBinaria(31, ArvoreBinaria(30, ArvoreBinaria(13, ArvoreBinaria(4, None, None), ArvoreBinaria(18, None, None)), None), None)
print(constituiArvoreBinariaDeBusca(raiz))

raiz = ArvoreBinaria(10, ArvoreBinaria(8), ArvoreBinaria(28, ArvoreBinaria(26), ArvoreBinaria(30)))
print(constituiArvoreBinariaDeBusca(raiz))
