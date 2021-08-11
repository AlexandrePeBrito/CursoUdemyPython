
#Fazer um programa para ler 5 valores e, em seguida, 
#mostrar a posição onde se encontram o maior e o menor valor.
vetor=[]
for c in range(0,5):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(max(vetor))
print(min(vetor))