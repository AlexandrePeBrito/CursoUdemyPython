#Faça um programa que leia um vetor de 10 números. Leia um
#número x. Conte os múltiplos de um número inteiro x num
#vetor e mostre-os na tela.
vetor=[]
n=int(input("Informe um numero: "))
for c in range(1,11):
   vetor.append(c*n)
print(vetor)
