#Leia a altura e o raio de um cilindro circular e
#imprima o volume do cilindro. O volume de um cilindro
#circular é calculado por meio da seguinte 
#fórmula: V = pi +raio^2 x altura, onde pi = 3.141592.
import math

altura=int(input("Informe a altura do cilindro: "))
raio=int(input("Informe o raio do cilindro: "))

v=3.14+pow(raio,2)*altura

print(f"O volume do cilindro eh {v}")

