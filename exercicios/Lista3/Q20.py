#Ler uma sequência de números inteiros e determinar se eles
#são pares ou não. Deverá ser informado o número de dados
#lidos e número de valores pares. O processo termina quando
#for digitado o número 1000.
import random
valores=[]
i=0
n=random.randint(0,15)
for c in range(0,n):
    num=random.randint(0,100)
    valores.append(num)
    if(num%2==0):
        i+=1
print(f"O numero total de elementos sao {len(valores)} e tem {i} numeros pares")
