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

    if indexCabeca == indexCauda:
        return 0

    if memoria[indexCabeca][indexCauda] != None:
        print(memoria)
        return memoria[indexCabeca][indexCauda]

    if acao == 'P': #incluir algum numero na soma
        escolheCabeca = numeros[indexCabeca] + jogoRec(indexCabeca+1,indexCauda,'D')
        escolheCauda = numeros[indexCauda] + jogoRec(indexCabeca,indexCauda-1,'D')

    else:
    # elif acao == 'D':
        escolheCabeca = jogoRec(indexCabeca+1,indexCauda,'P')
        escolheCauda = jogoRec(indexCabeca,indexCauda-1,'P')
        
    melhor = comparaMelhor(escolheCauda,escolheCabeca)
    memoria[indexCabeca][indexCauda] = melhor
    
    return melhor
    

def inicio():
    global memoria
    global numeros

    numeros,quantidadeNum = recebeDados()
    memoria = criaMatriz(quantidadeNum)
    # print(memoria)
    print(jogoRec(0,quantidadeNum-1,'P'))

inicio()

    
