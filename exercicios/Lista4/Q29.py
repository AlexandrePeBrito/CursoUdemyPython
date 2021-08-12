#Faça um programa que receba 6 números inteiros e mostre:
#e Os números pares digitados;
#e A soma dos números pares digitados;
#e Os números ímpares digitados;
#e A quantidade de números ímpares digitados;
import random
vetor=[]
vetorP=[]
vetorI=[]
for c in range(0,6):
    n=random.randint(0,50)
    vetor.append(n)
    if(n%2==0):
        vetorP.append(n)
    else:
        vetorI.append(n)
print(vetor)
print(vetorP)
print(sum(vetorP))
print(len(vetorI))