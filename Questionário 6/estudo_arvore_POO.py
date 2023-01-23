#valores menores à esquerda e maiores à direita, smp p baixo

class ArvoreBinariaBusca: 
    def __init__(self,dado,esq =None,dir=None):
        self.dado= dado
        self.esq = esq
        self.dir = dir
    
    def altura(self):
        h_esq = 0 if self.esq is None else self.esq.altura()
        h_dir = 0 if self.dir is None else self.dir.altura()
        
        return 1+max(h_esq,h_dir)

def insere(raiz,no): #sendo raíz o primeiro elemento da ávore
    if not raiz:
        return no

    if no.dado < raiz.dado:
        raiz.esq = insere(raiz.esq,no)
    else:
        raiz.dir = insere(raiz.dir,no)
    
    return raiz

def preorder(raiz):
    if raiz:
        print(raiz.dado)
        preorder(raiz.esq)
        preorder(raiz.dir)

def inorder(raiz):
    if raiz:
        inorder(raiz.esq)
        print(raiz.dado)
        inorder(raiz.dir)

def posorder(raiz):
    if raiz:
        posorder(raiz.esq)
        posorder(raiz.dir)
        print(raiz.dado)

raiz = ArvoreBinariaBusca(50)

raiz = insere(raiz,ArvoreBinariaBusca(17))
raiz = insere(raiz,ArvoreBinariaBusca(72))
raiz = insere(raiz,ArvoreBinariaBusca(12))
raiz = insere(raiz,ArvoreBinariaBusca(23))

# print(f'altura {raiz.altura()}')

inorder(raiz)

