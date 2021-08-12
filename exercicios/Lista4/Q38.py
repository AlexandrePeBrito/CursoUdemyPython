#Peça ao usuário para digitar dez valores numéricos e ordene
#por ordem crescente esses valores, guardando-os num vetor. 
#Ordene o valor assim que ele for digitado. Mostre ao final
#na tela os valores em ordem.
import random
vetorA=[]
for c in range(0,3):
    n=random.randint(0,50)
    #print(n)
    vetorA.append(n)
    print(vetorA[c])
vetorA.sort()
print(vetorA)

