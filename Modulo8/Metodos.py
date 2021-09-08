""" 
Metodos -> São ações/Comportamentos que um objeto faz para um sistema.

    *Metodos de Instancia   -> Metodo que esta na mesma classe fazendo o acesso a um atributo
    *Metodos de Classe      -> Metodo que não faz acesso a nenhum atributo de instancia

"""
#*Metodos de Instancia
""" 
class Produto():
    def __init__(self,nome,descricao,valor):
        self.__valor=valor
        self.__nome=nome
        self.__descricao=descricao
        
    def desconto(self,porcentagem):
        return (self.__valor*(100-porcentagem))/100

p1=Produto('garrafa','Agua mineral',4)

print(p1.desconto(10))                  #Chamada de metodo  
print(Produto.desconto(p1,10))          #Chamada de metodo



class Usuario():
    def __init__(self,nome,email,senha):
        self.__nome=nome
        self.__email=email
        self.__senha=senha """


    
#Metodos de Classe
class Usuario():
    contador=0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} Usuarios no sistema')

    def __init__(self,nome,email,senha):
        self.__id=Usuario.contador+1
        self.__nome=nome
        self.__email=email
        self.__senha=senha
        Usuario.contador=self.__id

class Produto():
    def __init__(self,nome,descricao,valor):
        self.__valor=valor
        self.__nome=nome
        self.__descricao=descricao
        
    def desconto(self,porcentagem):
        return (self.__valor*(100-porcentagem))/100

user1=Usuario('alexandre','user@gamil.com','13248759')

Usuario.conta_usuarios()