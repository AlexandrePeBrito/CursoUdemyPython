#Escreva um programa que leia números inteiros no intervalo
#[0,50] e os armazene em um vetor com 10 posições. Preencha
#um segundo vetor apenas com os números ímpares do primeiro
#vetor. Imprima os dois vetores, 2 elementos por linha.
import random
vetorA=[]
vetorB=[]
for c in range(0,10):
    n=random.randint(0,50)
    vetorA.append(n)
for c in range(0,10):
    if (vetorA[c]%2==1):
        vetorB.append(vetorA[c])
print("Vetor A")
print(f"{vetorA}")
print("Vetor B")
print(f"{vetorB}")