def converteLista(listaStr):
    listaInt = []
    numero = ''
    for i in listaStr:
        if i != ' ':
            numero += i
        else:
            listaInt.append(int(numero))
            numero = ''
    listaInt.append(int(numero))
    return listaInt

def recebeDados():
  quantidadeNum = int(input())
  lista = converteLista(str(input()))
  tamanhoJanela = int(input())
  return lista,tamanhoJanela

def retornaMaior(janela,tamanhoJanela):
  maior = janela[0]
  for i in range(tamanhoJanela):
    if janela[i] > maior:
      maior = janela[i]
  return str(maior) + '  '

def compara(lista,tamanhoJanela):
  janela = []
  numMaiores = ''
  maior = lista[0]
  for i in range(tamanhoJanela):
    janela.append(lista[i])

  del   lista[:tamanhoJanela]
  numMaiores += retornaMaior(janela,tamanhoJanela)

  for i in lista:
    janela.pop(0)
    janela.append(i)
    numMaiores += retornaMaior(janela,tamanhoJanela)
    # numMaiores.append(retornaMaior(janela,tamanhoJanela))

  print(numMaiores.strip())

def inicio():
  lista,tamanhoJanela = recebeDados()
  compara(lista,tamanhoJanela)

inicio()