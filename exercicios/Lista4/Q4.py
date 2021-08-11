#Faça um programa que leia um vetor de 8 posições e, em 
#seguida, leia também dois valores X e Y quaisquer 
#correspondentes a duas posições no vetor. Ao final seu
#programa deverá escrever a soma dos valores encontrados 
#nas respectivas posições X e Y.
vetor=[]
for c in range(0,8):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(vetor)
x=int(input("Informe um numero de 0 e ate 7: "))
y=int(input("Informe um numero de 0 e ate 7: "))
print(vetor[x])
print(vetor[y])

