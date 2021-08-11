#Faça um programa que calcule o terno pitagórico a, b, c, 
#para o qual a+b+c = 1000. Um terno pitagórico é um conjunto
#de três números naturais, a, b, c, para a qual,
#a^2+b^2=c^2
#Por exemplo,
#3^2+4^2=9+16=25=5^2
import math
a=int(input("Informe um numero: "))
b=int(input("Informe um numero: "))

c=pow(a,2)+pow(b,2)
d=math.sqrt(c)
print(f"{a}^2 + {b}^2 = {pow(a,2)} + {pow(b,2)} = {c} = {d}^2")
