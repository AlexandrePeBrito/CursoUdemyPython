#Leia um vetor com 10 números reais, ordene os elementos 
#deste vetor, e no final escreva os elementos do vetor 
#ordenado.
import random
vetorA=[]
for c in range(0,10):
    n=random.randint(0,50)
    vetorA.append(n)
print(vetorA)
vetorA.sort()
print(vetorA)
