#Faça um programa que preencha um vetor com 10 números reais,
#calcule e mostre a quantidade de números negativos e a 
#soma dos números positivos desse vetor.
vetor=[]
i=0
u=0
for c in range(0,10):
    n=int(input("Informe um numero: "))
    if(n>=0):
        i+=1
    else:
        u+=1
    vetor.append(n)
print(vetor)
print(i)
print(u)
