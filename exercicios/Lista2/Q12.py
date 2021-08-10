#Ler um número inteiro. Se o número lido for negativo,
#escreva a mensagem “Número inválido”.
#Se o número for positivo, calcular o logaritmo
#deste numero.
import math
n=int(input("Informe um numero inteiro: "))

if(n<0):
    print("Numero invalido!")
elif(n>0):
    print(math.log(n))