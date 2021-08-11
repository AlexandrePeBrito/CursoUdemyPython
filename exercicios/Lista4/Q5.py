#Leia um vetor de 10 posições. Contar e escrever quantos
#valores pares ele possui.
vetor=[]
i=0
for c in range(0,10):
    n=int(input("Informe um numero: "))
    vetor.append(n)
    if(n%2==0):
        i+=1
print(i)