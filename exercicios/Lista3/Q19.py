#Escreva um algoritmo que leia um número inteiro entre 100
#e 999 e imprima na saída cada um dos algarismos que compõem 
#o número
import random

n=random.randint(100,999)
txt=str(n)
print(f"O numero {txt[0]} compoe o numero {n}")