""" 
Polimorfismo -> são metodos abstratos
"""

class Animal(object):
    def __init__(self,nome):
        self.__nome=nome
    
    def falar(self):        #Metodo
        raise NotADirectoryError("A classe filha precisa implementar este metodo")
    
    def comer(self):
        print(f'{self.__nome} esta comendo')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala Au Au Au")

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala Miau Miau")

dog=Cachorro('zelda')
cat=Gato("Nimbus")
dog.falar()
cat.falar()