#leia o valor do raio de um circulo e 
#calcule e imprima a area do circulo correspondente.
#A area do circulo eh pi*raio^2, considere pi=3.141592
import math
raio=float(input("Informe o raio do circulo: "))

area=3.141592*pow(raio,2)

print(f"Area do circulo eh {round(area,2)}")