#Fazer um programa para ler 5 valores e, em seguida, mostrar 
#todos os valores lidos juntamente com o maior, o menor e 
#a média dos valores.
vetor=[]
for c in range(0,5):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(vetor)
print(f"{max(vetor)}")
print(f"{min(vetor)}")
