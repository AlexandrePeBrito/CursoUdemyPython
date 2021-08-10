#Leia um número inteiro de 4 dígitos (de 1000 a 9999) 
#e imprima 1 dígito por linha.


num=int(input("Informe um numero de 4 digitos: "))
num=str(num)

for c in range(0,4):
    print(num[c])
