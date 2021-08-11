#Faça um programa que apresente um menu de opções para 
#o cálculo das seguintes operações entre dois números:
#* adição (opção 1)
#* subtração (opção 2)
#* multiplicação (opção 3)
#* divisão (opção 4).
#* saída (opção 5)
#O programa deve possibilitar ao usuário a escolha da
#operação desejada, a exibição do resultado e a volta
#ao menu de opções. O programa só termina quando for
#escolhida a opção de saída (opção 5).
n=[]
menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))

while(menu!=5):
    n.append(int(input("Informe um numero inteiro: ")))
    n.append(int(input("Informe um numero inteiro: ")))
    if(menu==1):
        res=n[0]+n[1]
        print(f"O resultado da operacao eh {res}")
        menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))
    elif(menu==2):
        res=n[0]-n[1]
        print(f"O resultado da operacao eh {res}")
        menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))
    elif(menu==3):
        res=n[0]*n[1]
        print(f"O resultado da operacao eh {res}")
        menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))
    elif(menu==4):
        res=n[0]/n[1]
        print(f"O resultado da operacao eh {res}")
        menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))
    else:
        print("\nOpção invalida!")
        menu=int(input("1-adição\n\
2-subtração\n\
3-multiplicação\n\
4-divisão\n\
5-saída:\t"))
