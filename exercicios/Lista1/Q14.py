#Leia um angulo em graus e apresente-o convertido em radianos.
#A formula de conversao eh: R=G*pi/180,
#sendo G o angulo em graus e R em radianos e pi=3,14
import math

angulo=float(input("Informe o angulo: "))

R=math.radians(angulo)

print(f"O Radiano do angulo eh {round(R,1)}")