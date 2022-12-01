class Pilha:
    def __init__(self,pilha_recebida):
        self.pilha = pilha_recebida
    
    def add():
        pass

    def retira():
        pass

def recebeDados():
    pesos = []
    pesoEmpilhado = int(input())

    while pesoEmpilhado != 0:
        pesos.append(pesoEmpilhado)
        pesoEmpilhado = int(input())
    pesoRetirar = int(input())
    return pesos,pesoRetirar

def desempilha(pesos,pesoRetirar):
    pesos.reverse()
    soma = 0
    quantidadePesos =  0

    if pesos == []:
        print(f'Peso retirado: 0')
        print(f'Anilhas retiradas: 0')
        print(f'Peso total movimentado: 0')

    else:
        # print(pesos)
        for i in range(len(pesos)):
            print(f'Peso retirado: {pesos[i]}')
            soma += pesos[i]
            quantidadePesos = i

            if pesoRetirar == pesos[i]:
                break

    
        print(f'Anilhas retiradas: {quantidadePesos+1}')
        print(f'Peso total movimentado: {soma}')

def inicio():
    pesos,pesoRetirar = recebeDados()
    desempilha(pesos,pesoRetirar)

inicio()

    

    
            

            
