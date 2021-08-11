#Faça um programa que leia um conjunto não determinado de 
#valores, um de cada vez, e escreva para cada um dos valores
#lidos, o quadrado, o cubo e a raiz quadrada. Finalize a 
#entrada de dados com um valor negativo ou zero.
import math
num=int(input("Informe um numero: "))
while(num>=0):
    opcao=(int(input("\n1-O quadrado\n2-O cubo\n\
3-A raiz quadrada: ")))
    if(opcao==1):
        num=pow(num,2)
        print(f"\nO quadrado do numero eh {num}")
    elif(opcao==2):
        num=pow(num,3)
        print(f"\nO cubo do numero eh {num}")
    elif(opcao==3):
        num=math.sqrt(num)
        print(f"\nA raiz quadrada eh {num}")
    else:
        print("\nOpção invalida!")
    num=int(input("\nInforme um numero: "))
print("\nSistema Finalizado")