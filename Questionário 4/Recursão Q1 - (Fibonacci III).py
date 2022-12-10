nesimo_chamado = []

def fibonacci(n):
    global nesimo_chamado
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nesimo_chamado.append(n-1)
        nesimo_chamado.append(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

def printFib(nesimo_chamado,quantidades,resultado,numero):
    print(f'fibonacci({numero}) = {resultado}.')
    for i in range(len(nesimo_chamado)):
        print(f'{quantidades[i]} chamada(s) a fibonacci({nesimo_chamado[i]}).')

def contaFibonacci():
    global nesimo_chamado
    quantidades = []
    contagem = 0

    nesimo_chamado.sort()
    # print(nesimo_chamado)
    
    elemento = nesimo_chamado[0]
    for i in nesimo_chamado:
        if i != elemento:
            elemento = i
            quantidades.append(contagem)
            contagem = 0
        contagem += 1
    quantidades.append(contagem)
    nesimo_chamado = list(set(nesimo_chamado))

    return nesimo_chamado,quantidades
    

def inicio():
    global nesimo_chamado
    numero = int(input())
    nesimo_chamado.append(numero)
    resultado = fibonacci(numero)
    nesimo_chamado,quantidades = contaFibonacci()
    printFib(nesimo_chamado,quantidades,resultado,numero)


inicio()