from math import *

# def recebeDados():
#     entrada = input()
#     elementos = []
#     elementoAux = ''
#     for i in entrada:
#         # print(i)
#         if i != " " and i != ":":
#             elementoAux += i
#         else:
#             elementos.append(elementoAux)
#             elementoAux = ''
#     elementos.append(elementoAux)
#     for i in range(len(elementos)):
#         elementos[i] = int(elementos[i])
#     # print(elementos)
#     return elementos
    

# def comparaData(comeco,fim):
#     resultado = []
#     contagemTempo = [0,24,60,60]

#     if fim[0] >= comeco[0]:
#         if fim[1] >= comeco[1]:
#             resultado.append(fim[0]-comeco[0])
#         else:
#             resultado.append(fim[0]-comeco[0] - 1)
#         for i in range(1,4):
#             diferenca = int(fabs(fim[i]-comeco[i]))
#             if fim[i] >= comeco[i]:
#                 resultado.append(diferenca)
#             else:
#                 resultado.append(contagemTempo[i]-diferenca)
        
#         if fabs(fim[-1]-comeco[-1]) > 0:
#             # print('entrou aq')
#             resultado[1] = resultado[1] - 1
#             resultado[2] = resultado[2] - 1

#         return resultado
#         # print(resultado)
#     else:
#         # print('Data inválida! 1')
#         # print(resultado)
#         return resultado


# def inicio():
#     nomes = ['dia(s)','hora(s)','minuto(s)','segundo(s)']
#     comeco = list(recebeDados())
#     fim = list(recebeDados())
#     duracao = comparaData(comeco,fim)
#     duracaoStr = str(duracao)

#     # print(duracao)
#     # print(type(duracao))
    
#     if duracaoStr.count('0') == 4 or len(duracao) == 0:
#         print('Data inválida!')
#     else:
#         for i in range(4):
#             print(duracao[i],nomes[i])

# inicio()
# ---------------------------------------------------

def descobreValido(diferenca):    
    valido = True
    diferencaBool = []
    diferencaSoBool = []
    zeros = 0

    for i in diferenca:
        if i == 0:
            diferencaBool.append(0)
            diferencaSoBool.append(True)
            zeros += 1
        if i > 0:
            diferencaBool.append(True)
            diferencaSoBool.append(True)
        if i < 0:
            diferencaBool.append(False)
            diferencaSoBool.append(False)
    
    # print(diferencaBool)
    # print(diferencaSoBool)

    for i in range(4):
        resultado = 0

        if diferencaSoBool[i] != True:
            for j in diferencaBool[:i+1]:
                resultado = resultado or j
                # print('entrei aq')
                # print(j, resultado)

            if resultado == False:
                valido = False

                # print('invalidooo')

    if zeros == 4:
        valido = False
    
    # print(valido)
    return valido

def converteDias(diferenca):
    dias = [60,60,24,0]
    diferenca.reverse()
    for i in range(4):
        if diferenca[i] < 0 and i != 3:
            diferenca[i] = dias[i] + diferenca[i]
            diferenca[i+1] = diferenca[i+1] - 1
    
    diferenca.reverse()

    return diferenca
        
def printResposta(diferenca):
    respostas = ['dia(s)','hora(s)','minuto(s)','segundo(s)']
    for i in range(4):
        print(diferenca[i],respostas[i])


def comparaData(comeco, fim):
    diferenca = []
    for i in range(4):
        diferenca.append(fim[i]-comeco[i])
    
    # print(diferenca)

    if descobreValido(diferenca):
        diferenca = converteDias(diferenca)
        # print(diferenca)
        printResposta(diferenca)
    else:
        print('Data inválida!')


# descobreValido([0,0,0,-1])

def recebeDados():
    entrada = input()
    elementos = []
    elementoAux = ''
    for i in entrada:
        # print(i)
        if i != " " and i != ":":
            elementoAux += i
        else:
            elementos.append(elementoAux)
            elementoAux = ''
    elementos.append(elementoAux)
    for i in range(len(elementos)):
        elementos[i] = int(elementos[i])
    # print(elementos)
    return elementos


def inicio():
    comeco = list(recebeDados())
    fim = list(recebeDados())
    comparaData(comeco,fim)

inicio()

# a= [5,10,0,0]
# b =[5,10,0,1]

# a = [5, 8, 12, 23]
# b = [9, 6, 13, 23]

# e = [8,8,53,12]
# f = [7,8,58,14]
	
# 2 08:05:59
# 10 07:04:58

# 5 08:12:23
# 9 06:13:23


# c = [1,2,2,2]
# d = [2,2,2,2]

# comparaData(a,b)
# comparaData(c,d)
# comparaData(e,f)