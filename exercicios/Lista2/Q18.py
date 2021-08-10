#Faça um programa que mostre ao usuário um menu com 4 opções
#de operações matemáticas (as básicas, por exemplo).
#O usuário escolhe uma das opções e o seu programa então
#pede dois valores numéricos e realiza a operação, mostrando
#o resultado e saindo.

menu=int(input("\tMENU\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\t: "))

if(menu==1):
    n1=int(input("Informe um numero: "))
    n2=int(input("Informe um numero: "))
    print(f"O resultado da soma eh {n1+n2}")
elif(menu==2):
    n1=int(input("Informe um numero: "))
    n2=int(input("Informe um numero: "))
    print(f"O resultado da subtração eh {n1-n2}")
elif(menu==3):
    n1=int(input("Informe um numero: "))
    n2=int(input("Informe um numero: "))
    print(f"O resultado da multiplicação eh {n1*n2}")
elif(menu==4):
    n1=int(input("Informe um numero: "))
    n2=int(input("Informe um numero: "))
    print(f"O resultado da divisão  eh {n1*n2}")