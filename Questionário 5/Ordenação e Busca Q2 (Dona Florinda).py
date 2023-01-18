from math import *

def recebeDados():
    quantidade = int(input())
    informacoes = []
    alturas = []
    nomes = []
    sobrenomes = []
    pesos = []
    for i in range(quantidade):
        sublist = input().split()
        sublist[2], sublist[3] = int(sublist[2]),int(sublist[3])

        nomes.append(sublist[0])
        sobrenomes.append(sublist[1])
        alturas.append(sublist[2])
        pesos.append(sublist[3])

        informacoes.append(sublist)

    return nomes,sobrenomes,alturas,pesos,informacoes,quantidade

# [0.0, 0.0, 0.0, 0.0, 10.0, 15.0, 15.0]


def ordenaAtributo(atributo,quantidade,goal = 180):
    diferencas = []
    novaOrdem = []

    for i in range(quantidade):
        diferenca = fabs(atributo[i]-goal)
        diferencas.append(diferenca)
    
    diferencasOrd = diferencas[:]
    diferencasOrd.sort()

    for i in diferencasOrd:
        if goal+i in atributo:
            novaOrdem.append(goal+i)
            index = atributo.index(goal+i)
            atributo.pop(index)


        elif goal-i in atributo:
            novaOrdem.append(goal-i)
            index = atributo.index(goal-i)
            atributo.pop(index)

    return novaOrdem,diferencasOrd

# ordenaSoAltura([160, 180,165,170,170],5)


def ordenaPeso(difAltura,pesos,informacoes,quantidade,goal = 75):
    diferencas = []
    novasInfo = []
    # ordemPeso

    primeiro = difAltura[0]
    for i in difAltura:
        if primeiro == i: #repetindo elemento
            diferenca = fabs(informacoes[i][3]-goal)

        for i in diferencasOrd:
            index = diferencas.index(i)
            novasInfo.append(informacoes[index])
            diferencas.pop(index)
            informacoes.pop(index)

    return novasInfo


# def ordem

def ordenaAlturas(informacoes,quantidade,goal = 180):
    diferencas = []
    novasInfo = []
    
    for i in range(quantidade):
        valor = informacoes[i][2]
        diferenca = fabs(valor-goal)
        diferencas.append(diferenca)
    
    diferencasOrd = diferencas[:]
    diferencasOrd.sort()
    # print(diferencasOrd)
    # print(diferencas)

    for i in diferencasOrd:
        index = diferencas.index(i)
        novasInfo.append(informacoes[index])
        # print('index:',index)
        # print('elemento',diferencas[index])
        diferencas.pop(index)
        informacoes.pop(index)
        # print(informacoes)

    return novasInfo,diferencasOrd
# ordenaAlturas([['Guido', 'Batista', 195, 110], ['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Rafael', 'Rodrigues', 165, 110], ['Ricardo', 'Neto', 170, 70], ['Juca', 'Carvalho', 180, 77]],7)


# def desempata(repetidos,criterio): #alturas // 

def ordenaTudo(nomes,sobrenomes,alturas,pesos,informacoes,quantidade):
    
    novaLista = []
    nomes.sort()
    sobrenomes.sort()
    alturas,difAlturas = ordenaAtributo(alturas,quantidade,180)
    pesos,difPesos = ordenaAtributo(pesos,quantidade,75)

    primeiro = difAlturas[0]
    for i in difAlturas:
        if primeiro == i: #elemento repetido



# ordenaTudo(['Guido', 'Heitor', 'Bruno', 'Joao', 'Rafael', 'Ricardo', 'Juca'], ['Batista', 'Tostes', 'Costa', 'Kleber', 'Rodrigues', 'Neto', 'Carvalho'], [195, 180, 180, 180, 165, 170, 180], [110, 75, 75, 65, 110, 70, 77],[['Guido', 'Batista', 195, 110], ['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Rafael', 'Rodrigues', 165, 110], ['Ricardo', 'Neto', 170, 70], ['Juca', 'Carvalho', 180, 77]],7)


#nome sobreNome altura peso
#Prioridades: altura > peso  > sobrenome > nome
# 1,80m > 75kg > alfabetica