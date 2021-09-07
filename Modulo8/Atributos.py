""" 
Atributos -> Caracteristicas de objetos. Podemos representar os estados de um objeto

Em python dividimos  os atributos em 3 grupos:
    Atributos de Instancia
    Atributos de Classe
    atributos Dinamicos

"""
#Atributo de Instancia: Atributos declarados dentro do metodo construtor. Sendo obrigatorio
#todos os objetos terem esses atributos

"""
#Metodo private
class Lampada:      
    def __init__(self, voltagem, cor):              #Metodo Construtor __init__
        self.__voltagem=voltagem                    #Os 2 __ significa privte
        self.__cor=cor
#Chamada:
lamp=Lampada(120,'branca')

#OBS: Todo atributo de uma classe eh publico(podendo ser acessado por todo o projeto).
#Para determinar um atributo como privado, utiliza-se o "__"

#Metodo publico

class Usuario:
    def __init__(self, nome, email, senha):              #Metodo Construtor __init__
        self.nome=nome                    
        self.email=email
        self.__senha=senha
    def get_senha(self):                                #metodo para mostrar private
        print(self.__senha)
#Chamada:
user=Usuario('alexandre','user@gmail.com', '1243796')

print(user.nome)
#print(user.__senha)     #ERROR AttributeError
#print(user._Usuario__senha)     #Temos acesso, mas não deveriamos fazer
user.get_senha()                 #Modo correto de fazer chamada do private
"""


#Atributos de Classe    -> atributos inicializados ja na classe, fora do construtor
""" class Lampada:     
    intensidade='intensa'                           #Atributo de Classe
    def __init__(self, voltagem, cor):              
        self.__voltagem=voltagem                    
        self.__cor=cor
#Chamada:
lamp1=Lampada(120,'branca')
lamp2=Lampada(210,'verde')

print(lamp1.intensidade)                #Acesso Errado
print(lamp2.intensidade)                #Acesso Errado

print(Lampada.intensidade)              #Acesso Correto """

#Atributo Dinamico  -> Atributo de instancia que pode ser criado em tempo de execução
#OBS: Atributo Dinamico sera exclusivo da instancia que criou
#OBS: Pouco usual

class Lampada:                                    
    def __init__(self, voltagem, cor):              
        self.__voltagem=voltagem                    
        self.__cor=cor
#Chamada:
lamp1=Lampada(120,'branca')
lamp2=Lampada(210,'verde')

lamp1.intensidade='Forte'               #Atributo Dinamico 
print(lamp1.intensidade)                #Atributo Dinamico 
print(lamp1.__dict__)
del lamp1.intensidade                   #Deletando atributo de forma dinamica
print(lamp1.__dict__)
#print(lamp2.intensidade)               #ERROR AttributeError



