#Faça um programa que leia um vetor de 10 posições e verifique
#se existem valores iguais e os escreva na tela.
vetor=[]
for c in range(0,10):
    n=int(input("Informe um numero: "))
    if n in vetor:
        print(f"{n}")
    vetor.append(n) 

