""" 
Herança - ideia de herança eh reaproveitar codigo e extender nossas classes

obs: a partir de uma classe existente, nos extendemos outra classe que possa herdar atributos e metodos
da classe herdada

EX:

Cliente:
    -nome
    -sobrenome
    -cpf
    -renda

Funcionario:
    -nome
    -sobrenome
    -cpf
    -matricula
 """
class Pessoa():
    def __init__(self,nome,sobrenome,cpf):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__cpf=cpf

    def NomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):#Cliente herda de pessoa
    def __init__(self,nome,sobrenome,cpf,renda):
        super().__init__(nome,sobrenome,cpf)
        self.__renda=renda

class Funcionario(Pessoa):#Funcionario herda de pessoa
    def __init__(self,nome,sobrenome,cpf,matricula):   
        super().__init__(nome,sobrenome,cpf)
        self.__matricula=matricula
    
    def NomeCompleto(self):
        return f'Funcionarios: {self.__matricula} Nome: {self._Pessoa__nome}'       #Usar 1 _ apenas

cliente1=Cliente('ana','viana','051652165469',4000)
funcionario1=Funcionario('alexandre','brito','07828625510','511615646')
print(cliente1.NomeCompleto()) 
print(funcionario1.NomeCompleto())          