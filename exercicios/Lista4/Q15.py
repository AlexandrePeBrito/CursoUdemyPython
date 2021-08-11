#Leia um vetor com 20 números inteiros. Escreva os elementos
#do vetor eliminando elementos repetidos.
vetor=[]
for c in range(0,20):
    n=int(input("Informe um numero: "))
    vetor.append(n)
    if(vetor.count(n)!=1):
        vetor.pop(n)
