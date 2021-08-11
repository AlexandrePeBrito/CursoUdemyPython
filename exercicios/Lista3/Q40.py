#Elabore um programa que faça leitura de vários números 
#inteiros, até que se digite um número negativo. O programa
#tem que retornar o maior e o menor número lido.
n=int(input("Informe um numero: "))
valores=[]
while(n>=0):
    valores.append(n)
    n=int(input("Informe um numero: "))
print(f"O maior numero eh {max(valores)} e o menor numero eh {min(valores)}")
