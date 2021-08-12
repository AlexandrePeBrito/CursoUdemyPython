#Leia 10 números inteiros e armazene em um vetor. Em seguida
#escreva os elementos que são primos e suas respectivas
#posições no vetor.
import random
vetorA=[]
primo={}
for c in range(0,10):
    n1=random.randint(1,50)
    vetorA.append(n1)
    p=0
    for u in range(1,n1+1):
        if(n1%u==0):
            p+=1
    if(p<=2):
        primo[n1]=c
print(vetorA)
print(primo)

