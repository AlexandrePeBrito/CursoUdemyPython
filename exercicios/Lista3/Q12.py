#Faça um programa que leia um número inteiro positivo N e 
#imprima todos os números naturais de O até N em ordem 
#decrescente.

n=int(input("Informe um numero inteiro: "))

for c in range(n,-1,-1):
    print(c)