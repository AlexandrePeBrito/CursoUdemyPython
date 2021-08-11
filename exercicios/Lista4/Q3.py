#Ler um conjunto de números reais, armazenando-o em vetor 
#e calcular o quadrado das componentes deste vetor, 
#armazenando o resultado em outro vetor. Os conjuntos têm
#10 elementos cada. Imprimir todos os conjuntos.
vetorA=[]
vetorB=[]
for i in range(0,10):
    n=int(input("\nInforme um numero: "))
    vetorA.append(n)
for c in range(0,len(vetorA)):
    vetorB.append(pow(vetorA[c],2))
print(vetorA)
print(vetorB)
