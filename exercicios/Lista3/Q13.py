#Faça um programa que leia um número inteiro positivo par 
#N e imprima todos os números pares de O até N em ordem 
#crescente.

n=int(input("Informe um numero inteiro: "))

for c in range(0,n):
    if(c%2==0):
        print(c)