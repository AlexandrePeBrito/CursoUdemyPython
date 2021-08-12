#Faça um programa que leia dois vetores de 10 elementos. 
#Crie um vetor que seja a intersecção entre os 2 vetores
#anteriores, ou seja, que contém apenas os números que
#estão em ambos os vetores. Não deve conter números 
#repetidos.
import random
vetorA=[]
vetorB=[]
vetorC=[]
for c in range(0,10):
    n1=random.randint(1,100)
    n2=random.randint(1,100)
    vetorA.append(n1)
    vetorB.append(n2)
for c in range(0,10):
    if(vetorA[c] in vetorA and vetorA[c] in vetorB):
        vetorC.append(vetorA[c])
print(vetorA)
print(vetorB)
print(vetorC)
