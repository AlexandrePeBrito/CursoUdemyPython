#Faça um programa que leia um número inteiro positivo par 
#N e imprima todos os números pares de O até N em ordem 
#decrescente.

n=int(input("Informe  um numero inteiro positivo par: "))

if(n%2==0):
    for c in range(n,0,-1):
        if(c%2==0):
            print(c)
else:
    print("Valor Invalido")