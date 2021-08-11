#Faça um programa que leia um número inteiro positivo ímpar 
#N e imprima todos os números impares de 1 até N em ordem 
#decrescente.

n=int(input("Informe  um numero inteiro positivo impar: "))

if(n%2==1):
    for c in range(n,0,-1):
        if(c%2==1):
            print(c)
else:
    print("Valor Invalido")