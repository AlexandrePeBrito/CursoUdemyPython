""" 1. Crie uma classe para representar uma pessoa, com os atributos privados de nome
idade e altura. Crie os métodos públicos necessários para sets e gets e também un
método para imprimir os dados de uma pessoa. """

class Pessoa():
    def __init__(self,nome,idade,altura):
        self.__nome=nome
        self.__idade=idade
        self.__altura=altura
    
    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome=nome

    def getIdade(self):
        return self.__idade

    def setIdade(self,idade):
        if idade>0:
            self.__idade=idade
        else:
            print("Idade invalida")
            exit(1)

    def getAltura(self):
        return self.__altura

    def setAltura(self,altura):
        if altura>0 and altura<3:
            self.__altura=altura
        else:
            print("Altura invalida")
            exit(1)

    def dadosPessoa(self):
        print(f"Nome: {self.__nome}\nIdade: {self.__idade}\nAltura: {self.__altura}")

pessoa1=Pessoa('alexandre',28,1.74)
print(pessoa1.getNome())
pessoa1.setNome('Alex')
print(pessoa1.getNome())

pessoa1.dadosPessoa()


