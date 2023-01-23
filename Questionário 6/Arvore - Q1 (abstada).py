lista = ''

class Arvore:
    def __init__(self,valor,dir=None,esq=None):
        self.direita = dir
        self.esquerda = esq
        self.valor = valor


def insere(raiz, novoElemento):
    if not raiz:
        return novoElemento
    if novoElemento.valor < raiz.valor:
        raiz.esquerda = insere(raiz.esquerda,novoElemento)

    if novoElemento.valor > raiz.valor:
        raiz.direita = insere(raiz.direita,novoElemento)
    return raiz

def preorder(raiz):
    global lista

    if raiz:
        lista+= str(raiz.valor) + ' '
        preorder(raiz.esquerda)
        preorder(raiz.direita)

def inorder(raiz):
    global lista

    if raiz:
        inorder(raiz.esquerda)
        lista+= str(raiz.valor) + ' '
        inorder(raiz.direita)

def posorder(raiz):
    global lista

    if raiz:
        posorder(raiz.esquerda)
        posorder(raiz.direita)
        lista+= str(raiz.valor) + ' '


def recebeDados(comandosEscritos):
    comando = input()
    comandos = []

    while comando != "quack":
        if comando not in comandosEscritos:
            comando = int(comando)
            
        comandos.append(comando)
        comando = input()
    
    
    return comandos

def inicio():
    global lista

    comandosEscritos = ['in','pre','pos','quack']
    comandos = recebeDados(comandosEscritos)
    primeiraVez = True
    raiz = 0

    for i in range(len(comandos)):
        if comandos[i] not in comandosEscritos:
            if primeiraVez:
                primeiraVez = False
                raiz = Arvore(comandos[i])
            else:
                insere(raiz, Arvore(comandos[i]))
        else:
            if raiz != 0:    
                if comandos[i] == 'in':
                    inorder(raiz)
                    print(lista.strip())
                    lista = ' '

                if comandos[i] == 'pre':
                    preorder(raiz)
                    print(lista.strip())
                    lista = ' '

                if comandos[i] == 'pos':
                    posorder(raiz)
                    print(lista.strip())
                    lista = ' '
            else:
                print()


# inicio()



def teste():
    global lista
    # raiz = Arvore(7,Arvore(4),Arvore(10,Arvore(11),Arvore(15)))
    # raiz = Arvore(10, Arvore(8), Arvore(28, Arvore(26), Arvore(30)))
    # raiz = Arvore(1, Arvore(2), Arvore(3))
    # raiz = Arvore(2, Arvore(3), None)
    # raiz = Arvore(10, Arvore(8), Arvore(28, Arvore(26), Arvore(30)))
    raiz = Arvore(19, Arvore(31, Arvore(3, Arvore(7, None, None), Arvore(29, None, None)), Arvore(10, Arvore(5, None, None), Arvore(14, None, None))), Arvore(9, Arvore(15, Arvore(18, None, None), Arvore(21, None, None)), Arvore(28, Arvore(8, None, None), Arvore(17, None, None))))
    

    preorder(raiz)
    print(lista)

# raiz = Arvore(4)

# raiz = insere(raiz,Arvore(2))
# raiz = insere(raiz,Arvore(1))
# raiz = insere(raiz,Arvore(3))
# raiz = insere(raiz,Arvore(6))
# raiz = insere(raiz,Arvore(7))
# raiz = insere(raiz,Arvore(5))

teste()

        