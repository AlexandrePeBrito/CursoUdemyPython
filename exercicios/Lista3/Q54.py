#Faça um programa que receba um número inteiro maior do que 
#1, e verífique se o número fornecido é primo ou não.
n=int(input("Informe um numero maior que 1: "))
i=0
if(n>1):
    for c in range(1,n+1):
        if(n%c==0):
            i+=1
    if(i<=2):
        print(f"{n} eh um numero PRIMO")
    else:
        print(f"{n} NAO eh um numero primo")
