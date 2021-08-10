#Faça um programa que receba dois números e mostre o maior.
#Se por acaso, os dois números forem iguais, 
#imprima a mensagem Números iguais.

valores=[]

for c in range(0,2):
    num=int(input("Informe um numero inteiro:"))
    valores.append(num)

if(valores[0]==valores[1]):
    print("Os numeros sao iguais.")
else:
    print(f"O maior numero entre eles eh o {max(valores)}")

