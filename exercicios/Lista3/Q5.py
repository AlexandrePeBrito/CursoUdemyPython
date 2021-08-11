#Faça um programa que peça ao usuário para digitar 10 
#valores e some-os.

valores=[]

for c in range(0,10):
    n=int(input("Informe um numero: "))
    valores.append(n)

print(f"A somas dos valores eh {sum(valores)}")