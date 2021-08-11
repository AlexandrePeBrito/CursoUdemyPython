
#Faça um programa para ler a nota da prova de 15 alunos e
#armazene num vetor, calcule e imprima a média geral.
vetor=[]

for c in range(0,15):
    n=int(input("Informe um numero: "))
    vetor.append(n)
print(sum(vetor)/15)