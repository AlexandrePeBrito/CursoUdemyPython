#Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
#acordo com a tabela abaixo:

#     IMC    |  Classificação
#   <18,5    |  Abaixo do Peso
#18,6 - 24,9 |      Saudável
#25,0 - 29,9 |  Peso em excesso
#30,0 - 34,9 |    Obesidade I
#35,0 - 39,9 |    Obesidade II
#   >40,0    |    Obesidade III

import math


peso=float(input("Informe o peso: "))
altura=float(input("Informe a altura: "))
IMC = peso / (math.pow(altura,2))

if(IMC<=18.5):
    print("Abaixo do peso")
elif(18.5<IMC<=24.9):
    print("Saudavel")
elif(24.9<IMC<=29.9):
    print("Peso em excesso")
elif(29.9<IMC<=34.9):
    print("Obesidade 1")
elif(34.9<IMC<=39.9):
    print("Obesidade 2")
elif(40<IMC):
    print("Obesidade 3")