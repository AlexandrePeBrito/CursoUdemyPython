#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
#Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
#NúmeroLido = 123
#NúmeroGerado = 321.

num=int(input("Informe um numero: "))
num=str(num)
num=num[::-1]
print(int(num))