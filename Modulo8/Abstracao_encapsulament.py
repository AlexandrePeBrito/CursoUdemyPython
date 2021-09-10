""" 
Abstração       ->
Encapsulamento  -> capsular o elementos em uma classe

"""

class Conta():
    contador=400
    def __init__(self,titular,saldo,limite):
        self.__numero=Conta.contador
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        Conta.contador+=1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self,valor):
        if valor>0:
            self.__saldo+=valor
        else:
            print("Valor invalido")

    def sacar(self,valor):
        if valor>0:
            if self.__saldo>=valor:
                self.__saldo-=valor
            else:
                print("Saldo Insuficiente")
        else:
            print("Valor invalido")

conta1=Conta('alexandre',500,1000)

#eh possivel alterar os dados