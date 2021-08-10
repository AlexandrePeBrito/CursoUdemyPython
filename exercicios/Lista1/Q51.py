#Escreva um programa que leia as coordenadas x e y 
#de pontos no R^2 e calcule sua distância da origem (0,0).

from math import sqrt


x=int(input("Informe o valor de X: "))
y=int(input("Informe o valor de Y: "))

d=sqrt(pow(x,2)+pow(y,2))
print(f"A distancia eh {d} do centro(0,0)")