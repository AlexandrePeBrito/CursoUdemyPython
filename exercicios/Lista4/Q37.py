
#Considere um vetor A com 11 elementos onde 
#A1 < A2 < ... < A6 > A7 > A8 >... > A11, ou seja, está 
#ordenado em ordem crescente até o sexto elemento, e a partir
#desse elemento está ordenado em ordem decrescente. Dado 
#o vetor da questão anterior, proponha um algoritmo para
#ordenar os elementos.
import random
vetorA=[]
vetorB=[]
for c in range(0,11):
    n=random.randint(0,50)
    vetorA.append(n)
print(vetorA)
vetorA.sort()
for c in range(6,11):
    vetorB.append(vetorA[c])
    vetorB.sort()
    
u=4
for c in range(6,11):
    vetorA[c]=vetorB[u]
    u-=1
    
print(vetorA)