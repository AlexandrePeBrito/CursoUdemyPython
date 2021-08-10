#Leia um angulo em radianos e apresente-o convertido em graus.
#A formula de conversao eh: G=R*180/pi,
#sendo G o angulo em graus e R em radianos e pi=3,14

import math

angulo=float(input("Informe o radiano: "))

G=(math.radians(angulo)*180)/3.14

print(f"O Radiano do angulo eh {G}")