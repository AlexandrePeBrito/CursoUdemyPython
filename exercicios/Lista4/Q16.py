#Faça um programa que leia um vetor de 5 posições para números
#reais e, depois, um código inteiro. Se o código for zero,
#finalize o programa; se for 1, mostre o vetor na ordem 
#direta; se for 2, mostre o vetor na ordem inversa. Caso, 
#o código for diferente de 1 e 2 escreva uma mensagem 
#informando que o código é inválido.
vetor=[]
for c in range(0,5):
    n=float(input("Informe um numero: "))
    vetor.append(n)
menu=int(input("\n0-finalizar\n\
1-Imprimir vetor\n\
2-Imprimir vetor Inverso: "))
while(menu!=0):
    if(menu==1):
        print(f"\n{vetor}")
    elif(menu==2):
        print(f"\n{vetor[::-1]}")
    menu=int(input("\n0-finalizar\n\
1-Imprimir vetor\n\
2-Imprimir vetor Inverso: "))