#Faça um programa que leia três números inteiros positivos e 
#efetue o cálculo de uma das seguintes médias de acordo com 
#um valor numérico digitado pelo usuário:

#(a) Geométrica: raiz_cubica(x*y*z)
#(b) Ponderada: (x+2y+3z)/6
#(o) Harmônica: 1/((1/x)+(1/y)+(1/z))
#(d) Aritmética: (x+y+z)/3
import math


valores=[]
for c in range(0,3):
    n=int(input("Informe um numero: "))
    valores.append(n)

geometrica= (valores[0]*valores[1]*valores[2])**(1/3)
ponderada=  (valores[0]+(2*valores[1])+(3*valores[2]))/6
harmonica=1/((1/valores[0])+(1/valores[1])+(1/valores[2]))
aritmetica=sum(valores)/3

print(f"Geométrica: {geometrica}\n\
Ponderada: {ponderada}\n\
Harmônica: {harmonica}\n\
Aritmética: {aritmetica}")