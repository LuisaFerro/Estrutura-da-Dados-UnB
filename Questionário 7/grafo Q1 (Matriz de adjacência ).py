def geraMatriz(vertices):
    matriz = []
    for i in range(vertices):
        matriz.append([0]*vertices)
    return matriz

def montaMatriz(matriz,arestas,tipo):
    contador = 0
    while contador < arestas:
        coluna,linha,peso = input().split()
        coluna,linha,peso = int(coluna)-1,int(linha)-1,int(peso)
        if tipo == 'N':
            matriz[linha][coluna] = peso
        matriz[coluna][linha] = peso
        # print(matriz)

        contador += 1
    return matriz

def recebeDados():
    vertices,arestas,tipo= input().split()
    vertices,arestas = int(vertices),int(arestas)
    matriz = geraMatriz(vertices)
    matriz = montaMatriz(matriz,arestas,tipo)

    return matriz

def printa(matriz):
    for i in matriz:
        linha = ''
        for j in i:
            espaco = (4-len(str(j)))*' '
            linha += espaco + str(j)
        print(linha)

def inicio():
    matriz = recebeDados()
    printa(matriz)

inicio()

# printa([[0, 4, 0], [3, 0, 2], [4, 1, 0]])

