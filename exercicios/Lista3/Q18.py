#Escreva um algoritmo que leia certa quantidade de números e 
#imprima o maior deles e quantas vezes o maior número foi
#lido. A quantidade de números a serem lidos deve ser 
#fornecida pelo usuário.
valores=[]
qnt=int(input("Informe a quantidades de numeros deseja inserir: "))

for c in range(0,qnt):
    num=int(input("Informe um numero: "))
    valores.append(num)

print(f'O maior valor inserido eh {max(valores)} \
e o numeros de vezes que ele apareceu eh \
{valores.count(max(valores))}')