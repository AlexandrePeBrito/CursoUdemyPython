#Faça um programa que receba três números e mostre-os em 
#ordem crescente.

valores=[]
for c in range(0,3):
    n=int(input("Informe um numero: "))
    valores.append(n)
valores.sort()
print(f"O numero em ordem crescente eh {valores}")