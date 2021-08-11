
#Faça um programa que receba do usuário um vetor com 10 
#posições. Em seguida deverá ser impresso o maior e o menor
#elemento do vetor.
vetor=[]
for c in range(0,10):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(max(vetor))
print(min(vetor))