#Sejam a e b os catetos de um triangulo, 
#onde a hipotenusa eh obtida pela equação:
#hipotenusa = raiz(a^2+b^2).
#faça um programa que receba os valores de a e b e 
#calcule o valor da hipotenusa atraves da equação.
#imprima o resultado dessa operação
import math

a=int(input("Informe o valor do cateto a: "))
b=int(input("Informe o valor do cateto b: "))

hipotenusa=math.sqrt(pow(a,2)+pow(b,2))

print(f"O valor da hipotenusa eh {hipotenusa}")