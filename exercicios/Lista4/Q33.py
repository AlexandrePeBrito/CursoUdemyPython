
#Faça um programa que leia um vetor de 15 posições e o
#compacte, ou seja, elimine as posições com valor zero.
#Para isso, todos os elementos à frente do valor zero, 
#devem ser movidos uma posição para trás no vetor.
import random
vetorA=[]
for c in range(0,10):
    n1=random.randint(0,100)
    vetorA.append(n1)
print(vetorA)
for c in range(0,10):
    if(vetorA[c]==0):
        vetorA.pop(c)
        vetorA.insert(0,0)
print(vetorA)

