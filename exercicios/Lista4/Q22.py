#Faça um programa que leia dois vetores de 10 posições e
#calcule outro vetor contendo, nas posições pares os valores
#do primeiro e nas posições impares os valores do segundo.
import random
vetorA=[]
vetorB=[]
vetorC=[]
for c in range(0,10):
    n1=random.randint(1,20)
    n2=random.randint(1,20)
    vetorA.append(n1)
    vetorB.append(n2)
i=0
u=0
for c in range(0,len(vetorA)*2):
    if(c%2==0):
        vetorC.append(vetorA[i])
        i+=1
    elif(c%2==1):
        vetorC.append(vetorB[u])
        u+=1
print(vetorA)
print(vetorB)
print(vetorC)



