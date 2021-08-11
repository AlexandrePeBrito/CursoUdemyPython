
#Escreva um programa que leia 10 números inteiros e os 
#armazene em um vetor. Imprima o vetor, o maior elemento e
#a posição que ele se encontra.
vetor=[]
for c in range(0,10):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(max(vetor))
print(vetor.index(max(vetor)))