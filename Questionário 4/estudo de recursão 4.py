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

def recebeDados():
    quantidadeNum = int(input())
    numeros = converteStr(str(input()))
    return numeros,quantidadeNum

def criaMatriz(quantidadeNum):
    matriz = []
    elemento = [None]*quantidadeNum
    for i in range(quantidadeNum):
        matriz.append(elemento)
    return matriz

def comparaMelhor(escolheCauda,escolheCabeca):
    melhor = escolheCauda
    if escolheCabeca > escolheCauda:
        melhor = escolheCabeca
    return melhor
            

def jogoRec(indexCabeca,indexCauda,acao):
    global memoria    
    global numeros
    # print(memoria)

    if indexCabeca == indexCauda:
        return 0

    if memoria[indexCabeca][indexCauda] != None:
       return memoria[indexCabeca][indexCauda]    

    if acao == 'P': #incluir algum numero na soma
        escolheCabeca = numeros[indexCabeca] + jogoRec(indexCabeca+1,indexCauda,'D')
        escolheCauda = numeros[indexCauda] + jogoRec(indexCabeca,indexCauda-1,'D')

    elif acao == 'D':
        escolheCabeca = jogoRec(indexCabeca+1,indexCauda,'P')
        escolheCauda = jogoRec(indexCabeca,indexCauda-1,'P')
        
    melhor = comparaMelhor(escolheCauda,escolheCabeca)
    memoria[indexCabeca][indexCauda] = melhor
    
    return melhor

def inicioMeu():
    global memoria
    global numeros

    #numeros,quantidadeNum = recebeDados()
    numeros,quantidadeNum = [2,2,5,9,3,8],6
    memoria = criaMatriz(quantidadeNum)
    # print(memoria)
    print(jogoRec(0,quantidadeNum-1,'P'))



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

def inicioGrazi():
    #N = int(input())
    #cartas = list(map(int, input().split()))
    N = 6
    cartas = [2,2,5,9,3,8]
    resposta = sabacchard(cartas, N)
    print(resposta)



inicioGrazi()

