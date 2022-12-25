from itertools import *
from copy import copy
# from more-itertools import *

def converteStr(str):
    listaNumeros = []
    numero = ''
    for i in str:
        if i != ' ':
            numero += i
        else:
            listaNumeros.append(int(numero))
            numero = ''
    listaNumeros.append(int(numero))
    return listaNumeros

# def definePossibilidades(quantidadeNum):
#     lista = []
#     for i in range(int(quantidadeNum/2)):
#         lista.append(0)
#         lista.append(1)
#     return lista

def definePossibilidades(quantidadeNum):
    dicio = dict()
    dicio[1] = int(quantidadeNum/2)
    dicio[0] = int(quantidadeNum/2)
    # print(dicio)
    return dicio


# def definePermutacoes(lista):
#     permutacoes = set(permutations(lista))
#     permutacoes_lista = []
#     for i in permutacoes:
#         print(i)
#         # permutacoes_lista.append(list(i))
#     return permutacoes_lista

# def definePermutacoes(x, curr_list=[]):
#     if not x:
#         yield curr_list
#         return
#     last_item = None
#     if curr_list:
#         last_item = curr_list[-1]
#     for item in x:
#         if item != last_item:
#             for j in range(1, x[item] + 1):
#                 xchild = copy(x)
#                 xchild[item] -= j
#                 if xchild[item] == 0:
#                     del xchild[item]
#                 for y in definePermutacoes(xchild, curr_list + [item] * j):
#                     yield y

def definePermutacoes(unsZeros, listaAtual=[]):
    global listona
    ultimo = None

    if unsZeros == {}:
        return listaAtual

    elif len(listaAtual) > 0:
        ultimo = listaAtual[-1]

    for item in unsZeros:
        if item != ultimo:
            for j in range(1, unsZeros[item] + 1):
                copiaDicio = dict(unsZeros)
                copiaDicio[item] -= j
                if copiaDicio[item] == 0:
                    copiaDicio.pop(item)
                elementos = definePermutacoes(copiaDicio, listaAtual + [item] * j)
                if elementos != None:
                    listona.append(elementos)

def montaPossibilidades(permutacoes,numeros,quantidadeNum):
    maiorSoma = 0
    for i in range(len(permutacoes)):
        soma = 0
        copiaNumeros = numeros[:]
        for j in range(quantidadeNum):
            if permutacoes[i][j] == 1:
                soma+=numeros[j]
        if soma > maiorSoma:
            maiorSoma = soma   
    print(maiorSoma)
    
def recebeDados():
    quantidadeNum = int(input())
    numeros = converteStr(str(input()))
    return numeros,quantidadeNum

def inicio():
    global listona
    listona = []

    numeros,quantidadeNum = recebeDados()
    definePermutacoes(definePossibilidades(quantidadeNum))
    permutacoes = listona
    montaPossibilidades(permutacoes,numeros,quantidadeNum)

inicio()

# print(definePermutacoes([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))

# def permutationsA(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     for indices in product(range(n), repeat=r):
#         if len(set(indices)) == r:
#             yield tuple(pool[i] for i in indices)

# permutacoes = set(permutationsA([1,1,1,1,0,0,0,0]))

# len = 0
# for i in permutacoes:
#     len +=1
#     print(i)
# print(len)


# l = [1,2,3,4]
#l[0] + soma(l[:_])
# reotornar zero no caso base

