#Faça um programa que simula o lançamento de dois dados, 
#dl e d2, n vezes, e tem como saída o número de cada dado 
#e a relação entre eles (>,<,=) de cada lançamento.
import random
n=int(input("Informe o numero de vezes: "))

for c in range(1,n+1):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    if(d1<d2):
        print(f"D1= {d1} < D2= {d2}")
    elif(d2<d1):
        print(f"D1= {d1} > D2= {d2}")
    elif(d1==d2):
        print(f"D1= {d1} = D2= {d2}")

