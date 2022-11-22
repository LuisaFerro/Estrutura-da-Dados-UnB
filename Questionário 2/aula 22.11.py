from pythonds.basic import *

# Dica: Criação de maquinas virtuais pra instalar bibliotecas locais, 'venv'
# pra n deixar o pc smp cheio de lixo
#https://docs.python.org/3/library/venv.html
#https://github.com/mfcaetano/pydash

class Pessoa: #definição de um novo tipo
    def __init__(self,prioridade,idade): #construtor da classe // o que é isso de fato?
        self.prioridade = prioridade #quanto maior o numero, maior prioridade
        self.idade = idade

    def __repr__(self) -> str: #refiz o módulo já existente de print da classe(?)
        return str(self.prioridade) +' ' + str(self.idade) #f"Pessoa com {self.idade} anos de idade e com prioridade {self.prioridade}"

class Fila_Prioridade:
    def __init__(self) -> None:
        self.geral = [Queue(),Queue(),Queue()] #fila geral, com 3 filas dentro

    def enfileirar(self,item): #pq tem hora que voce chama o self e hora que não?
        if item.prioridade == 0: #não precisa passar "prioridade" no parâmetro pois o "ítem" é necessariamente da classe "Pessoa"
            self.geral[2].enqueue(item)

        else:
            if item.idade >= 80: #self.geral[1].enqueue(item)
                self.geral[0].enqueue(item)
            else:
                self.geral[1].enqueue(item)
    
    def desenfileirar(self):
        for queue in self.geral:
            if queue.size():
                queue.dequeue()

    def __str__(self) -> str:
        resp = str(self.geral[0]) + ' e ' + str(self.geral[1]) + ' e ' + str(self.geral[2])
        return resp

#proposta: reescrever de forma arcaica, sem a biblioteca

fila = Fila_Prioridade()
fila.enfileirar(Pessoa(0,22))
fila.enfileirar(Pessoa(1,85))
fila.enfileirar(Pessoa(1,22))
fila.enfileirar(Pessoa(2,10))

print(fila)


#pra eu printar algo que puxa um objeto de outra classe, preciso definir como um método a 
# forma que essa classe inicial pode ser printada !!

