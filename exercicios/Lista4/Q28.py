#Leia 10 números inteiros e armazene em um vetor v. Crie dois
#novos vetores v1 e v2. Copie os valores ímpares de v para
#v1, e os valores pares de v para v2. Note que cada um dos
#vetores v1 e v2 têm no máximo 10 elementos, mas nem todos 
#os elementos são utilizados. No final escreva os elementos
#UTILIZADOS de v1 e v2.
import random
v=[]
v1=[0,0,0,0,0,0,0,0,0,0]
v2=[0,0,0,0,0,0,0,0,0,0]
for c in range(0,10):
    n=random.randint(1,50)
    v.append(n)
    if(n%2==0):
        v2[c]=n
    else:
        v1[c]=n
print(v)
for c in range(0,10):
    if(v1[c]!=0):
        print(f"V1 = {v1[c]}")
    elif(v2[c]!=0):
        print(f"V2 = {v2[c]}")