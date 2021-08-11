#Leia um vetor de 10 posições e atribua valor O para todos os
#elementos que possuírem valores negativos.
import random
vetor=[]
for c in range(0,10):
    n=random.randint(-20,20)
    vetor.append(n)
print(vetor)
for c in range(0,10):
    if(vetor[c]<0):
        vetor[c]=0
print(vetor)
