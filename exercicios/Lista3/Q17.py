#Faça um programa que leia um número inteiro positivo n e 
#calcule a soma dos n primeiros números naturais.

n=int(input("Informe um numero inteiro positivo: "))
num=0
for c in range(0,n):
    if(c>=0):
        num=num+c

print(f"A soma dos numeros eh {num}")