from math import *

# Ordem de importancia = altur > peso > sobrenome > nome
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
    print(informacoes)
    return nomes,sobrenomes,alturas,pesos,informacoes,quantidade


def ordenaDiferencas(lista,goal):
    diferencas = []
    listaOrd = []

    for i in lista:
        diferencas.append(fabs(i-goal))
    diferencasOrd = diferencas[:]
    diferencasOrd.sort()

    return diferencas,diferencasOrd

def ordenaAlturas(informacoes,alturas):
    novasInfo = []
    sublista = []

    diferencas,diferencasOrd = ordenaDiferencas(alturas,goal=180)
    setDiferencas = set(diferencasOrd)
    
    for i in setDiferencas:
        while i in diferencas:
            index = diferencas.index(i)
            sublista.append(informacoes[index])

            diferencas.pop(index)
            informacoes.pop(index)

        novasInfo.append(sublista)
        sublista = []        

    return novasInfo

# print(ordenaAlturas([['Guido', 'Batista', 195, 110], ['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Rafael', 'Rodrigues', 165, 110], ['Ricardo', 'Neto', 170, 70], ['Juca', 'Carvalho', 180, 77]],[195,180,180,180,165,170,180]))

def ordenaPesoAntigo(informacoes):#pesos):
    novasInfo = []
    sublistNovasInfo = []
    # pesos = []
    # sublistPesos = []
    sublistDifPesos = []
    difPesos = []
    difPesosOrd = []

    for i in informacoes: #anda pelos grupos de alturas
        for j in i: #anda pelo grupo de alturas iguais
            # sublistPesos.append(j[3])
            sublistDifPesos.append(fabs(j[3]-75))
        # pesos.append(sublistPesos)
        difPesos.append(sublistDifPesos)
        sublistDifPesos.sort()
        difPesosOrd.append(sublistDifPesos)
        # sublistPesos = []
        sublistDifPesos = []

    for i in difPesosOrd:
        for j in i:
            index = difPesos[i].index(j)
            difPesos[i][j].pop()
            # sublistNovasInfo.append(informacoes[][index])
            

    # print(difPesosOrd)
    # setDifPesosOrd = set(difPesosOrd)
    # print(setDifPesosOrd)
    # for i in setDifPesosOrd:
    #     while i in difPesos:
    #         difPesos.
  
    # print(pesos,difPesos,difPesosOrd)

# ordenaPeso([[['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Juca', 'Carvalho', 180, 77]], [['Ricardo', 'Neto', 170, 70]], [['Guido', 'Batista', 195, 110], ['Rafael', 'Rodrigues', 165, 110]]])



def ordenaDiferencas(lista,goal):
    diferencas = []
    listaOrd = []

    for i in lista:
        diferencas.append(fabs(i-goal))
    diferencasOrd = diferencas[:]
    diferencasOrd.sort()

    return diferencas,diferencasOrd

def ordenaAlturas(informacoes,alturas):
    novasInfo = []
    sublista = []

    diferencas,diferencasOrd = ordenaDiferencas(alturas,goal=180)
    setDiferencas = set(diferencasOrd)
    
    for i in setDiferencas:
        while i in diferencas:
            index = diferencas.index(i)
            sublista.append(informacoes[index])

            diferencas.pop(index)
            informacoes.pop(index)

        novasInfo.append(sublista)
        sublista = []        

    return novasInfo

# print(ordenaAlturas([['Guido', 'Batista', 195, 110], ['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Rafael', 'Rodrigues', 165, 110], ['Ricardo', 'Neto', 170, 70], ['Juca', 'Carvalho', 180, 77]],[195,180,180,180,165,170,180]))
# for i in ordenaAlturas([['Guido', 'Batista', 195, 110], ['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Rafael', 'Rodrigues', 165, 110], ['Ricardo', 'Neto', 170, 70], ['Juca', 'Carvalho', 180, 77]],[195,180,180,180,165,170,180]):
#     print(i)      

def ordenaPesos(informacoes):
    pesos = []
    difPesosOrd = []
    difPesos = []
    novasInfo = []

    for i in range(len(informacoes)):
        pesoAux = []
        for j in range(len(informacoes[i])):
            pesoAux.append(informacoes[i][j][3])
        pesos.append(pesoAux)
        pesoAux = []
    
    for i in pesos:
        diferencas,diferencasOrd =ordenaDiferencas(i,75)
        difPesos.append(diferencas)
        difPesosOrd.append(set(diferencasOrd))
    
    # print(difPesosOrd)
    # print(difPesos)

    listaInterna = []
    listaExterna = []
    novasInfo= []

    numMsmAltura = len(difPesosOrd)
    for i in range(numMsmAltura):
        for j in difPesosOrd[i]:
            while j in difPesos[i]:
                indexElemento = difPesos[i].index(j)
                listaInterna.append(informacoes[i][indexElemento])
                
                difPesos[i].pop(indexElemento)
                informacoes[i].pop(indexElemento)
                
            listaExterna.append(listaInterna)
            listaInterna = []
        novasInfo.append(listaExterna)
        listaExterna = []

    return novasInfo
        
# [{0.0, 2.0, 10.0}, {5.0}, {35.0}] 
# [[0.0, 0.0, 10.0, 2.0], [5.0], [35.0, 35.0]]
# print(ordenaPesos([[['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75], ['Joao', 'Kleber', 180, 65], ['Juca', 'Carvalho', 180, 77]], [['Ricardo', 'Neto', 170, 70]], [['Guido', 'Batista', 195, 110], ['Rafael', 'Rodrigues', 165, 110]]]))

def ordenaSobrenome(informacoes):
    sobreNom = []
    difSobreNomOrd = []
    difSobreNom = []
    novasInfo = []

    for i in range(len(informacoes)):
        for j in range(len(informacoes[i])):
            print(informacoes[i][j])

sobreNom = []
difSobreNomOrd = []
difSobreNom = []
novasInfo = []
informacoes = [[[['Heitor', 'Tostes', 180, 75], ['Bruno', 'Costa', 180, 75]], [['Juca', 'Carvalho', 180, 77]], [['Joao', 'Kleber', 180, 65]]], [[['Ricardo', 'Neto', 170, 70]]], [[['Guido', 'Batista', 195, 110], ['Rafael', 'Rodrigues', 165, 110]]]]

for i in range(len(informacoes)):
    for j in range(len(informacoes[i])):
        for k in informacoes[i][j]:
            print(k)


        