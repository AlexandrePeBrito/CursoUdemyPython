#Faça um programa que leia dois vetores de 10 elementos. 
#Crie um vetor que seja a união entre os 2 vetores 
#anteriores, ou seja, que contém os números dos dois 
#vetores. Não deve conter números repetidos.
import random
vetorA=[]
vetorB=[]
vetorC=[]
for c in range(0,10):
    n1=random.randint(1,100)
    n2=random.randint(1,100)
    vetorA.append(n1)
    vetorB.append(n2)
print(vetorA)
print(vetorB)
vetorC=set(vetorA+vetorB)
print(vetorC)