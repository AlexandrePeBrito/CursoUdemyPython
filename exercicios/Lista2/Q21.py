#Escreva o menu de opções abaixo. Leia a opção do usuário e 
#execute a operação escolhida. Escreva uma mensagem de erro 
#se a opção for inválida.
#Escolha a opção:
#1- Soma de 2 números.
#2- Diferença entre 2 números (maior pelo menor).
#3- Produto entre 2 números.
#4- Divisão entre 2 números (o denominador não pode ser zero).
#Opção
valores=[]
menu=int(input("\tMENU\n1-Soma de 2 Numeros\n\
2-Diferença entre 2 números\n\
3-Produto entre 2 números\n\
4-Divisão entre 2 números\t: "))

if(menu==1):
    for c in range(0,2):
        n=int(input("Informe um numero: "))
        valores.append(n)
    print(f"O resultado da soma eh {sum(valores)}")
elif(menu==2):
    for c in range(0,2):
        n=int(input("Informe um numero: "))
        valores.append(n)
    print(f"O resultado da subtração eh {max(valores-min(valores))}")
elif(menu==3):
    for c in range(0,2):
        n=int(input("Informe um numero: "))
        valores.append(n)
    print(f"O resultado da multiplicação eh {valores[0]*valores[1]}")
elif(menu==4):
    for c in range(0,2):
        n=int(input("Informe um numero: "))
        valores.append(n)
    if(valores[1]>0):
        print(f"O resultado da divisão  eh {valores[0]*valores[1]}")
    else:
        print(f"Denominador igual a 0")
