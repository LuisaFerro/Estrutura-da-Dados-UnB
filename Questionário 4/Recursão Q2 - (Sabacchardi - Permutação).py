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

def definePossibilidades(quantidadeNum):
    dicio = dict()
    dicio[1] = int(quantidadeNum/2)
    dicio[0] = int(quantidadeNum/2)
    # print(dicio)
    return dicio

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
