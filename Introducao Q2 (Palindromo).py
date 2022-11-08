def ehPar(palavra):
    if len(palavra)%2 == 0:
        return True
    else:
        return False


def ehPalindromo(comeco,fim):
    ehPalindromo = True
    for i in range(len(comeco)):
        if comeco[i] != fim[i]:
            ehPalindromo =  False

    return ehPalindromo

def compara(comeco,fim):
    comecoAux = comeco[:]
    fimAux = fim[:]
    rola = False


    for i in range(len(comeco)):
        if comeco[i] != fim[i]:
            comecoAux = comeco[:i] + fim[i] + comeco[i + 1:]
            if ehPalindromo(comecoAux,fim):
                rola = True
                break
    return rola

def inicio():
    palavra = input()
    
    metade = int(len(palavra)/2)
    comeco = palavra[:metade]
    if not ehPar(palavra):
        metade+=1
    fim = palavra[metade:]
    fim = fim[::-1]

    if ehPalindromo(comeco,fim) and not ehPar(palavra):
        rola = True
    else:
        rola = compara(comeco,fim)

    if rola:
        print('POSSÍVEL')
    else:
        print('IMPOSSÍVEL')


inicio()
# print(ehPalindromo('bna','ana'))
