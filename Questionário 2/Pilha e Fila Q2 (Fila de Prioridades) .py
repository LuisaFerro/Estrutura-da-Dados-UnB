class Fila:
    def __init__(self,activity,priority):
        self.atividade = activity
        self.prioridade = priority

    def add(self):
        pass

    def remove(self):
        pass

    def __str__(self):
        return f'Atividade: {self.atividade}, Prioridade: #{self.prioridade}'

def converteInteiros(lista):
    for i in range(len(lista)):
        if i % 2 != 0:
            lista[i] = int(lista[i])
    return lista

def getDados():
    dados = input()
    atividades = []
    palavra = ''
    for i in dados:
        if i == ' ':
            atividades.append(palavra)
            palavra = ''
        else:
            palavra += i
    atividades.append(palavra)
    numAtividades = int(input())
    atividades = converteInteiros(atividades)

    return atividades,numAtividades

def ordenaLista(lista):
    prioridades = []
    atividades = []
    prioridOrdenado = []
    atvOrdenado = []
    
    for i in lista:
        if type(i) == int:
            # print(i)
            prioridades.append(i)
            prioridOrdenado.append(i)        
        else:
            atividades.append(i)
    prioridOrdenado.sort()    
    for i in prioridOrdenado:
        index = prioridades.index(i)
        atvOrdenado.append(atividades[index])

        prioridades.pop(index)
        atividades.pop(index)

    return prioridOrdenado,atvOrdenado

def tiraElementos(atividades,prioridades,numAtividades):
    tamanhoFila = 0

    if len(atividades) > numAtividades:
        tamanhoFila = len(atividades) - numAtividades
        del atividades[:numAtividades]
        del prioridades[:numAtividades]
    else:
        prioridades = []
        atividades = []    
    print(f'Tamanho da fila: {tamanhoFila}')
    return prioridades,atividades


def imprimeTela(atividades,prioridades):
    if atividades != []:
        for i in range(len(atividades)):
            print(f'Atividade: {atividades[i]}, Prioridade: #{prioridades[i]}')

def inicio():
    atividades,numAtividades = getDados()
    prioridades,atividades = ordenaLista(atividades)
    prioridades,atividades = tiraElementos(atividades,prioridades,numAtividades)
    imprimeTela(atividades,prioridades)

inicio()

     




