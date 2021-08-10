#Faça um programa para verificar se um determinado número 
#inteiro e divisível por 3 ou 5, mas não simultaneamente 
#pelos dois.

num=int(input("Informe um numero inteiro: "))

if(num%3==0 and num%5==0):
    print("Errado")
else:
    print("Correto")
