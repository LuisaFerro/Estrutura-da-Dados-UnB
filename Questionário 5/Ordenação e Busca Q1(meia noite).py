def recebeDados():
    numeroTestes = int(input())
    atividades = []
    atividadesTurnos = []
    for i in range(numeroTestes):
        for j in range(4):
            atividadesTurnos.append(str(input()))
        atividades.append(atividadesTurnos)
        atividadesTurnos = []
    return atividades,numeroTestes

def concatena(lista):
    planejamento = lista.pop(0)
    atividades = ''
    for i in lista:
        atividades+=str(i)
    return atividades,planejamento

def subtraiStrings(atividades,planejamento):
    restoAtividades = ''
    for i in range(len(atividades)): #string enorme com todas as atividades
        if atividades[i] in planejamento:
            index = planejamento.index(atividades[i])
            if index == 0:
                planejamento = planejamento[1:]
            else:
                planejamento = planejamento[:index] + planejamento[index+1:]
        else:
            restoAtividades += atividades[i]

    return restoAtividades, planejamento

def analise(lista):
    atividades,planejamento = concatena(lista) #longa string com as atividades
    atividades,planejamento = subtraiStrings(atividades,planejamento)
    
    if atividades == planejamento == '': # 00
        print("It's in the box!")

    elif atividades == '' and planejamento != '': # 01
        texto = ''
        for i in sorted(set(planejamento)):
            texto += i
        print('Bora ralar:',texto)
    elif atividades != '': #and planejamento == '': # 11
        print("You died!")

def inicio():
    atividades,numeroTestes = recebeDados()
    for i in range(numeroTestes):
        analise(atividades[i])

inicio()
        

        
    
# possibilidades = ['Bora ralar: {conteudo}',   "It's in the box!",'    You died!']
# possilibidades = [Caso realize N-x atividades do planejamento e falte fazer coisa do planejamento ;
                    # Caso se tenha estudado tudo que se tinha pra estudar, GG;
                    # Caso tenham elementos na lista que não constam em planejamento3
