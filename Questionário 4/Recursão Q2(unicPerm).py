x = {1:30,0:30} #o da esquerda é a chave e o da direita é a quantidade de repetições


def permutations_unique(unsZeros, listaAtual=[],resultados=[]):
    if len(unsZeros) == {}:
        yield listaAtual
        return
    ultimo = None
    if len(listaAtual) > 0:
        ultimo = listaAtual[-1]
    for item in x:
        if item != ultimo:
            for j in range(1, x[item] + 1):
                xchild = dict(unsZeros)
                xchild[item] -= j
                if xchild[item] == 0:
                    del xchild[item]
                for y in permutations_unique(xchild, listaAtual + [item] * j):
                    yield y

# a = permutations_unique(x)
# for i in a:
#     print(i)

# unsZeros = {1:5,0:5}:

# def var():
#     global listona
#     listona = []

# def permutations_unique(unsZeros, listaAtual=[]):
#     global listona
#     ultimo = None

#     if unsZeros == {}:
#         yield listaAtual
#         return

#     elif len(listaAtual) > 0:
#         ultimo = listaAtual[-1]

#     for item in unsZeros:
#         if item != ultimo:
#             for j in range(1, unsZeros[item] + 1):
#                 copiaDicio = dict(unsZeros)
#                 copiaDicio[item] -= j
#                 if copiaDicio[item] == 0:
#                     copiaDicio.pop(item)
#                 elementos = permutations_unique(copiaDicio, listaAtual + [item] * j)
#                 for y in elementos:
#                 # if elementos != None:
#                 #     listona.append(elementos)
#                     yield y
#                 # lista = permutations_unique(xchild, listaAtual + [item] * j)
#                 # for y in lista:
#                 #     print('y',y)
#                 #     listona.append(y)


def sabacchard(L, n):
    # Tabela de programação dinâmica, 
    # para salvar os resultados já calculados
    pd = [[None] * n for i in range(n)]
    
    def solucao(ini, fim, tipo):
        # Se as posições forem iguais, o baralho está vazio
        if ini == fim:
            return 0
        
        # Se a matriz de programação dinâmica nessas posições, 
        # forem diferentes de None, então o valor já foi calculado
        # e pode ser retornado
        if pd[ini][fim] != None:
            return pd[ini][fim]
 # Se tipo for igual a 1, a escolha é para pontuar
        if tipo == 1:
            # Pontuação escolhendo a extremidade esquerda
            # desloca-se ini para a direita
            r1 = L[ini] + solucao(ini + 1, fim    , 0)
            
            # Pontuação escolhendo a extremidade esquerda,
            # desloca-se fim para a esquerda
            r2 = L[fim] + solucao(ini    , fim - 1, 0)
        
        # Se tipo for igual a 0, a escolha é para descartar
        else:
            r1 = solucao(ini + 1, fim    , 1)
            r2 = solucao(ini    , fim - 1, 1)
        
        # A melhor opção é inserida na tabela e retornada
        if r1 > r2:
            pd[ini][fim] = r1
            return r1
        else:
            pd[ini][fim] = r2
            return r2
    # Chama a função recursiva, passando:
    # 1 - Posição do início da lista
    # 2 - Posição do fim da lista
    # 3 - 1 para indicar que irá pontuar ou 0 para indicar que irá descartar
    return solucao(0, n - 1, 1)

# N = int(input())
# cartas = list(map(int, input().split()))
# resposta = sabacchard(cartas, N)
# print(resposta)