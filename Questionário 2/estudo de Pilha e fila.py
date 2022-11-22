class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def printar(self):
        return self.items

# pilha = Stack()
# pilha.push(1)
# pilha.push(2)
# pilha.push(7)

# print(pilha.printar())
# print(pilha.peek())

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def printar(self):
        return self.items

# fila = Queue()
# fila.enqueue(7)
# fila.enqueue(12)
# print(fila.printar())



#---------------POO--------------------

class Fracao:
    # We need to be able to add, subtract, multiply, and divide fractions.

    def __init__(self,num,den):
        self.numerador = num #aqui eu defino que, para acessar o parâmetro "num" que é passado, eu defino que sua chamada se dá por self.numerador
        self.denominador = den

    def __str__(self) -> str:
        return str(self.numerador) + '/' + str(self.denominador)

    def soma(self,frac1,frac2):
        pass
numero = Fracao(1,2)
print(numero )

