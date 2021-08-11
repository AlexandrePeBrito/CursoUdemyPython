#Escreva um programa que leia 10 números e escreva o menor 
#valor lido e o maior valor lido.

valores=[]

for c in range(0,10):
    n=int(input("Informe um numero: "))
    valores.append(n)

print(f"O menor Valor eh {min(valores)} e o Maior valor eh {max(valores)}")
