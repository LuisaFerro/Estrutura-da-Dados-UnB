# POO - criando classes

#Bolinha vermelha do vs code faz com que a aplicação role até esse ponto escolhifo

class numeroComplexo: # instanciando a classe, ou seja, definindo-a

    def __init__(self,r,i): #metodo construtor, cujos atributos vêm depois de self, ou seja, são os parâmetros que passaremos ao chamar ao instanciar o objeto
        #o primeiro parâmetro representa o próprio objeto que ta sendo criado
        
        self.real = r
        self.imaginario = i

        #em ambas linhas acima define os atributos do objeto

    def get_imaginario(self):
        return self.imaginario

    def multiplica_por(self,n):
        r = self.real*n.real - self.imaginario*n.imaginario
        i = self.real*n.imaginario

    def __str__(self):
        return f'{self.real}{self.imaginario:+}j' #em :+, indica que quer sempre mostrar o sinal do número

i = numeroComplexo(0,-1)
print(numeroComplexo.get_imaginario())
print(numeroComplexo.__str__)