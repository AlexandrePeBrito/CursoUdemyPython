#Faça um programa que leia um número e, caso ele 
#seja positivo, calcule e mostre:

#O número digitado ao quadrado
#A raiz quadrada do número digitado
import math
num=int(input("Informe um numero: "))

if(num>0):
    print(f"O numero ao Quadrado eh {math.pow(num,2)} e a raiz quadrada eh {math.sqrt(num)} ")
else:
    print(f"O numero informado eh {num}")