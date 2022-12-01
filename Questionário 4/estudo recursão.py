def fatorial(n):
    if n == 0: #caso base
        return 1
    else:
        return n*fatorial(n-1)

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0]+soma(lista[1:])

#------------------------- Lista [simplesmente] Encadeada! ----------------------
#lista circular: retorna ao primeiro, mas como saber quem é o primeiro?
#lista duplamente encadeada: como implementar?

#> inserir no começo, meio ou final OU recursivamente sempre inserir no começo, considerando listas menores

class Item():
    def __init__(self,dado, prox=None): #se for o último elemento, já sabe-se que o próximo é NONE
        self.dado = dado
        self.prox = prox


def insere_inicio(lista,item):# não precisa de self pois não é um método da classe
    if lista != None: #quando é None,return False
        item.prox = lista #aqui define-se o novo primeiro elemento; assim fica atribuido ao parametro "prox" de joao -> paulo (que já estava na estrutura anteriormente)
    return item #retorna o endereço do último item adicionado, a nova cabeça

def insere(lista,item,pos):
    if pos == 0: 
        return insere_inicio(lista,item)
    
    if lista:
        lista.prox = insere(lista.prox,item,pos-1)
        return lista
    
    raise ValueError('Posição inválida') #pois o código funciona caso coloque um valor de append válido. Se não, dará erro

def len_lista(lista):
    if lista:
        return 1 + len(lista(lista.prox))
    return 0    

# item = Item(1)
# item2 = Item(2,item)

lista = None 
#lista não é uma estrutura [], mas um objeto que liga objetos da classe item() e armazena  a memória dos últimos ítens adicionados

lista = insere_inicio(lista,Item('Paulo'))
lista = insere_inicio(lista,Item('Joao')) #insere_lista deve retornar a cabeça da lista para que o próximo elemento adicionado possa se basear na atual cabeça como elemento qu aponta

lista = insere(lista,Item('Caetano'),0)

lista = insere(lista,Item('Caetano'),30)

print('oi')



