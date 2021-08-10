#Faça um programa que receba dois números e 
#mostre qual deles é o maior.

valores=[]
for c in range(0,2):
    num=float(input("Informe um numero: "))
    valores.append(num)

print(max(valores))