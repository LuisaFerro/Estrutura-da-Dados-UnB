class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

lista = []
def inorder(raiz):
    global lista

    if raiz:
        inorder(raiz.esq)
        lista.append(raiz.dado)
        inorder(raiz.dir)  
    else:
        lista.append(0) 

def ehPar(palavra):
    if len(palavra)%2 == 0:
        return True
    else:
        return False

def comparaLados(lista):
    meio = int(len(lista)/2)
    comeco = lista[:meio]
    fim = lista[meio+1:]
    fim.reverse()

    ehSimetrico = True
    for i in range(len(comeco)):
        if comeco[i] != fim[i]:
            ehSimetrico =  False

    return ehSimetrico

def verificaSimetria(raiz):
    global lista
    inorder(raiz)
    print(lista)
    ehSimetrico = False

    if len(lista) == 1:
        return True
    
    if not ehPar(lista):
        ehSimetrico = comparaLados(lista)
    
    lista = []
    return ehSimetrico

	
raiz = ArvoreBinaria(0)
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(0, None, None), ArvoreBinaria(1, None, None)))
print(verificaSimetria(raiz))