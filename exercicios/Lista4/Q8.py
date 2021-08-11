
#Crie um programa que lê 6 valores inteiros e, em seguida, 
#mostre na tela os valores lidos na ordem inversa.
vetor=[]
for c in range(0,6):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(vetor[::-1])