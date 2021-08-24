#8. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
#hipotenusa =raiz(a^2+b^2) Faça uma função que receba os valores de a e b e calcule o
#valor da hipotenusa através da equação.
import math
def hip(a,b):
    return math.sqrt(pow(a,2)+pow(b,2))

a=float(input('Informe o valor do cateto: '))
b=float(input('Informe o valor do cateto: '))
h=hip(a,b)
print(f"O valor da hipotenusa eh {h}")