#Leia um numero real. Se o número for positivo
#imprima a raiz quadrada. Do contrário, imprima 
#o numero ao quadrado.
import math
num=int(input("Informe um um numero: "))

if(num>0):
    print(f"A raiz quadrada do {num} eh {math.sqrt(num)}")
else:
    print(f"O {num} ao quadrado eh {math.pow(num,2)}")