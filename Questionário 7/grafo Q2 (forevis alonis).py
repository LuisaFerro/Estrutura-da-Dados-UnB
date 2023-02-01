def recebedados():
    matriz = []
    numVertices = int(input())

    for i in range(numVertices):
        elementos = input().split()

        elemento_atual = int(elementos.pop(0))
        conexoes = []
        conexoes.append(elemento_atual)
        subconexoes = []

        for i in elementos:
            subconexoes.append(int(i))
        
        conexoes.append(subconexoes)
        matriz.append(conexoes)

    meuID,mussumID = input().split()
    meuID,mussumID = int(meuID),int(mussumID)

    print(matriz)
    print(meuID)
    print(mussumID)

recebedados()