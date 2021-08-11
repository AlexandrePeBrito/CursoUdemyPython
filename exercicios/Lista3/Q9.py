#Faça um programa que leia um número inteiro N e depois 
#imprima os N primeiros números naturais ímpares.

n=int(input("Informe um numero inteiro: "))
c=1
u=0
while(c!=0):
    if(c%2==1):
        print(c)
        u+=1
    if(u==n):
        break
    c+=1
