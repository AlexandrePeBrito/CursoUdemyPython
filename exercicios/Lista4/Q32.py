#Leia dois vetores de inteiros x e y, cada um com 5 elementos
#(assuma que o usuário não informa elementos repetidos). 
#Calcule e mostre os vetores resultantes em cada caso abaixo:
#*Soma entre x e y: soma de cada elemento de x com o elemento
#da mesma posição em y.
#*Produto entre : e y: multiplicação de cada elemento de : 
#como elemento da mesma posição em y.
#*Diferença entre x e y: todos os elementos de r que não
#existam em y.
#*Interseção entre x e y: apenas os elementos que aparecem
#nos dois vetores.
#*União entre x e y: todos os elementos de , e todos os 
#elementos de y que não estão em r.
import random
vetorA=[]
vetorB=[]
for c in range(0,5):
    n1=random.randint(1,20)
    n2=random.randint(1,20)
    vetorA.append(n1)
    vetorB.append(n2)
for c in range(0,5):
    print(f"A Soma entre os numeros {vetorA[c]} e {vetorB[c]} eh {vetorA[c]+vetorB[c]}")
for c in range(0,5):
    print(f"O Produto entre os numeros {vetorA[c]} e {vetorB[c]} eh {vetorA[c]*vetorB[c]}")
for c in range(0,5):
    if(vetorA[c] in vetorB):
        print(f"O numero {vetorA[c]} esta em ambos os vetores")
print(f"A junção dos dois vetores da os numeros {set(vetorA+vetorB)} ")



