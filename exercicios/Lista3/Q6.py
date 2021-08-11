#Faça um programa que leia 10 inteiros e imprima sua 
#média.

valores=[]

for c in range(0,10):
    n=int(input("Informe um numero: "))
    valores.append(n)

print(f"A somas dos valores eh {(sum(valores))/10}")