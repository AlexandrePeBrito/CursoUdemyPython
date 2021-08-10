#Escreva um programa que, dados dois números inteiros,
#mostre na tela o maior deles, assim como a diferença
#existente entre ambos.
valores=[]

for c in range(0,2):
    num=int(input("Informe um numero inteiro:"))
    valores.append(num)

print(f"O maior numero entre eles eh o {max(valores)}")

print(f"A diferença entre eles eh o {max(valores)-min(valores)}")
