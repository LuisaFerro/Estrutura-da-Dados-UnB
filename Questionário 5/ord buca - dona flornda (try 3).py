from math import *

def recebeDados():
    quantidade = int(input())
    informacoes = []
    sublistOrdenada = [0,0,0,0]

    for i in range(quantidade):
        sublist = input().split()
        sublist[2], sublist[3] = int(sublist[2]),int(sublist[3])
        
        peso = fabs(sublist[3]-75)
        if sublist[-1] > 75:
             peso *= 1000

        sublistOrdenada[0],sublistOrdenada[1],sublistOrdenada[2],sublistOrdenada[3] = fabs(sublist[2]-180),peso,sublist[1],sublist[0]

        informacoes.append(sublistOrdenada)
        sublistOrdenada = [0,0,0,0]

    return informacoes
    
def inicio():
    info = recebeDados()   
    info.sort()
    for i in info:
        print(f'{i[2]}, {i[3]}')

inicio()

























