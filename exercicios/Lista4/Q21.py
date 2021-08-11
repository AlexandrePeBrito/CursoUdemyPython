#Faça um programa que receba do usuário dois vetores, A e B
#,com 10 números inteiros cada. Crie um novo vetor 
#denominado C calculando C = A - B. Mostre na tela os dados
#do vetor C.
import random
vetorA=[]
vetorB=[]
vetorC=[]
for c in range(0,10):
    n1=random.randint(1,20)
    n2=random.randint(1,20)
    vetorA.append(n1)
    vetorB.append(n2)

for c in range(0,10):
    vetorC.append(vetorA[c]-vetorB[c])

print(vetorA)
print(vetorB)
print(vetorC)